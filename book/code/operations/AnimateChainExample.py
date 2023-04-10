
from manim import *


class AnimateChainExample(Scene):
    def changeTitle(self, title, text):
        self.remove(title)
        newtitle = Title(text)
        self.add(newtitle)

        return newtitle

    def construct(self):
        s1 = Square()

        title = Title("** START **")
        self.add(title)

        title = self.changeTitle(title, "Create Square")
        self.play(Create(s1))
        self.wait(1)

        title = self.changeTitle(title, "Shift / Scale / Rotate")
        self.play(
            s1.animate.shift(RIGHT).scale(2).rotate(PI / 2),
            run_time=5
        )
        self.wait()

        title = self.changeTitle(title, "Uncreate")
        self.play(Uncreate(s1))
        self.wait()

        s2 = Square()

        title = self.changeTitle(title, "Create")
        self.play(Create(s2))
        self.wait()

        title = self.changeTitle(title, "Shift")
        self.play(s2.animate.shift(RIGHT))
        self.wait()

        title = self.changeTitle(title, "Scale")
        self.play(s2.animate.scale(2))
        self.wait()

        title = self.changeTitle(title, "Rotate")
        self.play(s2.animate.rotate(PI / 2))
        self.wait()

        self.play(Uncreate(s2))
