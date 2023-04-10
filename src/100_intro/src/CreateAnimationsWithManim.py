from manim import *


class CreateAnimationsWithManim(Scene):
    def construct(self):
        text = Text("Create Animations with Manim", font_size=60)
        self.play(Write(text))
