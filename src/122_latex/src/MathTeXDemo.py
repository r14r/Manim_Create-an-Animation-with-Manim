
import manimpango
from manim import *
from manimlib import *


class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.play(Write(VGroup(rtarrow0, rtarrow1).arrange(DOWN)))
        self.wait(10)
