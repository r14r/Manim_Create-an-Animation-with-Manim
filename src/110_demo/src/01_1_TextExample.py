#from manimlib import *
from manim import *
#from manimlib.constants import FRAME_WIDTH


class TextExample(Scene):
    def construct(self):
        text1 = Text(
            "Here is a text",
            font="Consolas",
            font_size=90,
            t2c={"Here": BLUE, "text": GREEN}
        )

        text2 = Text(
            """
            The most important difference between Text and TexText is that\n
            you can change the font more easily, but can't use the LaTeX grammar
            """,
            font="Arial", font_size=24
        )

        VGroup(text1, text2).arrange(DOWN, buff=1)

        text3 = Text(
            "You can set the font for different words",
            font="Arial",
            t2f={"font": "Consolas", "words": "Consolas"},
            t2c={"font": BLUE, "words": GREEN}
        )

        text4 = Text(
            "Same as slant and weight",
            font="Consolas",
            t2s={"slant": ITALIC},
            t2w={"weight": BOLD},
            t2c={"slant": ORANGE, "weight": RED}
        )

        VGroup(text3, text4).arrange(DOWN, buff=0.5)

        # ANIMATION
        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.wait(3)

        #
        self.play(FadeOut(text1, shift=UP), FadeOut(text2, shift=DOWN))

        #
        self.play(FadeIn(text3))
        self.wait()

        #
        self.play(FadeIn(text4))
        self.wait()
