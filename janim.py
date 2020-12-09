# A Scene is basically the universe where all the objects of an animation
# reside. A Scene should contain a camera that shows that Scene to the world.
# It should also contain many objects in it. What the Camera sees will be
# rendered into a Cairo image surface.
class Scene:
    def __init__(self):
        self.actors = set()

    # Add an actor to the scene.
    def add(self, actor):
        self.actors.add(actor)

    # Remove an actor from the scene.
    def remove(self, actor):
        self.actors.remove(actor)


# An Element is an object that can be displayed in a scene.
class Element:
    # The definition for the `__init__` function is usually supplied by the
    # children.
    def __init__(self):
        pass
