from Hit_chance import Hit_chance
from Max_hit import Max_hit

class DPS:

    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender
        self.hit_chance = Hit_chance(attacker, defender)
        self.max_hit = Max_hit(attacker, self.hit_chance)


    def calc_dps(self):
        chance = self.hit_chance.hit_chance()
        max = self.max_hit.calc_max_hit()
        dps = (((chance * max) / self.attacker.atk_speed) / 0.6) / 2
        return dps, chance, max

