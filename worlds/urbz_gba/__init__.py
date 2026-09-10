import settings
import typing
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, LocationProgressType
from Fill import sweep_from_pool
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_item_rule
from .items import item_table, item_groups
from .locations import location_data
from .regions import create_regions
from .options import UrbzOptions
from .data import rom_addresses
from .rom import generate_output, UrbzProcedurePatch
from .rules import set_rules
from . import logic
from . import client


class UrbzGbaSettings(settings.Group):
    class UrbzRomFile(settings.UserFilePath):
        description = "Urbz, The - Sims in the City (Usa, Europe) ROM File"
        copy_to = "Urbz, The - Sims in the City (USA, Europe) (En,Fr,De,Es,It,Nl).gba"
        md5s = [UrbzProcedurePatch.hash]

    urbz_rom_file: UrbzRomFile = UrbzRomFile(UrbzRomFile.copy_to)


class UrbzWebWorld(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Urbz GBA with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["RamenStrategist"]
    )

    tutorials = [setup_en]


class UrbzWorld(World):
    """The Urbz: Sims in the City is the second handheld Sims game and the sequel of The Sims Bustin' Out.
    This game is loosely-based on The Sims, with many simulation elements taken from it,
    such as motives and skills. However, the handheld versions feature a unique storyline focused on completing tasks
    to rise to fame. """

    game = "Urbz Sims in the City"

    options_dataclass = UrbzOptions
    options: UrbzOptions

    settings: typing.ClassVar[UrbzGbaSettings]
    topology_present = True

    location_name_to_id = {location.name: location.address for location in location_data if location.type == "Item"
                           and location.address is not None}
    item_name_groups = item_groups

    web = UrbzWebWorld()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.item_pool = []
        self.total_key_items = None
        self.traps = None
        self.local_locs = []

    @classmethod
    def stage_generate_early(cls, multiworld: MultiWorld):

        seed_groups = {}
        urbz_worlds = multiworld.get_game_worlds("Urbz Sims in the City")

        for world in urbz_worlds:
            if not (world.options.type_chart_seed.value.isdigit() or world.options.type_chart_seed.value == "random"):
                seed_groups[world.options.type_chart_seed.value] = seed_groups.get(world.options.type_chart_seed.value,
                                                                                   []) + [world]

        copy_chart_worlds = {}

        for worlds in seed_groups.values():
            chosen_world = multiworld.random.choice(worlds)
            for world in worlds:
                if world is not chosen_world:
                    copy_chart_worlds[world.player] = chosen_world


        for player in copy_chart_worlds:
            multiworld.worlds[player].type_chart = copy_chart_worlds[player].type_chart

    def create_items(self):
        self.multiworld.itempool += self.item_pool

    @classmethod
    def stage_fill_hook(cls, multiworld, progitempool, usefulitempool, filleritempool, fill_locations):
        locs = []
        for world in multiworld.get_game_worlds("Urbz Sims in the City"):
            locs += world.local_locs
        for loc in sorted(locs):
            if loc.item:
                continue
            itempool = progitempool + usefulitempool + filleritempool
            multiworld.random.shuffle(itempool)
            unplaced_items = []
            for i, item in enumerate(itempool):
                if ((item.player == loc.player or (item.player in multiworld.groups
                                                   and loc.player in multiworld.groups[item.player]["players"]))
                        and loc.can_fill(multiworld.state, item, False)):
                    if item.advancement:
                        pool = progitempool
                    elif item.useful:
                        pool = usefulitempool
                    else:
                        pool = filleritempool
                    for i, check_item in enumerate(pool):
                        if item is check_item:
                            pool.pop(i)
                            break
                    if item.advancement:
                        state = sweep_from_pool(multiworld.state, progitempool + unplaced_items)
                    if (not item.advancement) or state.can_reach(loc, "Location", loc.player):
                        multiworld.push_item(loc, item, False)
                        fill_locations.remove(loc)
                        break
                    else:
                        unplaced_items.append(item)
            progitempool += [item for item in unplaced_items if item.advancement]
            usefulitempool += [item for item in unplaced_items if item.useful]
            filleritempool += [item for item in unplaced_items if (not item.advancement) and (not item.useful)]

    def pre_fill(self) -> None:
        # Place local items in some locations to prevent save-scumming.


    def create_regions(self):
        create_regions(self)
        self.multiworld.completion_condition[self.player] = lambda state, player=self.player: state.has("Parade", player=player)

    def set_rules(self):
        set_rules(self.multiworld, self, self.player)

    def create_item(self, name: str) -> Item:
        return UrbzItem(name, self.player)

    def generate_output(self, output_directory: str):
        generate_output(self, output_directory)

    def fill_slot_data(self) -> dict:
        ret = {
            "death_link": self.options.death_link.value,
        }

        return ret

class UrbzItem(Item):
    game = "Urbz Sims in the City"
    type = None

    def __init__(self, name, player: int = None):
        item_data = item_table[name]
        super(UrbzItem, self).__init__(
            name,
            item_data.classification,
            item_data.id, player
        )
