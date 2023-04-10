# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)
