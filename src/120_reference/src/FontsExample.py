# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class FontsExample(Scene):
    def construct(self):
        ft = Text("Noto Sans", font="Noto Sans")
        self.add(ft)
