
from manim import *


class PathAlongCirclesExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        circle_center = Dot(3 * LEFT)
        self.add(circle_center)

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.path_along_circles(
                    2 * PI, circle_center.get_center()
                ),
                run_time=3,
            )
        )
        self.wait()
