from manim import *


class CoordsToPointExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()

        # a dot with respect to the axes
        dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(2, 2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane()
        dot_scene = Dot((2, 2, 0), color=RED)

        # self.add(plane, dot_scene, ax, dot_axes, lines)

        self.play(Write(plane))
        self.play(Write(dot_scene))
        self.play(Write(ax))
        self.play(Write(dot_axes))
        self.play(Write(lines))

        self.wait()
