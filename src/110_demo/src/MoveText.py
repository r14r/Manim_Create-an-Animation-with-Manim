from manim import *


class MoveText(Scene):
    def construct(self):

        #circle1 = Circle(color=BLUE).move_to(0.5*UP).scale(1.7)
        #circle2 = Circle(radius=1, color=BLUE).move_to(0.5*UP).scale(1)

        text1 = Text("Mert Cobanov").scale(0.7).to_corner(DR)
        text2 = Text("Data Science").scale(2).move_to(2*DOWN)

        img = ImageMobject(
            "jf"
        ).scale(1.7).move_to(UP)

        self.play(
            # Write(circle1),
            FadeIn(img),
            FadeIn(text2),
            FadeIn(text1),
            run_time=2
        )

        self.play(
            FadeOut(img),
            FadeOut(text1),
            FadeOut(text2)
        )

        # self.play(
        #    ReplacementTransform(circle1, circle2),
        #    run_time=0.7
        # )

        self.wait()
