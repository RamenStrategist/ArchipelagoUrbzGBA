from typing import Dict

from worlds.urbz_gba import item_table


class Districts:
    urbania = "Urbania"
    simQ = "Sim Quarter"
    gTown = "Glasstown"
    bayou = "Bayou"
    pIsland = "Paradise Island"

class Missions:
    CH1 = "High Above the World"
    CH1G1 = f"{CH1} - Slave to the Grind"
    CH1G2 = f"{CH1} - Get Cleaned Up"
    CH1G3 = f"{CH1} - Help Kris Thistle"
    CH1G4 = f"{CH1} - Find the Key"
    CH1G5 = f"{CH1} - Get Out of Jail"
    CH1G6 = f"{CH1} - Find a Place to Live"
    CH2 = "Urbania"
    CH2G1 = f"{CH2} - Work Study"
    CH2G2 = f"{CH2} - Gotta Finish the Riff"
    CH2G3 = f"{CH2} - Race for Glory"
    CH2G4 = f"{CH2} - Salesmanship"
    CH2G5 = f"{CH2} - Club Xizzle"
    CH2G6 = f"{CH2} - Road to Sim Quarter"
    CH3 = "Viva la Sim Quarter"
    CH3G1 = f"{CH3} - Mission for the Mann"
    CH3G2 = f"{CH3} - Daddy Bigbucks and the Xizzle Factory"
    CH3G3 = f"{CH3} - None Shall Pass"
    CH3G4 = f"{CH3} - Get on the List"
    CH3G5 = f"{CH3} - High Society"
    CH3G6 = f"{CH3} - The Ballad of Pepper Pete"
    CH4 = "The Bayou and Beyond"
    Ch4G1 = f"{CH4} - The Greatest Fear"
    Ch4G2 = f"{CH4} - Fiddle with the Red Man"
    Ch4G3 = f"{CH4} - Bye Bye Bayou"
    Ch4G4 = f"{CH4} - Running from the Law"
    Ch4G5 = f"{CH4} - Carnivale!"
    Ch4G6 = f"{CH4} - The Bigbucks Players"
    CH5 = "Time After Time"
    Ch5G1 = f"{CH5} - Reality Show"
    Ch5G2 = f"{CH5} - Back to the Drawing Board"
    Ch5G3 = f"{CH5} - Interview with a Cajun Vampire"
    Ch5G4 = f"{CH5} - Captured"
    Ch5G5 = f"{CH5} - Atlantis Premiere Party"
    Ch5G6 = f"{CH5} - Back in Time"

region_exits: Dict[str, list[str]] = {
    Districts.urbania: [Districts.simQ, Districts.gTown],
    Districts.simQ: [Districts.urbania, Districts.gTown, Districts.bayou, Districts.pIsland],
    Districts.gTown: [Districts.urbania, Districts.simQ, Districts.bayou, Districts.pIsland],
    Districts.bayou: [Districts.simQ, Districts.gTown, Districts.pIsland],
    Districts.pIsland: [Districts.simQ, Districts.gTown, Districts.bayou],


}