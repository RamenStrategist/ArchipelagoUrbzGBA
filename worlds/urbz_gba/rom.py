import os
import pkgutil
import typing

import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from .data import rom_addresses
from .items import item_table
from .text import encode_text
from .regions import PokemonRBWarp, map_ids, town_map_coords

if typing.TYPE_CHECKING:
    from . import UrbzWorld

class UrbzProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Urbz Sims in the City"
    hash = "8efd27375d1f92b43fe0d1c93a63c08b7a259acc"
    patch_file_ending = ".apurb"
    result_file_ending = ".gb"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"]),
    ]

def generate_output(world: "UrbzWorld", output_directory: str):
    game_version = world.options.game_version.current_key

    # Guestimating based on other world's rom file
    patch_type = UrbzProcedurePatch
    patch = patch_type(player=world.player, player_name=world.player_name)
    patch.write_file("base_patch.bsdiff4", pkgutil.get_data(__name__, f"basepatch_{game_version}.bsdiff4"))

    # Set slot auth
    patch.write_token(APTokenTypes.WRITE, rom_addresses["gArchipelagoInfo"], world.auth)

    patch.write_file("token_data.bin", patch.get_token_binary())
    out_file_name = world.multiworld.get_out_file_name_base(world.player)
    patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))