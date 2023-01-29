# ../../repositories/ManimCommunity_manim/docs/source/tutorials/building_blocks.rst

from manim import *


class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
