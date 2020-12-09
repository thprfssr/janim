from constants import *
from janim import *
from vector import *

from math import tau



class Circle(Element):
    def __init__(self, radius = 1, center = ORIGIN):
        self.center = center
        self.radius = radius

    def draw(self, context):
        x = self.center.x
        y = self.center.y
        r = self.radius
        context.set_source_rgba(1, 1, 1, 1)
        context.arc(x, y, r, 0, tau)
        context.fill()
