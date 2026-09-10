import base64
import time
from typing import TYPE_CHECKING, Optional, Dict, Set, Tuple

import worlds._bizhawk as bizhawk
from worlds._bizhawk import read, write, guarded_write
from worlds._bizhawk.client import BizHawkClient

from .options import Goal, RemoteItems

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

EXPECTED_ROM_NAME = "urbz"

DATA_LOCATIONS = {
    "ItemIndex": (0x1A6E, 0x02),
    "Deathlink": (0x00FD, 0x01),
    "APItem": (0x00FF, 0x01),
    "EventFlag": (0x1735, 0x140),
    "ResetCheck": (0x0100, 4),
}
class UrbzClient(BizHawkClient):
    system = "GBA"
    patch_suffix = ".apurb"
    game = "Urbz Sims in the City"

    def __init__(self):
        super().__init__()
        self.auto_hints = set()
        self.locations_array = None
        self.disconnect_pending = False
        self.set_deathlink = False
        self.game_state = False
        self.last_death_link = 0
        self.current_map = 0

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger

        try:
            # Check ROM name/patch version
            rom_name_bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x108, 32, "ROM")]))[0])
            rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode("ascii")
            if not rom_name.startswith("Urbz"):
                logger.info("ERROR: You appear to be running an unpatched version of Pokemon Emerald. "
                            "You need to generate a patch file and use it to create a patched ROM.")
                return False
            if rom_name != EXPECTED_ROM_NAME:
                logger.info("ERROR: The patch file used to create this ROM is not compatible with "
                            "this client. Double check your client version against the version being "
                            "used by the generator.")
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b001
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125

        return True

    async def set_auth(self, ctx):
        auth_name = await read(ctx.bizhawk_ctx, [(0xFFC6, 21, "ROM")])
        if auth_name[0] == bytes([0] * 21):
            # rom was patched before rom names implemented, use player name
            auth_name = await read(ctx.bizhawk_ctx, [(0xFFF0, 16, "ROM")])
            auth_name = auth_name[0].decode("ascii").split("\x00")[0]
        else:
            auth_name = base64.b64encode(auth_name[0]).decode()
        ctx.auth = auth_name

    async def game_watcher(self, ctx):
        if not ctx.server or not ctx.server.socket.open or ctx.server.socket.closed:
            return
        data = await read(ctx.bizhawk_ctx, [(loc_data[0], loc_data[1], "WRAM")
                                            for loc_data in DATA_LOCATIONS.values()])
        data = {data_set_name: data_name for data_set_name, data_name in zip(DATA_LOCATIONS.keys(), data)}

        if self.set_deathlink:
            self.set_deathlink = False
            await ctx.update_death_link(True)

        if self.disconnect_pending:
            self.disconnect_pending = False
            await ctx.disconnect()

        if data["GameStatus"][0] == 0 or data["ResetCheck"] == b'\xff\xff\xff\x7f':
            # Do not handle anything before game save is loaded
            self.game_state = False
            return
        self.game_state = True

    def on_package(self, ctx, cmd, args):
        if cmd == 'Connected':
            if 'death_link' in args['slot_data'] and args['slot_data']['death_link']:
                self.set_deathlink = True
                self.last_death_link = time.time()
            ctx.set_notify(f"EnergyLink{ctx.team}")
        super().on_package(ctx, cmd, args)