from manim import *


class ObjectsAppearDisappear(Scene):
    def construct(self):

        text1 = Text(
            "This is a sample Text\n" +
            "which should be disappear a few minuste",
            t2c={'sample': ORANGE, 'should': BLUE},
            #t2w={'disappear ': BOLD}
        )

        circle = Circle()
        text2 = Text("Text is gone :)")

        self.play(Write(text1), Create(circle))
        self.wait(2)

        self.remove(text1)
        self.wait(2)

        self.remove(circle)
        self.wait(2)

        self.play(Write(text2))
        self.wait()
