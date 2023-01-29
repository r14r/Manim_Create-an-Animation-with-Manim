
from manim import *


class SizingAndSpacing(Scene):
    def construct(self):
        def func(pos): return np.sin(
            pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        vf = ArrowVectorField(func, x_range=[-7, 7, 1])
        self.add(vf)
        self.wait()

        def length_func(x): return x / 3
        vf2 = ArrowVectorField(
            func, x_range=[-7, 7, 1], length_func=length_func)
        self.play(vf.animate.become(vf2))
        self.wait()
