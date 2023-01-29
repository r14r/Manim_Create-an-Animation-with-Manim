from manim import *
# from manimlib import *


class Graph(Scene):
    # Scene.setup()
    # x_min=-3.5,
    # x_max=3.5,
    # y_min=-5,
    # y_max=5,
    # graph_origin=ORIGIN,
    # axes_color=BLUE,
    # x_labeled_nums=range(-4, 4, 2),  # x tickers
    # y_labeled_nums=range(-5, 5, 2),  # y tickers
    # **kwargs

    def construct(self):
        axes = Axes()

        # self.setup_axes(animate=False)

        # Draw graphs
        func_graph_cube = self.get_graph(lambda x: x**3, RED)
        func_graph_ncube = self.get_graph(lambda x: -x**3, GREEN)

        # Create labels
        graph_lab = self.get_graph_label(func_graph_cube, label="x^3")
        graph_lab2 = self.get_graph_label(
            func_graph_ncube, label="-x^3", x_val=-3)

        # Create a vertical line
        vert_line = self.get_vertical_line_to_graph(
            1.5, func_graph_cube, color=YELLOW)
        label_coord = self.input_to_graph_point(1.5, func_graph_cube)
        text = MathTex(r"x=1.5")
        text.next_to(label_coord)

        self.add(func_graph_cube, func_graph_ncube,
                 graph_lab, graph_lab2, vert_line, text)
        self.wait()
