from typing import Dict

regions: Dict[str, str] = {}

class Districts:
    urbania = "Urbania"
    simQ = "Sim Quarter"
    gTown = "Glasstown"
    bayou = "Bayou"
    pIsland = "Paradise Island"


class Missions:
    CH1 = "High Above the World"
    C1G1 = f"{CH1} - Slave to the Grind"
    C1G2 = f"{CH1} - Get Cleaned Up"
    C1G3 = f"{CH1} - Help Kris Thistle"
    C1G4 = f"{CH1} - Find the Key"
    C1G5 = f"{CH1} - Get Out of Jail"
    C1G6 = f"{CH1} - Find a Place to Live"
    CH2 = "Urbania"
    C2G1 = f"{CH2} - Work Study"
    C2G2 = f"{CH2} - Gotta Finish the Riff"
    C2G3 = f"{CH2} - Race for Glory"
    C2G4 = f"{CH2} - Salesmanship"
    C2G5 = f"{CH2} - Club Xizzle"
    C2G6 = f"{CH2} - Road to Sim Quarter"
    CH3 = "Viva la Sim Quarter"
    C3G1 = f"{CH3} - Mission for the Mann"
    C3G2 = f"{CH3} - Daddy Bigbucks and the Xizzle Factory"
    C3G3 = f"{CH3} - None Shall Pass"
    C3G4 = f"{CH3} - Get on the List"
    C3G5 = f"{CH3} - High Society"
    C3G6 = f"{CH3} - The Ballad of Pepper Pete"
    CH4 = "The Bayou and Beyond"
    C4G1 = f"{CH4} - The Greatest Fear"
    C4G2 = f"{CH4} - Fiddle with the Red Man"
    C4G3 = f"{CH4} - Bye Bye Bayou"
    C4G4 = f"{CH4} - Running from the Law"
    C4G5 = f"{CH4} - Carnivale!"
    C4G6 = f"{CH4} - The Bigbucks Players"
    C5 = "Time After Time"
    C5G1 = f"{CH5} - Reality Show"
    C5G2 = f"{CH5} - Back to the Drawing Board"
    C5G3 = f"{CH5} - Interview with a Cajun Vampire"
    C5G4 = f"{CH5} - Captured"
    C5G5 = f"{CH5} - Atlantis Premiere Party"
    C5G6 = f"{CH5} - Back in Time"


region_exits: Dict[str, list[str]] = {
    Districts.urbania: [Districts.simQ, Districts.gTown],
    Districts.simQ: [Districts.urbania, Districts.gTown, Districts.bayou, Districts.pIsland],
    Districts.gTown: [Districts.urbania, Districts.simQ, Districts.bayou, Districts.pIsland],
    Districts.bayou: [Districts.simQ, Districts.gTown, Districts.pIsland],
    Districts.pIsland: [Districts.simQ, Districts.gTown, Districts.bayou],

}