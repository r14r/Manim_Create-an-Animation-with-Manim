
import manimpango
from manim import *
from manimlib import *


class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX',
                  tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.play(Write(tex))
        self.wait(10)
