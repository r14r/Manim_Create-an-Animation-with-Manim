# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        self.add(text)
