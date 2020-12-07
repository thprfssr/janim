from math import tanh

class Star:
    def __init__(self, name, ra, dec, magnitude):
        self.name = name
        self.ra = ra
        self.dec = dec
        self.magnitude = magnitude

    # This function determines the radius of the dot to be drawn based on the
    # apparent magnitude of the star. The radius is a number between 0 and 1,
    # so you can scale it up later to suit your needs.
    def magnitude_to_radius(self):
        threshold = 3
        x = self.magnitude - threshold
        if self.magnitude > threshold:
            r = (1 - tanh(x)) / 2
        else:
            slope = (1/2) * 1/threshold
            r = - slope * x + (1/2)
        return r
