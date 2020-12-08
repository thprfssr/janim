import cairo
import tempfile
from math import tau

import ffmpeg
import os
from geometry import *
from read_bsc import *

W = 16
H = 9

def janim_to_cairo(v):
    x, y = v

    x_new = 120 * (x + W/2)
    y_new = 120 * (-y + H/2)

    return x_new, y_new



def draw_frame(i):
    surface = cairo.ImageSurface(cairo.Format.ARGB32, 1920, 1080)
    context = cairo.Context(surface)

    # Set background color
    context.set_source_rgba(0, 0, 0, 1)
    context.paint()
    context.save()
    context.restore()

    context.set_line_width(60)
    context.set_source_rgba(1, 1, 1, 1)


    for star in filter(lambda s: s.magnitude < 5, stars):
        x = - star.ra * 16/tau + 8 + i/60
        y = star.dec * 16/tau

        x, y = janim_to_cairo((x, y))
        r = 3 * star.magnitude_to_radius()
        context.arc(x, y, r, 0, tau)
        context.fill()

    return surface


output = ffmpeg.output('moi.mp4')
for i in range(0, 300):
    frame_surface = draw_frame(i)
    f, path = tempfile.mkstemp('.png')
    os.close(f)

    frame_surface.write_to_png(path)

    #stream = ffmpeg.input(f)
