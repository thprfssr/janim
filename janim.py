# A scene is basically the universe where all the objects of an animation
# reside. A scene should contain a camera that shows that scene to the world.
# It should also contain many objects in it. What the camera sees will be
# rendered into an SVG file.
class Scene:
    def __init__(self):
        self.actors = set()

    # Add an actor to the scene.
    def add(self, actor):
        self.actors.add(actor)

    # Remove an actor from the scene.
    def remove(self, actor):
        self.actors.remove(actor)


# An actor is an object that can be displayed in a scene.
class Actor:
    # The definition for the `__init__` function is usually supplied by the
    # children.
    def __init__(self):
        pass


# A camera is what shows the scene to the world.
class Camera:
    def __init__(
            self,
            frame_height = None,
            frame_width = None,
            frame_rate = None,
            ):
        pass
