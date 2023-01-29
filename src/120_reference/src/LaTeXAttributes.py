# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144)
        self.add(tex)
