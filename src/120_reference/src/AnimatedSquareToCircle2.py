# ../../repositories/ManimCommunity_manim/docs/source/tutorials/quickstart.rst

from manim import *


class AnimatedSquareToCircle2(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        # transform the square into a circle
        self.play(ReplacementTransform(square, circle))
        # color the circle on screen
        self.play(circle.animate.set_fill(PINK, opacity=0.5))
