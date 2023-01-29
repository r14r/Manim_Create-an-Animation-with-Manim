
from manim import *


class UsingFlash(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(DOWN)
        self.add(Tex("Flash the dot below:"), dot)
        self.play(Flash(dot))
        self.wait()
