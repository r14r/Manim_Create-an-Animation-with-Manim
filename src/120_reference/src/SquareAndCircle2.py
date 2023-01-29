# ../../repositories/ManimCommunity_manim/docs/source/tutorials/quickstart.rst

from manim import *


class SquareAndCircle2(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        # set the color and transparency
        circle.set_fill(PINK, opacity=0.5)

        square = Square()  # create a square
        # set the color and transparency
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        # show the shapes on screen
        self.play(Create(circle), Create(square))
