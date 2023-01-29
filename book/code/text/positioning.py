from manim import *


class Positioning(Scene):
    def construct(self):
        text_c = Text("Center").scale(0.7)
        text_1 = Text("Center + 1").scale(0.7)
        text_1.shift(1 * DOWN)

        text_2 = Text("Center - 2").scale(0.7)
        text_2.shift(2 * UP)

        self.play(
            FadeIn(text_c),
            FadeIn(text_1),
            FadeIn(text_2),
            FadeIn(Text("DL").scale(0.7).to_corner(DL)),
            FadeIn(Text("DR").scale(0.7).to_corner(DR)),
            FadeIn(Text("UL").scale(0.7).to_corner(UL)),
            FadeIn(Text("UR").scale(0.7).to_corner(UR)),
            FadeIn(Text("LEFT").scale(0.7).to_corner(LEFT)),
            FadeIn(Text("RIGHT").scale(0.7).to_corner(RIGHT)),
            FadeIn(Text("UP").scale(0.7).to_corner(UP)),
            FadeIn(Text("DOWN").scale(0.7).to_corner(DOWN)),
        )

        self.wait(10)
