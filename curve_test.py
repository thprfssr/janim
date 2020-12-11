from camera import *
from geometry import *
from vector import *

import numpy as np

camera = Camera()
surface = camera.get_cairo_surface()
context = camera.get_cairo_context()

#context.set_source_rgba(1, 1, 1, 1)


#X = np.linspace(-7, 7, 1000)
#Y = np.sin(X)
#V = [Vector(X[i], Y[i]) for i in range(len(X))]
#m = MultiLine(*V)
#m.draw(context)

X_AXIS = NumberLine(7 * LT, 7 * RT)
Y_AXIS = NumberLine(4 * UP, 4 * DN)
X_AXIS.draw(context)
Y_AXIS.draw(context)

parameter = np.linspace(-7, 7, 10000)
curve = Curve(parameter, lambda t: Vector(t, t - t**3/6 + t**5/120))
curve.draw(context)

surface.write_to_png('curve.png')
