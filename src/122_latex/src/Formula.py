from manim import *
from manimlib import *


class Formula(Scene):
    def construct(self):
        # t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        text = MathTex('a^2 + b^2 = c^2')
        
        #self.add(text)
        self.play(Write(text))
        self.wait(10)
         