from janim import *
from geometry import *
from vector import *
from constants import *
from astro import *

import numpy as np

'''
scene = Scene()
scene.add(NumberLine(7*LT, 7*RT))
scene.add(NumberLine(4*UP, 4*DN))

parameter = np.linspace(-7, 7, 10000)
function = lambda x: Vector(x, x - x**3/6 + x**5/120)
scene.add(Curve(parameter, function))

scene.draw()
scene.write_to_png('tet.png')
'''

scene = Scene()
sky = CelestialSphere()
scene.draw()
scene.write_to_png('sky.png')
