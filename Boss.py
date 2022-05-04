
class Boss:

    def __init__(self, name, points, hp, a, b=1, c=0, d=0, e=0, f=0, g=0):

        self.name = name
        self.points = points

        self.hp = hp
        self.def_level = a
        self.mage_level = b

        self.stab_def_bonus = c
        self.slash_def_bonus = d
        self.crush_def_bonus = e
        self.mage_def_bonus = f
        self.range_def_bonus = g


    # Points facts
    # 1. Base points is an exponential formula based on combat level.
    # 2. Multiplier is a linear formula based on Base points.
    # 3. Only the Song of the elves boss is an exception to 1.
    # 4. (Only?) the Dream mentor bosses are an exception to 2.

