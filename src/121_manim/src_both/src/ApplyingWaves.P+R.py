
from manim import *


class ApplyingWaves(Scene):
    def construct(self):
        tex = Tex("Wiggle").scale(3)
        self.play(Wiggle(tex))
        self.wait()
