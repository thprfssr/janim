import ffmpeg
import os
import shutil
import tempfile
from tqdm import tqdm

from astro import *
from camera import *
from geometry import *
from vector import *


def draw_frame(i, camera):
    camera.draw_background()
    context = camera.get_cairo_context()

    for star in sky.stars:
        v = star.get_stereographic(i/720).scale(12)
        v = camera.janim_to_cairo_coordinates(v)

        r = 10 * star.magnitude_to_radius()
        circle = Circle(r, v)
        circle.draw(context)

camera = Camera()
sky = CelestialSphere()
directory = tempfile.mkdtemp()
for i in tqdm(range(0, 120)):
    draw_frame(i, camera)

    name = os.path.join(directory, 'JANIM-' + str(i).zfill(12) + '.png')
    camera.write_to_png(name)

(
        ffmpeg
        .input(os.path.join(directory, 'JANIM-*.png'), pattern_type = 'glob', framerate = 60)
        .output('moi.mp4')
        .run()
)

shutil.rmtree(directory)
