from camera import *

# A Scene is basically the universe where all the objects of an animation
# reside. A Scene should contain a camera that shows that Scene to the world.
# It should also contain many objects in it. What the Camera sees will be
# rendered into a Cairo image surface.
class Scene:
    def __init__(self, camera = Camera()):
        self.elements = set()
        self.camera = camera

    # Add an actor to the scene.
    def add(self, element):
        self.elements.add(element)

    # Remove an element from the scene.
    def remove(self, element):
        self.elements.remove(element)

    # Draw the elements onto the camera.
    def draw(self):
        for e in self.elements:
            e.draw(self.camera)

    def write_to_png(self, filename):
        self.camera.write_to_png(filename)


# An Element is an object that can be displayed in a scene.
class Element:
    # The definition for the `__init__` function is usually supplied by the
    # children.
    def __init__(self):
        pass
