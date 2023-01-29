from manim import *
from manimlib import *


class MovingFrameBox(Scene):
    def construct(self):
        equation = MathTex("2x^2-5x+2", "=", "(x-2)(2x-1)")

        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+",
            "g(x)\\frac{d}{dx}f(x)"
        )

        self.play(Write(text))

        framebox1 = SurroundingRectangle(text[1], buff=.1)
        framebox2 = SurroundingRectangle(text[3], buff=.1)

        self.play(Create(framebox1))
        self.wait()

        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()
