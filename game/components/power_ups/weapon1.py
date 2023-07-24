from game.components.power_ups.power_up import PowerUp

from game.utils.constants import WEAPON, WEAPON_TYPE

class Weapon_1(PowerUp):
    def __init__(self):
        super().__init__(WEAPON, WEAPON_TYPE)