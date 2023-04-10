
import manimpango
from manim import *
from manimlib import *


class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED)

        self.play(Write(tex))
        self.wait(10)