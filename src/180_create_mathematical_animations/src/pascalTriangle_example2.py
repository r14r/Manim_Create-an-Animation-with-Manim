from manim import *
from pascalTriangle import PascalTriangle


class PascalTriangle_2(Scene):
    def construct(self):

        # Create a 4 rows Pascal Triangle
        #   color gradient from RED to BLUE to YELLOW
        #   width value of 4
        pascal = PascalTriangle(rows=4, colors=[RED, BLUE, YELLOW], width=4)

        self.add(pascal)
        self.wait()
