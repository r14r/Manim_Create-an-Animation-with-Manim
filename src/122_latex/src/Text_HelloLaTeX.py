
import manimpango
from manim import *
from manimlib import *


class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.play(Write(tex))


