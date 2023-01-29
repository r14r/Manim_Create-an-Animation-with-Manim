from manim import *
from pascalTriangle import PascalTriangle


class PascalTriangle_1(Scene):
    def construct(self):

        # Create a 11 rows Pascal Triangle
        pascal = PascalTriangle(11)

        self.add(pascal)
        self.wait()
