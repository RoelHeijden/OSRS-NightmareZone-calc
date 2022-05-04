from DPS import DPS
from Defender import Defender
from Boss import Boss
from FindOptimal import FindOptimal
import math


class NMZ:

    # check dream mentor multiplier
    # collect all bosses points
    # make heuristics
    def __init__(self, attacker, bosses_selected, ignore_list):
        self.attacker = attacker
        self.bosses_selected = bosses_selected
        self.ignore_list = ignore_list
        self.bosses = self.init_bosses()
        self.groups = self.init_groups()
        self.boss_forms = self.init_forms()
        self.boss_data = self.calc_boss_data()


    def init_bosses(self):
        bosses = {
                                                     #basepoints/hp/def/mage/Stab/Slash/Crush/Magic/Ranged
        "Trapped Soul"        : Boss("Trapped Soul",         412, 100, 20, 1, 0, 0, 0, 0, 0),
        "Corsair Traitor"     : Boss("Corsair Traitor",      412, 160, 80, 90, 0, 0, 0, 0, 0),
        "Sand Snake"          : Boss("Sand Snake",           947, 180, 20, 1, 0, 0, 0, 0, 0),
        "Count Draynor"       : Boss("Count Draynor",       1276, 210, 30, 1, 2, 1, 3, 0, 0),
        "King Roald"          : Boss("King Roald",          1441, 150, 30, 1, 0, 0, 0, 0, 0),
        "Khazard warlord"     : Boss("Khazard warlord",     1482, 255, 80, 1, 0, 0, 0, 0, 0),
        "Treus Dayth"         : Boss("Treus Dayth",         1523, 240, 100, 1, 5, 5, 5, -5, 5),
        "Agrith-Naar"         : Boss("Agrith-Naar",         1564, 209, 82, 220, 0, 0, 0, 0, 0),
        "Skeleton Hellhound"  : Boss("Skeleton Hellhound",  1606, 132, 100, 1, 0, 0, 0, 0, 0),
        "Tree spirit"         : Boss("Tree spirit",         1606, 187, 80, 1, 0, 0, 0, 0, 0),
        "Dad"                 : Boss("Dad",                 1647, 240, 50, 0, 25, 25, 40, 200, 200),
        "The Kendal"          : Boss("The Kendal",          1812, 150, 60, 0, 10, 10, 10, -10, 20),
        "Arrg"                : Boss("Arrg",                1812, 255, 40, 0, 35, 60, 35, 200, 200),
        "Dessous"             : Boss("Dessous",             1935, 255, 99, 1, 10, 150, 150, 0, 0),
        "Damis1"              : Boss("Damis1",                 0, 198, 90, 1, 60, 60, 60, 60, 60),
        "Damis2"              : Boss("Damis2",              3005, 255, 160, 1, 100, 100, 100, 80, 120),
        "Kamil"               : Boss("Kamil",               3047, 255, 135, 1, 35, 60, 35, 0, 0),
        "Black demon"         : Boss("Black demon",         3499, 255, 152, 1, 0, 0, 0, -10, 0),
        "Fareed"              : Boss("Fareed",              3664, 255, 135, 1, 100, 100, 100, 0, 0),
        "Jungle Demon"        : Boss("Jungle Demon",        4363, 255, 170, 340, 0, 50, 0, 50, 0),
        "Black Knight Titan"  : Boss("Black Knight Titan",  1777, 255, 91, 1, 18, 27, 18, 1000, 1000),

        # "Witch's experiment1" : Boss("Witch's experiment1", 0, 63, 19, 1, 0, 0, 0, 0, 0),
        # "Witch's experiment2" : Boss("Witch's experiment2", 0, 93, 29, 1, 0, 0, 0, 0, 0),
        # "Witch's experiment3" : Boss("Witch's experiment3", 0, 103, 39, 1, 0, 0, 0, 0, 0),
        # "Witch's experiment4" : Boss("Witch's experiment4", 0, 113, 49, 1, 0, 0, 0, 0, 0),
        # "Nazastarool1"        : Boss("Nazastarool1",        0, 154, 80, 0, 0, 0, 0, 0, 0),
        # "Nazastarool2"        : Boss("Nazastarool2",        0, 180, 58, 0, 5, 5, 5, 5, 5),
        # "Nazastarool3"        : Boss("Nazastarool3",        0, 176, 80, 0, 0, 0, 0, 0, 0),

        # "Elvarg"              : Boss("Elvarg",              0, 240, 70, 210, 20, 40, 40, 30, 20),
        # "Corrupt Lizardman"   : Boss("Corrupt Lizardman",   0, 150, 38, 1, -10, 25, 0, 0, 0),
        # "Moss Guardian"       : Boss("Moss Guardian",       0, 240, 60, 1, 0, 0, 0, 0, 0),
        # "Karamel"             : Boss("Karamel",             0, 255, 100, 1, 150, 150, 150, 150, 150),
        # "Tanglefoot"          : Boss("Tanglefoot",          0, 204, 91, 1, 0, 0, 0, 0, 0),
        # "Me"                  : Boss("Me",                  0, 135, 74, 1, 0, 0, 0, 0, 0),
        # "Slagilith"           : Boss("Slagilith",           0, 150, 75, 1, 50, 50, 5, 5, 50),
        # "Dagannoth mother"    : Boss("Dagannoth mother",    0, 240, 81, 1, 150, 150, 150, 50, 50),
        # "Gelatinnoth Mother"  : Boss("Gelatinnoth Mother",  0, 240, 81, 1, 150, 150, 150, 50, 50),
        # "Culinaromancer"      : Boss("Culinaromancer",      0, 255, 10, 1, -10, -10, -10, -10, -10),
        # "Ice Troll King"      : Boss("Ice Troll King",      0, 255, 80, 1, 45, 45, 45, 2000, 2000),
        # "Dessourt"            : Boss("Dessourt",            0, 255, 99, 1, 10, 150, 150, 0, 0),
        # "Agrith-Na-Na"        : Boss("Agrith-Na-Na",        0, 255, 82, 200, 100, 100, 100, 100, 100),
        # "Flambeed"            : Boss("Flambeed",            0, 255, 75, 1, 50, 50, 5, 5, 50),
        # "Bouncer"             : Boss("Bouncer",             0, 232, 120, 1, 0, 0, 0, 0, 0),
        # "Giant Roc"           : Boss("Giant Roc",           0, 255, 100, 1, 0, 0, 0, 150, 0),
        # "Glod"                : Boss("Glod",                0, 255, 110, 1, 105, 110, 130, 125, 100),
        # "Evil Chicken"        : Boss("Evil Chicken",        0, 240, 126, 400, 0, 0, 0, 0, 0),
        # "Nezikchened"         : Boss("Nezikchened",         0, 150, 167, 320, 0, 0, 0, 0, 0),
        # "Chronozon"           : Boss("Chronozon",           0, 120, 173, 1, 0, 0, 0, 0, 0),
        # "Giant scarab"        : Boss("Giant scarab",        0, 255, 169, 1, 70, 99, 99, 159, 149),
        # "The Everlasting"     : Boss("The Everlasting",     0, 255, 120, 1, 0, 0, 0, 0, 0),
        # "Barrelchest"         : Boss("Barrelchest",         0, 255, 140, 162, 0, 0, 0, 0, 0),
        # "Elven traitor"       : Boss("Elven traitor",       0, 300, 102, 153, 80, 80, 80, 260, 180),
        # "The Untouchable"     : Boss("The Untouchable",     0, 180, 434, 1, 0, 0, 0, 0, 0),
        # "Essyllt"             : Boss("Essyllt",             0, 320, 104, 104, 40, 40, 20, 30, 120),
        # "The Inadequacy"      : Boss("The Inadequacy",      0, 255, 240, 1, 0, 0, 0, 0, 0)
        }
        return bosses


    def init_groups(self):
        groups = {
        "Fareed"  : ["Dessous", "Damis" , "Kamil"],
        "Dessous" : ["Fareed" , "Damis" , "Kamil"],
        "Damis"   : ["Dessous", "Fareed", "Kamil"],
        "Kamil"   : ["Dessous", "Damis" ,"Fareed"],

        "Evil Chicken"       : ["Karamel", "Gelatinnoth Mother", "Dessourt",
                                "Agrith-Na-Na", "Flambeed", "Culinaromancer"],
        "Karamel"            : ["Evil Chicken", "Gelatinnoth Mother", "Dessourt",
                                "Agrith-Na-Na", "Flambeed", "Culinaromancer"],
        "Gelatinnoth Mother" : ["Karamel", "Evil Chicken", "Dessourt",
                                "Agrith-Na-Na", "Flambeed", "Culinaromancer"],
        "Dessourt"           : ["Karamel", "Evil Chicken", "Gelatinnoth Mother",
                                "Agrith-Na-Na", "Flambeed", "Culinaromancer"],
        "Agrith-Na-Na"       : ["Karamel", "Evil Chicken", "Gelatinnoth Mother",
                                "Dessourt", "Flambeed", "Culinaromancer"],
        "Flambeed"           : ["Karamel", "Evil Chicken", "Gelatinnoth Mother",
                                "Dessourt", "Agrith-Na-Na", "Culinaromancer"],
        "Culinaromancer"     : ["Karamel", "Evil Chicken", "Gelatinnoth Mother",
                                "Dessourt", "Agrith-Na-Na", "Flambeed"],
        }
        return groups


    def init_forms(self):
        boss_forms = {
        "Trapped Soul"       : ["Trapped Soul"],
        "Corsair Traitor"    : ["Corsair Traitor"],
        "Sand Snake"         : ["Sand Snake"],
        "Count Draynor"      : ["Count Draynor"],
        "King Roald"         : ["King Roald"],
        "Khazard warlord"    : ["Khazard warlord"],
        "Tree spirit"        : ["Tree spirit"],
        "The Kendal"         : ["The Kendal"],
        "Treus Dayth"        : ["Treus Dayth"],
        "Agrith-Naar"        : ["Agrith-Naar"],
        "Skeleton Hellhound" : ["Skeleton Hellhound"],
        "Dad"                : ["Dad"],
        "Arrg"               : ["Arrg"],
        "Black demon"        : ["Black demon"],
        "Jungle Demon"       : ["Jungle Demon"],
        "Fareed"             : ["Fareed"],
        "Dessous"            : ["Dessous"],
        "Damis"              : ["Damis1", "Damis2"],
        "Kamil"              : ["Kamil"],
        "Witch's experiment" : ["Witch's experiment1", "Witch's experiment2",
                                "Witch's experiment3", "Witch's experiment4"],
        "Black Knight Titan" : ["Black Knight Titan"],
        "Nazastarool"        : ["Nazastarool1", "Nazastarool2", "Nazastarool3"],
        "Elvarg"             : ["Elvarg"],
        "Corrupt Lizardman"  : ["Corrupt Lizardman"],
        "Moss Guardian"      : ["Moss Guardian"],
        "Karamel"            : ["Karamel"],
        "Tanglefoot"         : ["Tanglefoot"],
        "Me"                 : ["Me"],
        "Slagilith"          : ["Slagilith"],
        "Dagannoth mother"   : ["Dagannoth mother"],
        "Gelatinnoth Mother" : ["Gelatinnoth Mother"],
        "Culinaromancer"     : ["Culinaromancer"],
        "Ice Troll King"     : ["Ice Troll King"],
        "Dessourt"           : ["Dessourt"],
        "Agrith-Na-Na"       : ["Agrith-Na-Na"],
        "Flambeed"           : ["Flambeed"],
        "Bouncer"            : ["Bouncer"],
        "Giant Roc"          : ["Giant Roc"],
        "Glod"               : ["Glod"],
        "Evil Chicken"       : ["Evil Chicken"],
        "Nezikchened"        : ["Nezikchened"],
        "Chronozon"          : ["Chronozon"],
        "Giant scarab"       : ["Giant scarab"],
        "The Everlasting"    : ["The Everlasting"],
        "Barrelchest"        : ["Barrelchest"],
        "Elven traitor"      : ["Elven traitor"],
        "The Untouchable"    : ["The Untouchable"],
        "Essyllt"            : ["Essyllt"],
        "The Inadequacy"     : ["The Inadequacy"],
        }
        return boss_forms


    def calc_boss_data(self):
        boss_data = {}
        for name in self.bosses:
            boss = self.bosses.get(name)
            def_bonus = None
            style = self.attacker.attack_style
            if style == "Magic":
                def_bonus = boss.mage_def_bonus
            if style == "Ranged":
                def_bonus = boss.range_def_bonus
            if style == "Stab":
                def_bonus = boss.stab_def_bonus
            if style == "Crush":
                def_bonus = boss.crush_def_bonus
            if style == "Slash":
                def_bonus = boss.slash_def_bonus

            defender = Defender(boss.def_level, def_bonus, boss.mage_level)
            dps_calc = DPS(self.attacker, defender)
            dps, _, _ = dps_calc.calc_dps()
            time_to_kill = boss.hp / dps
            points_per_sec = boss.points / time_to_kill

            boss_data[name] = (points_per_sec, dps, boss, time_to_kill)
        return boss_data


    def get_base_points_1(self, points):
        a = - 4364 / 647
        b = math.sqrt(647 * points + 4761124)
        c = 2182
        return round(a * (b - c))


    def get_base_points_2(self, multiplier):
        prev_base_points = 0
        for boss_name in self.bosses_selected:
            for form in self.boss_forms.get(boss_name):
                prev_base_points += self.bosses.get(form).points

        total_base_points = (multiplier - 1) / 0.000033973070224594
        return round(total_base_points - prev_base_points)

    def get_base_points_3(self, combat_lvl):
        a = 683/17200
        b = 361/688
        c = -470041/8600
        return a*math.pow(combat_lvl, 2) + b*combat_lvl + c


    def calc_multiplier(self, used_bosses):
        points_included = 0
        for boss_name in used_bosses:
            for form in self.boss_forms.get(boss_name):
                points_included += self.bosses.get(form).points

        return 3.3973070224594E-5 * points_included + 1


    def points_per_hour(self, bosses):
        multiplier = self.calc_multiplier(bosses)
        total_ttk = 0
        total_points = 0
        for boss_name in bosses:
            if boss_name in self.ignore_list:
                continue
            for form in self.boss_forms.get(boss_name):
                _, _, boss, ttk = self.boss_data.get(form)
                total_ttk += ttk
                total_points += boss.points
        return (3600 / total_ttk) * total_points * multiplier


    def show_data(self, bosses_selected, sort_on=0):
        multiplier = self.calc_multiplier(bosses_selected)
        points_per_hour = self.points_per_hour(bosses_selected)
        dmg_per_hour = self.dmg_per_hour(bosses_selected)
        data = self.boss_data_sort(bosses_selected, sort_on)

        for pps, dps, boss_name, ttk in data:
            if boss_name not in self.ignore_list:
                if sort_on == 0:
                    print(round(pps*multiplier), " - ", boss_name)
                if sort_on == 1:
                    print(round(dps, 4), " - ", boss_name)

        print()
        for pps, dps, boss_name, ttk in data:
            if boss_name in self.ignore_list:
                print("Ignored", " - ", boss_name)

        print()
        if sort_on == 0:
            print("Points multiplier:", round(multiplier, 6))
            print("Points per hour  :", round(points_per_hour))
            print("Per Overload (1) :", round(points_per_hour/12))
        if sort_on == 1:
            print("Damage per hour  :", round(dmg_per_hour))
            print("Exp per hour  :", round(dmg_per_hour*4))

        print()
        print("-----------------------------------------------")


    def boss_data_sort(self, bosses, index=0):
        boss_data_list = []
        for boss_name in bosses:
            total_ttk = 0
            avg_pps = 0
            avg_dps = 0
            for form in self.boss_forms.get(boss_name):
                pps, dps, _, ttk = self.boss_data.get(form)
                total_ttk += ttk
                avg_pps += pps * ttk
                avg_dps += dps * ttk
            avg_pps = avg_pps / total_ttk
            avg_dps = avg_dps / total_ttk
            boss_data_list.append((avg_pps, avg_dps, boss_name, total_ttk))

        boss_data_list.sort(reverse=True, key=lambda x: x[index])
        return boss_data_list


    def quests_selected(self, bosses):
        counted = []
        count = 0
        for boss in bosses:
            if boss not in counted:
                count += 1
            if boss in self.groups:
                counted += self.groups.get(boss)
        return count


    def optimal_points(self, min_bosses=5):
        bosses = self.bosses_selected.copy()
        bosses.sort()
        amount_selected = self.quests_selected(bosses)
        search = FindOptimal(self.groups, [], self.points_per_hour)

        optimal_bosses = search.find_optimal(bosses, {}, min_bosses, amount_selected)
        self.show_data(optimal_bosses[1])
        print("Combinations explored:", search.count)


    def optimal_dps(self, min_bosses=5):
        bosses = self.bosses_selected.copy()
        bosses.sort()
        amount_selected = self.quests_selected(bosses)
        search = FindOptimal(self.groups, [], self.dmg_per_hour)

        optimal_bosses = search.find_optimal(bosses, {}, min_bosses, amount_selected)
        self.show_data(optimal_bosses[1], sort_on=1)
        print("Combinations explored:", search.count)


    def dmg_per_hour(self, bosses):
        total_hp = 0
        total_ttk = 0
        for boss_name in bosses:
            if boss_name in self.ignore_list:
                continue
            for form in self.boss_forms.get(boss_name):
                _, _, boss, ttk = self.boss_data.get(form)
                total_ttk += ttk
                total_hp += boss.hp

        avg_dps = total_hp / total_ttk
        return avg_dps*3600

