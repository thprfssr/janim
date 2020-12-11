from geometry import *
from camera import *
from vector import *

camera = Camera()
context = camera.get_cairo_context()

X_AXIS = NumberLine(7 * LT, 7 * RT)
Y_AXIS = NumberLine(4 * DN, 4 * UP)

X_AXIS.draw(context)
Y_AXIS.draw(context)

surface = camera.get_cairo_surface()
surface.write_to_png('number-line.png')
