from dataclasses import dataclass
from typing import ClassVar
import random

@dataclass
class Player:
    player_name: str
    player_hp: ClassVar[int] = 50
    player_inventory: ClassVar[int] = 3

    @property
    def player_name(self) -> str:
        return self._player_name
    
    @player_name.setter
    def player_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name should be a string of characters")
        else:
            self._player_name = value
    
    
    def player_attack(self,enemy):
        """ 
        This function remove a random number of HP between 5 and 10 to the enemy
        """
        enemy.health_points = enemy.health_points - random.randint(5, 10)
        return enemy.health_points
    

    def use_potion(self):
        """
        This function adds HP points to the player if he chooose to
        """
        self.player_hp += random.randint(15, 50)
        if self.player_hp>50:
            self.player_hp = 50
        return self.player_hp

    def check_inventory(self):
            """
            Checking if the player have enough potions
            """
            if self.player_inventory > 0:
                self.player_hp = self.use_potion()
                self.player_inventory -= 1
            else:
                print("Dommage tu n’as plus de potion")

    def check_infos(self, enemy):
        """
        This function print informations about the player's pv
        (and the number of potions he has ) and the monster's pv.
        """
        print(f"{self.player_name}, il vous reste {self.player_hp} points de vie et {self.player_inventory} potion(s), le Troll a {enemy.health_points} points de vie.")

