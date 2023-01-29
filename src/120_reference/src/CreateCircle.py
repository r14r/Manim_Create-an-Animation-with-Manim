# ../../repositories/ManimCommunity_manim/docs/source/tutorials/quickstart.rst

from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()                   # create a circle
        # set the color and transparency
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))     # show the circle on screen
