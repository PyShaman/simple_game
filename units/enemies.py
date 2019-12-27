import json
import random


class Enemy:
    def __init__(self):
        self.hp = 10
        self.attack = 1
        self.exp = 5
        self.reward = 5
        self.prefix = [("small", 1), ("medium", 5), ("large", 10)]
        self.suffix = [("flesh", 1), ("clay", 2), ("iron", 5), ("steel", 10)]
        self.unit = [("rat", 5), ("mantis", 7), ("scaven", 13), ("golem", 20), ("zombie", 25), ("lich", 38), ("moloch", 50)]

    @staticmethod    
    def enemy_stats():
        with open("stats.json") as stats:
            return stats


    def enemy_unit(self):
        random_prefix = self.prefix[random.randint(0,2)]
        random_suffix = self.suffix[random.randint(0,3)]
        random_unit = self.unit[random.randint(0,6)]
        return f"You encountered {random_prefix[0]} {random_suffix[0]} {random_unit[0]} with {self.hp*random_prefix[1]*random_suffix[1]*random_unit[1]}HP and {self.attack+random_prefix[1]+random_suffix[1]+random_unit[1]}ATT"
