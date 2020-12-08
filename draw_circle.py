import cairo

from math import tau

from geometry import *
from read_bsc import *

W = 16
H = 9

def janim_to_cairo(v):
    x, y = v

    x_new = 120 * (x + W/2)
    y_new = 120 * (-y + H/2)

    return x_new, y_new



circle = Circle()

surface = cairo.SVGSurface('test.svg', W*120, H*120)
context = cairo.Context(surface)

# Set background color
context.set_source_rgba(0, 0, 0, 1)
context.paint()
context.save()
context.restore()

context.set_line_width(60)
context.set_source_rgba(1, 1, 1, 1)


#x, y = janim_to_cairo(circle.center)
#r = 120 * circle.radius
#context.arc(x, y, r, 0, tau)


for star in filter(lambda s: s.magnitude < 5, stars):
    x = - star.ra * 16/tau + 8
    y = star.dec * 16/tau

    x, y = janim_to_cairo((x, y))
    r = 3 * star.magnitude_to_radius()
    context.arc(x, y, r, 0, tau)
    context.fill()
