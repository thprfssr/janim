from camera import *
from constants import *
from janim import *
from vector import *

from math import tau, ceil, floor

DEFAULT_THICKNESS = 5


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

class MultiLine(Element):
    def __init__(self, *points,
            thickness = DEFAULT_THICKNESS,
            ):
        self.points = points
        self.thickness = thickness

    def draw(self, context):
        context.set_source_rgba(1, 1, 1, 1)
        p = Camera().janim_to_cairo_coordinates(self.points[0])
        context.move_to(p.x, p.y)
        for i in range(1, len(self.points)):
            p = Camera().janim_to_cairo_coordinates(self.points[i])
            context.line_to(p.x, p.y)

        context.set_line_width(self.thickness)
        context.stroke()

class Line(MultiLine):
    def __init__(self, start, end, thickness = DEFAULT_THICKNESS):
        self.start = start
        self.end = end
        super().__init__(start, end, thickness = thickness)


class NumberLine(Line):
    def __init__(self, start, end,
            thickness = DEFAULT_THICKNESS,
            tick_height = 0.3,
            unit_size = 1):
        super().__init__(start, end, thickness)
        self.unit_size = unit_size
        self.tick_height = tick_height

    def get_direction_vector(self):
        v = self.end - self.start
        return v.normalize()

    def draw(self, context):
        v = self.get_direction_vector()
        s_min = self.start * v
        s_max = self.end * v
        main_line = Line(self.start, self.end)
        main_line.draw(context)
        h = self.tick_height
        w = v.rotate(tau/4)
        for i in range(ceil(s_min), floor(s_max) + 1):
            tick_center = i * v
            tick_mark = Line(-w * h/2 + tick_center, w * h/2 + tick_center)
            tick_mark.draw(context)
