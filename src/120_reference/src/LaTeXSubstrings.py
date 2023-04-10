# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)
