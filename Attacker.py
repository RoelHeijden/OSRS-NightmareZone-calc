
class Attacker:

    def __init__(self, spell_max_hit, a, b, c, d, e, f, g=0, h=1.00, i=1.00, j=1.00,
                 k=1.00, l=0, m=1.00, n=1.00, o=1.00, p=1.00):

        self.spell_max_hit = spell_max_hit
        self.atk_speed = a
        self.attack_style = b

        self.str_level = c
        self.str_bonus = d

        self.atk_level = e
        self.atk_bonus = f

        self.str_stance_bonus = g
        self.str_prayer = h
        self.str_void_bonus = i
        self.str_item_bonus = j
        self.str_special_bonus = k

        self.atk_stance_bonus = l
        self.atk_prayer = m
        self.atk_void_bonus = n
        self.atk_item_bonus = o
        self.atk_special_bonus = p

