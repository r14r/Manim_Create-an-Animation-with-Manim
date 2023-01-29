# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)
