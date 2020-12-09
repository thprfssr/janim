import cairo

from vector import *
from constants import *

# Default camera constants
FRAME_HEIGHT    = 9
FRAME_WIDTH     = 16
PIXEL_HEIGHT    = 1920
PIXEL_WIDTH     = 1080
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

    def create_cairo_surface(self):
        self.surface = cairo.ImageSurface(
                cairo.Format.ARGB32,
                height  = self.pixel_height,
                width   = self.pixel_width,
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

        x_new = (x + fw/2) * pw/fw
        y_new = (-y + fh/2) * ph/fh

        return Vector(x_new, y_new)
