"OSRS Calcs"

calc_dps = True
calc_nmz = False

# Attacker
str_level         = 308
str_bonus         = 1.00      # Strength, ranged strength or magic damage
str_stance_bonus  = 0         # +3 for accurate/aggressive / +1 for controlled
str_prayer        = 1.00
str_void_bonus    = 1.00
str_item_bonus    = 1.00     # Salve amulet / Slayer helm
str_special_bonus = 1.00     # Tome of fire / special attacks

attack_style      = "Magic"  # Stab/Slash/Crush/Magic/Ranged
atk_speed         = 5        # amount of ticks
spell_max_hit     = 30       # magic base max hit

atk_level         = 150
atk_bonus         = 150
atk_stance_bonus  = 0        # +3 for accurate / +1 for controlled
atk_prayer        = 1.00
atk_void_bonus    = 1.00
atk_item_bonus    = 1.00     # Salve amulet / Slayer helm
atk_special_bonus = 1.00     # Smoke staff / special attacks


# defender
is_a_player       = True
def_level         = 91
mage_level        = 101
def_stance_bonus  = 0        # +3 for defensive / +1 for controlled
def_bonus         = 141
def_prayer        = 1.25
mage_prayer       = 1.00


# nmz
min_bosses = 5
i_wont_attack = [
    # "Damis",
]
bosses_selected = [
    "Trapped Soul",
    "Corsair Traitor",
    "Sand Snake",
    "Count Draynor",
    "King Roald",
    "Khazard warlord",
    "Black Knight Titan",
    "Tree spirit",
    "The Kendal",
    "Treus Dayth",
    "Agrith-Naar",
    "Skeleton Hellhound",
    "Dad",
    "Arrg",
    "Black demon",
    "Jungle Demon",
    "Fareed",
    "Dessous",
    "Damis",
    "Kamil",

    # "Witch's experiment",
    # "Nazastarool",

    # "Evil Chicken",
    # "Karamel",
    # "Gelatinnoth Mother",
    # "Dessourt",
    # "Agrith-Na-Na",
    # "Flambeed",
    # "Culinaromancer",
    # "Elvarg",
    # "Corrupt Lizardman",
    # "Moss Guardian",
    # "Tanglefoot",
    # "Me",
    # "Slagilith",
    # "Dagannoth mother",
    # "Ice Troll King",
    # "Bouncer",
    # "Giant Roc",
    # "Glod",
    # "Nezikchened",
    # "Chronozon",
    # "Giant scarab",
    # "The Everlasting",
    # "Barrelchest",
    # "Elven traitor",
    # "The Untouchable",
    # "Essyllt",
    # "The Inadequacy",
]


from DPS import DPS
from NMZ import NMZ
from Attacker import Attacker
from Defender import Defender

def main():
    attacker = Attacker(spell_max_hit, atk_speed, attack_style, str_level, str_bonus, atk_level, atk_bonus,
                        str_stance_bonus, str_prayer, str_void_bonus, str_item_bonus, str_special_bonus,
                        atk_stance_bonus, atk_prayer, atk_void_bonus, atk_item_bonus, atk_special_bonus)

    defender = Defender(def_level, def_bonus, mage_level, def_stance_bonus, def_prayer, mage_prayer,
                        is_a_player)

    if calc_dps:
        dps_calc = DPS(attacker, defender)
        dps, hit_chance, max_hit = dps_calc.calc_dps()
        print("Chance to hit:", hit_chance)
        print("Maximum hit:  ", max_hit)
        print("DPS:          ", dps)
        print("Dmg/Hour:     ", round(dps * 3600))
        # print("Exp/Hour:     ", round(40 * 1200 + dps * 3600 * 2 * 9))
        # print("Exp/Cast:     ", round(40 + dps * 8 * 2 * 3))

    if calc_nmz:
        nmz = NMZ(attacker, bosses_selected, i_wont_attack)
        nmz.optimal_points(min_bosses)
        # nmz.optimal_dps()


main()
