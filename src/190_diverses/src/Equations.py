# https://github.com/malhotra5/Manim-Tutorial
from manim import *
from manimlib import *


class Equations(Scene):
    def construct(self):
        # Making equations
        first_eq = r'$J(\\theta) = -\\frac{1}{m} [\\sum_{i=1}^{m} y^{(i)} \\log{h_{\\theta}(x^{(i)})} + (1-y^{(i)}) \\log{(1-h_{\\theta}(x^{(i)}))}] $$'
        second_eq = ["$J(\\theta_{0}, \\theta_{1})$", "=", "$\\frac{1}{2m}$",
                     "$\\sum\\limits_{i=1}^m$", "(", "$h_{\\theta}(x^{(i)})$", "-", "$y^{(i)}$", "$)^2$"]

        second_mob = MathTex(*second_eq)

        for i, item in enumerate(second_mob):
            if(i != 0):
                item.next_to(second_mob[i-1], RIGHT)

        return
        eq2 = VGroup(*second_mob)

        des1 = MathTex(
            "With manim, you can write complex equations like this...")
        des2 = MathTex("Or this...")
        des3 = MathTex("And it looks nice!!")

        # Coloring equations
        second_mob.set_color_by_gradient("#33ccff", "#ff00ff")

        # Positioning equations
        des1.shift(2*UP)
        des2.shift(2*UP)

        # Animating equations
        self.play(Write(des1))
        self.play(Write(first_eq))
        self.play(ReplacementTransform(des1, des2), Transform(first_eq, eq2))
        self.wait(1)

        for i, item in enumerate(eq2):
            if (i < 2):
                eq2[i].set_color(color=PURPLE)
            else:
                eq2[i].set_color(color="#00FFFF")

        self.add(eq2)
        self.wait(1)
        self.play(FadeOut(eq2), FadeOut(
            first_eq), Transform(des2, des3))
        self.wait(2)
