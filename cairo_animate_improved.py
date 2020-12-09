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

def janim_to_cairo(v):
    x, y = v

    x_new = 120 * (x + W/2)
    y_new = 120 * (-y + H/2)

    return x_new, y_new



def draw_frame(i):
    camera = Camera()
    surface = camera.get_cairo_surface()
    context = camera.get_cairo_context()

    # Set background color
    context.set_source_rgba(0, 0, 0, 1)
    context.paint()
    context.save()
    context.restore()

    context.set_line_width(60)
    context.set_source_rgba(1, 1, 1, 1)

    sky = CelestialSphere()

    for star in sky.stars:
        x = (-(star.ra + i/720) * 16/tau) % 16 - 8
        y = star.dec * 16/tau

        x, y = janim_to_cairo((x, y))
        r = 3 * star.magnitude_to_radius()
        context.arc(x, y, r, 0, tau)
        context.fill()

    return surface

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
