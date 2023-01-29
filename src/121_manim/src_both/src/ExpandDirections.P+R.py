
from manim import *


class ExpandDirections(Scene):
    def construct(self):
        banners = [ManimBanner().scale(0.5).shift(UP*x) for x in [-2, 0, 2]]
        self.play(
            banners[0].expand(direction="right"),
            banners[1].expand(direction="center"),
            banners[2].expand(direction="left"),
        )

        self.wait()
