# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)
