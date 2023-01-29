from manim import *


class TransformSquareToCircle(Scene):
    def construct(self):
        square = Square(color=BLUE)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
      
        self.play(GrowFromCenter(square))
        self.play(Transform(square, circle))
        self.wait()