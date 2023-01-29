from manim import *


class SquareToCircle(Scene):
    _title = None

    def display(self, title):
        if self._title != None:
            self.play(FadeOut(self._title))

        self._title = Text(title)
        self.play(FadeIn(self._title.scale(0.7).to_corner(UP)))
        self.wait()

    def construct(self):
        self.display("Create Square")

        square = Square(color=BLUE)
        self.play(Create(square))

        self.display("Flip Square")
        square.flip(RIGHT)

        self.display("Rotate Square")
        square.rotate(-3 * TAU / 8)

        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        self.display("Grow from Center and transform")      
        self.play(GrowFromCenter(square))
        self.play(Transform(square, circle))
        self.wait()
