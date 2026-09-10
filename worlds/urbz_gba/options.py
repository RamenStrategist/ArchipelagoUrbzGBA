from dataclasses import dataclass

from Options import (Choice, DeathLink, DefaultOnToggle, OptionSet, NamedRange, Range, Toggle, FreeText,
                     PerGameCommonOptions, OptionGroup, StartInventory, OptionList)

from .data import rom_addresses


class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.
    Parade is default experience
    Miniopolis will take the longest, requiring Glasstown access and Rep 5 for each group in order to be go mode
    Each individual group has same requirements as miniopolis but only for one group of your choosing.

    - Parade(Default): Finish the game's original story and witness the parade
    - Miniopolis Takeover: Complete all Rep Goals for each Rep Group
    - Streeties: Complete all Rep Goals for Streeties
    - Richies: Complete all Rep Goals for Richies
    - Artsies: Complete all Rep Goals for Artsies
    - Nerdies: Complete all Rep Goals for Nerdies
    """
    display_name = "Goal"
    default = 0
    option_parade = 0
    option_miniopolis = 1
    option_streeties = 2
    option_richies = 3
    option_artsies = 4
    option_nerdies = 5

class UrbzDeathLink(DeathLink):
    __doc__ = DeathLink.__doc__ + "\n\n    Hunger reduced to 0 sends a deathlink, and receiving causes a pass out from hunger."

@dataclass
class UrbzOptions(PerGameCommonOptions):
    goal: Goal
    death_link: UrbzDeathLink
