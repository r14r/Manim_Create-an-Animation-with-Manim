
from manim import *


class EndAnimation(Scene):
    def construct(self):
        def func(pos): return np.sin(
            pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(
            func, stroke_width=3, max_anchors_per_line=5, virtual_time=1, color=BLUE
        )
        self.add(stream_lines)
        stream_lines.start_animation(
            warm_up=False, flow_speed=1.5, time_width=0.5)
        self.wait(1)
        self.play(stream_lines.end_animation())
