
from manim import *


class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        
        self.play(Write(tex))
        self.wait()


