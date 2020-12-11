import cairo

from camera import *
from geometry import *
from vector import *




camera = Camera()
surface = camera.get_cairo_surface()
context = camera.get_cairo_context()

"""
context.set_source_rgba(1, 1, 1, 1)
start = camera.janim_to_cairo_coordinates(Vector(1, 2))
end = camera.janim_to_cairo_coordinates(Vector(3, 4))
context.move_to(start.x, start.y)
context.line_to(end.x, end.y)

context.set_line_width(5)
context.stroke()
"""

start = camera.janim_to_cairo_coordinates(Vector(1, 2))
end = camera.janim_to_cairo_coordinates(Vector(5, 3))
m = Line(start, end)
m.draw(context)

camera.write_to_png('lines.png')
