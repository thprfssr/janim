import cairo

from math import tau

W = 1920
H = 1080

with cairo.SVGSurface('test.svg', W, H) as surface:
    context = cairo.Context(surface)
    context.rectangle(100, 100, 100, 100)
    context.rectangle(500, 100, 100, 100)

    # The call to `new_sub_path()` is needed to prevent the circle from
    # connecting to the previous rectangle.
    context.new_sub_path()
    context.arc(700, 700, 100, 0, tau)

    x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
    x2, y2, x3, y3 = 0.4, 0.1, 0.9, 0.6

    context.scale(700, 700)
    context.set_line_width(0.04)
    context.move_to(x, y)

    context.curve_to(x1, y1, x2, y2, x3, y3)

    # setting color of the context
    context.set_source_rgba(0.4, 1, 0.4, 1)

    # stroke out the color and width property
    context.stroke()


print("File Saved")
