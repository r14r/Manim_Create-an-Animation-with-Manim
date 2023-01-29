
from manim import *


class ShuffleSubmobjectsExample(Scene):
    def construct(self):
        s = VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20, 20)])
        s2 = s.copy()
        s2.shuffle_submobjects()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))
        self.wait()
