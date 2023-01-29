
from manim import *


class BraceBPExample(Scene):
    def construct(self):
        p1 = [0, 0, 0]
        p2 = [1, 2, 0]
        brace = BraceBetweenPoints(p1, p2)
        self.play(Create(NumberPlane()))
        self.play(Create(brace))
        self.wait(2)
