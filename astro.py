from bsc import *
from geometry import *
from janim import *
from vector import *

from math import tanh, tau, tan, acos, atan2, asin

class Star:
    def __init__(self, name, ra, dec, mag):
        self.name = name
        self.ra = ra
        self.dec = dec
        self.mag = mag

    # This function determines the radius of the dot to be drawn based on the
    # apparent magnitude of the star. The radius is a number between 0 and 1,
    # so you can scale it up later to suit your needs.
    def magnitude_to_radius(self):
        threshold = 3
        x = self.mag - threshold
        if self.mag > threshold:
            r = (1 - tanh(x)) / 2
        else:
            slope = (1/2) * 1/threshold
            r = - slope * x + (1/2)
        return r

    def get_stereographic(self, hour_angle):
        theta = tau/4 - self.dec
        r = tan(theta / 2)
        phi = hour_angle - self.ra
        return Vector(r * cos(phi), r * sin(phi))

class CelestialSphere(Element):
    def __init__(self, cutoff_magnitude = 5, hour_angle = 0):
        self.hour_angle = hour_angle
        self.cutoff_magnitude = cutoff_magnitude
        self.stars = set()
        for name in STARS.keys():
            ra      = float(STARS[name]['ra'])
            dec     = float(STARS[name]['dec'])
            mag     = float(STARS[name]['mag'])

            if mag < cutoff_magnitude:
                s = Star(name, ra, dec, mag)
                self.stars.add(s)

    def rotate(self, theta):
        self.angle += theta

    def draw(self, camera):
        context = camera.get_cairo_context()
        for s in self.stars:
            v = s.get_stereographic(self.hour_angle)
            v = camera.janim_to_cairo_coordinates(v)

            r = 10 * s.magnitude_to_radius()
            circe = Circle(r, v)
            circle.draw(camera)


class Telescope(Element):
    def __init__(self, sky = CelestialSphere(),
            lat    = 0,
            alt    = 0,
            azi     = 0,
            ):
        self.sky = sky
        self.lat = lat
        self.alt = alt
        self.azi = azi

    def draw(self, camera):
        for star in self.sky.stars:
            # Convert geocentric coordinates to spherical coordinates
            x = cos(star.dec) * cos(star.ra)
            y = cos(star.dec) * sin(star.ra)
            z = sin(star.dec)

            # Adjust their position according to your latitude
            y_new = y * cos(self.lat) - z * sin(self.lat)
            z_new = z * cos(self.lat) + y * sin(self.lat)
            y, z = y_new, z_new

            # Convert to stereographic
            theta = acos(z)
            phi = - atan2(y, x)
            r = tan(theta/2)
            v = Vector(r * cos(phi), r * sin(phi))
            if v.norm() > 1:
                continue
            v *= 12
            v = camera.janim_to_cairo_coordinates(v)

            circle = Circle(5 * star.magnitude_to_radius(), v)
            circle.draw(camera)
