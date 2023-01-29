
import manimpango
from manim import *
from manimlib import *


class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED)
        self.play(Write(text))
