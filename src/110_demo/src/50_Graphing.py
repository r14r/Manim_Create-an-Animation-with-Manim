import math

from manim import *

class Graphing(Scene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        def f2(x):
            return x**2

        def f3(x):
            return x**3

        def f1(x):
            return 2 * (x - 5) ** 2

        # Make graph
        # self.setup_axes(animate=True)

        xyaxes = Axes(
            x_range=[-10, 10],
            y_range=[-100, 100, 10],
            axis_config={"include_tip": False}
        )

        labels = xyaxes.get_axis_labels(
            x_label="x",
            y_label="f(x)"
        )

        t = ValueTracker(0)

        graph1 = xyaxes.plot(f1, color=MAROON)
        graph2 = xyaxes.plot(f2, color=RED)
        graph3 = xyaxes.plot(f3, color=BLUE)

        #
        #
        #
        initial_point = [
            xyaxes.coords_to_point(t.get_value(), f1(t.get_value()))
        ]

        dot = Dot(point=initial_point)
        dot.add_updater(lambda x: x.move_to(
            xyaxes.c2p(t.get_value(), f1(t.get_value())))
        )

        x_space = np.linspace(*xyaxes.x_range[:2], 200)
        minimum_index = f1(x_space).argmin()

        self.add(xyaxes, labels)
        self.wait()

        self.play(FadeIn(graph1))
        self.wait()

        # self.add(dot)
        # self.play(t.animate.set_value(x_space[minimum_index]))
        # self.wait()

        self.play(FadeOut(graph1))
        self.play(FadeIn(graph2))
        self.wait()
        self.play(
            Transform(graph2, graph3)
        )
        self.wait(2)

        return

        func_graph = self.get_graph(self.f1, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label="x^{2}")

        func_graph_2 = self.get_graph(
            self.f2, self.function_color)

        graph_lab_2 = self.get_graph_label(func_graph_2, label="x^{3}")

        vert_line = self.get_vertical_line_to_graph(
            1, func_graph, color=YELLOW)

        x = self.coords_to_point(1, self.f1(1))
        y = self.coords_to_point(0, self.f1(1))
        horz_line = Line(x, y, color=YELLOW)

        point = Dot(self.coords_to_point(1, self.f1(1)))

        # Display graph
        self.play(Create(func_graph), Write(graph_lab))
        self.wait(1)

        self.play(Create(vert_line))
        self.play(Create(horz_line))

        self.add(point)
        self.wait(1)

        self.play(
            Transform(func_graph, func_graph_2),
            Transform(graph_lab, graph_lab_2)
        )
        self.wait(2)
