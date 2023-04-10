
import manimpango
from manim import *
from manimlib import *


class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC)
        self.play(Write(a))


