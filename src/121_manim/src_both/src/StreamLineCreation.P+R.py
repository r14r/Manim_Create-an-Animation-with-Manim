
from manim import *


class StreamLineCreation(Scene):
    def construct(self):
        def func(pos): return (pos[0] * UR + pos[1] * LEFT) - pos
        stream_lines = StreamLines(
            func,
            color=YELLOW,
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            stroke_width=3,
            virtual_time=1,  # use shorter lines
            max_anchors_per_line=5,  # better performance with fewer anchors
        )
        self.play(stream_lines.create())  # uses virtual_time as run_time
        self.wait()
