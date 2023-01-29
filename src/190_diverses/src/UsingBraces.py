from manim import *


class UsingBraces(Scene):
    def construct(self):
        eq1A = MathTex("41x + 3y")
        eq1B = MathTex("=")
        eq1C = MathTex("-5")
        eq2A = MathTex("5x -2y")
        eq2B = MathTex("=")
        eq2C = MathTex("3")

        eq1B.next_to(eq1A, RIGHT)
        eq1C.next_to(eq1B, RIGHT)

        eq2A.align_to(eq1A, LEFT)
        eq2B.align_to(eq1B, LEFT)
        eq2C.align_to(eq1C, LEFT)

        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)

        self.play(GrowFromCenter(braces), Write(eq_text))
        self.wait(50)
