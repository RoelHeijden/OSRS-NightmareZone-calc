
class Hit_chance:

    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender


    def hit_chance(self):
        A, B = self.relevant_effective_levels()
        atk_roll = self.max_roll(A, self.attacker.atk_bonus, self.attacker.atk_item_bonus,
                                    self.attacker.atk_special_bonus)
        def_roll = self.max_roll(B, self.defender.def_bonus, 1.00, 1.00)

        if atk_roll > def_roll:
            return 1 - (def_roll + 2) / (2 * (atk_roll + 1))
        else:
            return atk_roll / (2 * (def_roll + 1))


    def max_roll(self, effective_level, equipment_bonus, item_bonus, special_bonus):
        roll = effective_level * (equipment_bonus + 64)
        roll *= item_bonus
        roll = int(roll)
        roll *= special_bonus
        roll = int(roll)
        return roll


    def relevant_effective_levels(self):
        effective_atk = self.effective_level(self.attacker.atk_level, self.attacker.atk_prayer,
                                             self.attacker.atk_stance_bonus, self.attacker.atk_void_bonus)
        effective_def = self.effective_level(self.defender.def_level, self.defender.def_prayer,
                                             self.defender.def_stance_bonus, 1.00)
        effective_mage = self.effective_level(self.defender.mage_level, self.defender.mage_prayer, 0, 1.00)
        a = effective_atk
        b = None

        if not self.attacker.attack_style == "Magic":
            b = effective_def
        if self.attacker.attack_style == "Magic" and not self.defender.is_a_player:
            b = effective_mage
        if self.attacker.attack_style == "Magic" and self.defender.is_a_player:
            b = int(0.3*effective_def)+int(0.7*effective_mage)
        return a, b


    def effective_level(self, level, prayer_bonus, stance_bonus, void_bonus):
        e = 0
        e += level*prayer_bonus
        e = int(e)
        e += stance_bonus
        e += 8
        e *= void_bonus
        e = int(e)
        return e




