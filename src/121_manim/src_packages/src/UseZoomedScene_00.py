
from manim import *


class UseZoomedScene(ZoomedScene):
    def construct(self):
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(1)
        self.activate_zooming(animate=False)
        self.wait(1)
        self.play(dot.animate.shift(LEFT))
