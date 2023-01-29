
import manimpango
from manim import *
from manimlib import *


class SimpleColor(Scene):
    def construct(self):
        col = Text("RED COLOR", color=RED)
        self.play(Write(col))
        self.wait(10)
