# ../../repositories/ManimCommunity_manim/docs/source/contributing/examples.rst

from manim import *


class Formula1(Scene):
    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b) - f(a)")
        self.add(t)
        self.wait(1)
