
import manimpango
from manim import *
from manimlib import *


class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):

        # correcet
        equation1 = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation1.set_color_by_tex("x", YELLOW)

        self.play(Write(equation1))
        self.wait()

        # Incorrect
        equation2 = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation2.set_color_by_tex("x", YELLOW)

        self.play(Write(equation2))
        self.wait()
