from bsc import *

from math import tanh

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

class CelestialSphere:
    def __init__(self, cutoff_magnitude = 5, angle = 0):
        self.angle = angle
        self.cutoff_magnitude = cutoff_magnitude
        self.stars = set()
        for name in STARS.keys():
            ra      = float(STARS[name]['ra'])
            dec     = float(STARS[name]['dec'])
            mag     = float(STARS[name]['mag'])

            if mag < cutoff_magnitude:
                s = Star(name, ra, dec, mag)
                self.stars.add(s)

    def rotate(theta):
        self.angle += theta
