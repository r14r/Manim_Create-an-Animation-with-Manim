
from manim import *


class ShowWriteReversed(Scene):
    def construct(self):
        self.play(Write(Text("Hello", font_size=144), reverse=True))
        self.wait()
