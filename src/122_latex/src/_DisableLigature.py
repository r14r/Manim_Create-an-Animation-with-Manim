
import manimpango
from manim import *
from manimlib import *


class DisableLigature(Scene):
    def construct(self):
        li = Text("fl ligature", font_size=96)
        nli = Text("fl ligature", disable_ligatures=True, font_size=96)

        self.add(Group(li, nli).arrange(DOWN, buff=.8))
