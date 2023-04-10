
from manim import *


class MatchingEquationParts(Scene):
    def construct(self):
        eq1 = MathTex("{{a^2}} + {{b^2}} = {{c^2}}")
        eq2 = MathTex("{{a^2}} = {{c^2}} - {{b^2}}")
        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(0.5)
