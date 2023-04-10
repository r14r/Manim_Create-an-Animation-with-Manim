# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC)
        self.add(a)
