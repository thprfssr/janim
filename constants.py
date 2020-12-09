from vector import *

# Cardinal directions and their useful abbreviations
UP = Vector(0, 1)
DN = Vector(0, -1)
LT = Vector(-1, 0)
RT = Vector(1, 0)
DOWN = DN
RIGHT = RT
LEFT = LT

# Composite directions and their useful abbreviations
UL = (UP + LT).normalize()
UR = (UP + RT).normalize()
DL = (DN + LT).normalize()
DR = (DN + RT).normalize()
UPLEFT = UL
UPRIGHT = UR
DOWNLEFT = DL
DOWNRIGHT = DR

# Zero vector
ZERO = Vector()
ORIGIN = Vector()
O = Vector()
