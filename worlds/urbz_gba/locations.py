from BaseClasses import Location
from .data import rom_addresses

def always_on(world, player):
    return True

class LocationData:
    def __init__(self, region, name, original_item, rom_address=None, ram_address=None, event=False, type="Item",
                 inclusion=always_on, level=None, level_address=None):
        self.region = region
        self.name = region if name == "" else region.split("-")[0] + " - " + name
        self.original_item = original_item
        self.rom_address = rom_address
        self.ram_address = ram_address
        self.event = event
        self.type = type
        self.inclusion = inclusion
        self.level = level
        self.address = None
        if level_address:
            self.level_address = level_address
        elif level:
            self.level_address = rom_address - 1
        else:
            self.level_address = None

class EventFlag:
    def __init__(self, flag):
        self.byte = int(flag / 8)
        self.bit = flag % 8
        self.flag = flag

location_data = [
    LocationData("Chapter 1", "Goal 1", "Squeegee Clean Intro", rom_addresses.objective_rom_addresses["C1G101"], event=True)
]