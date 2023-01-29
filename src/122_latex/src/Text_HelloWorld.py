
import manimpango
from manim import *
from manimlib import *


class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.play(Write(text))


