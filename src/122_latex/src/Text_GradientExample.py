
import manimpango
from manim import *
from manimlib import *


class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.play(Write(t))


