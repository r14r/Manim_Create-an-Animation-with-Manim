# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class SimpleColor(Scene):
    def construct(self):
        col = Text("RED COLOR", color=RED)
        self.add(col)
