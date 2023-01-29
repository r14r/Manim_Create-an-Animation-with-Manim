#
# https://towardsdatascience.com/how-to-create-mathematical-animations-like-3blue1brown-using-python-f571fb9da3d1
#

from manim import *


class PointMovingOnShapes2(Scene):
    def construct(self):

        # Create a square
        square = Square(color=BLUE)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        # Create a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        # Create animations
        self.play(GrowFromCenter(square))
        self.play(Transform(square, circle))  # turn the square into a circle

        self.wait()  # wait for some seconds
