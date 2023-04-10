
import manimpango
from manim import *
from manimlib import *


class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144)
        self.play(Write(tex))
        self.wait()
