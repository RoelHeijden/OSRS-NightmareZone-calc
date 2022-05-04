
class Max_hit:

    def __init__(self, attacker, hit_chance):
        self.attacker = attacker
        self.hit_chance = hit_chance


    def calc_max_hit(self):
        if self.attacker.attack_style == "Magic":
            hit = self.attacker.spell_max_hit * self.attacker.str_bonus
        else:
            a = self.hit_chance.effective_level(self.attacker.str_level, self.attacker.str_prayer,
                                                self.attacker.str_stance_bonus, self.attacker.str_void_bonus)
            b = self.attacker.str_bonus
            hit = 0.5 + a * (b + 64) / 640
        hit = int(hit)
        hit *= self.attacker.str_item_bonus
        hit = int(hit)
        hit *= self.attacker.str_special_bonus
        hit = int(hit)
        return hit
