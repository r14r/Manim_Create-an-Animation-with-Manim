
import manimpango
from manim import *
from manimlib import *


class BasicEquations(Scene):

    def construct(self):
        eq1 = MathTex("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2 = MathTex("\\vec{F}_{net} = \\sum_i \\vec{F}_i")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))


