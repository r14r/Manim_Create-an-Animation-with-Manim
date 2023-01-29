
from manim import *


class ChangeOfDirection(Scene):
    def construct(self):
        ccw = RegularPolygon(5)
        ccw.shift(LEFT).rotate
        cw = RegularPolygon(5)
        cw.shift(RIGHT).reverse_direction()

        self.play(Create(ccw), Create(cw),
                  run_time=4)
        self.wait()
