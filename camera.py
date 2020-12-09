import cairo

from vector import *
from constants import *

# Default camera constants
FRAME_HEIGHT    = 9
FRAME_WIDTH     = 16
PIXEL_HEIGHT    = 1080
PIXEL_WIDTH     = 1920
FRAME_RATE      = 60
FRAME_CENTER    = ORIGIN


# A camera is what shows the scene to the world.
class Camera:
    def __init__(
            self,
            frame_height    = FRAME_HEIGHT,
            frame_width     = FRAME_WIDTH,
            frame_center    = FRAME_CENTER,
            frame_rate      = FRAME_RATE,
            pixel_height    = PIXEL_HEIGHT,
            pixel_width     = PIXEL_WIDTH,
            ):
        self.frame_height   = frame_height
        self.frame_width    = frame_width
        self.frame_rate     = frame_rate
        self.pixel_height   = pixel_height
        self.pixel_width    = pixel_width
        self.frame_center   = frame_center

        self.create_cairo_surface()
        self.draw_background()

    def create_cairo_surface(self):
        self.surface = cairo.ImageSurface(
                cairo.Format.ARGB32,
                self.pixel_width,
                self.pixel_height,
                )
        self.context = cairo.Context(self.surface)

        return self.surface

    def get_cairo_surface(self):
        return self.surface

    def get_cairo_context(self):
        return self.context

    def janim_to_cairo_coordinates(self, vector):
        x = vector.x
        y = vector.y
        fw = self.frame_width
        fh = self.frame_height
        pw = self.pixel_width
        ph = self.pixel_height

        v = Vector(x, y)

        x_new = (x + fw/2) * pw/fw
        y_new = (-y + fh/2) * ph/fh

        return Vector(x_new, y_new)

    def draw_background(self):
        self.context.set_source_rgba(0, 0, 0, 1)
        self.context.paint()

    def write_to_png(self, filename):
        self.surface.write_to_png(filename)
