from BaseClasses import Location
from .data.rom_addresses import mission_rom_addresses as rom
from .items import item_table
from .regions import Missions


def always_on(world, player):
    return True

class LocationData:
    def __init__(self, region, name, original_item, rom_address=None, event=False, type="Item"):
        self.region = region
        self.name = region if name == "" else region.split("-")[0] + " - " + name
        self.original_item = original_item
        self.rom_address = rom_address
        self.event = event
        self.type = type

# Might still be needed, especially for death link
# class EventFlag:
#     def __init__(self, flag):
#         self.byte = int(flag / 8)
#         self.bit = flag % 8
#         self.flag = flag

def create_mission_locations(location_data):
    for item in item_table:
        if item_table[item].groups == "missions":
            location_data.append((
                LocationData(getattr(Missions, item_table[item].parent),
                             None,item,rom[item_table[item].id],event=True)))
