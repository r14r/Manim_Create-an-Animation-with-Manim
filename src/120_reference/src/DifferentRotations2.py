# ../../repositories/ManimCommunity_manim/docs/source/tutorials/quickstart.rst

from manim import *


class DifferentRotations2(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2*LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2*RIGHT)
        self.play(left_square.animate.rotate(PI), Rotate(
            right_square, angle=PI), run_time=2)
        self.wait()
