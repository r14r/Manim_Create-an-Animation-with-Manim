
import manimpango
from manim import *
from manimlib import *


class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.play(Write(tex))
        self.wait()
