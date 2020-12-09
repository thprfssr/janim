import cairo
import cartopy.crs as ccrs
import ffmpeg
import os
import tempfile
from math import pi, tau
from tqdm import tqdm

from astro import *
from camera import *
from constants import *
from geometry import *
from vector import *


W = 16
H = 9

def draw_frame(i):
    camera = Camera()
    context = camera.get_cairo_context()

    sky = CelestialSphere()

    for star in sky.stars:
        v = star.get_stereographic(i/720).scale(12)
        v = camera.janim_to_cairo_coordinates(v)

        r = 10 * star.magnitude_to_radius()
        circle = Circle(r, v)
        circle.draw(context)

    return camera.get_cairo_surface()

for i in tqdm(range(0, 120)):
    frame_surface = draw_frame(i)
    #f, path = tempfile.mkstemp('.png')
    #os.close(f)

    name = '/tmp/JANIM-' + str(i).zfill(12) + '.png'
    frame_surface.write_to_png(name)

(
        ffmpeg
        .input('/tmp/JANIM-*.png', pattern_type = 'glob', framerate = 60)
        .output('moi.mp4')
        .run()
)
