
from manim import *


class MovingAndZoomingCamera(MovingCameraScene):
    def construct(self):
        s = Square(color=BLUE, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=YELLOW, fill_opacity=0.5).move_to(2 * RIGHT)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s).set(width=s.width*2))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t).set(width=t.width*2))

        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))
