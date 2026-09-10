from BaseClasses import ItemClassification

class ItemData:
    def __init__(self, item_id, classification, groups):
        self.groups = groups
        self.classification = classification
        self.id = None if item_id is None else item_id + 172000000

item_table = {
    "Chapter 1.1: Squeegee Clean": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.1: Befriend Kris (Rel 30)": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.1: Give Kris Squeegee 'n Bucket": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.2: Take a Shower": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.2: Take a Nap": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.2: Eat Something (Vending Machine)": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.3: Move Bed to the Suite": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.3: Repair the Television": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.3: Repair Two Fountains": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.4: Mechanical Skill - Law Office Workbench": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.4: Pick Lily's Lock": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.4: Law Office Key": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.5: Befriend Det. Dan (Rel 30)": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.6: Play Hoopz": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.6: Rent money (150)": ItemData(None, ItemClassification.progression, []),
    "Chapter 1.6: Buy a House": ItemData(None, ItemClassification.progression, []),


}