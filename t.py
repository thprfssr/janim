from astro import *

import tempfile
import ffmpeg
from tqdm import tqdm
import os



def draw_frame(t, camera):
    camera.draw_background()
    telescope = Telescope(lat = t * (tau/2) -tau/4)
    telescope.draw(camera)


N = 3600
camera = Camera()
directory = tempfile.mkdtemp()
for i in tqdm(range(0, N)):
    draw_frame(i/N, camera)
    name = os.path.join(directory, 'JANIM-' + str(i).zfill(12) + '.png')
    camera.write_to_png(name)

(
        ffmpeg
        .input(os.path.join(directory, 'JANIM-*.png'), pattern_type = 'glob', framerate = 60)
        .output('sky.mp4')
        .run()
)
