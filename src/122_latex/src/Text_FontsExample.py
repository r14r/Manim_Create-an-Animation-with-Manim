
import manimpango
from manim import *
from manimlib import *


class FontsExample(Scene):
    def construct(self):
        ft = Text("Noto Sans", font="Noto Sans")
        self.play(Write(ft))


