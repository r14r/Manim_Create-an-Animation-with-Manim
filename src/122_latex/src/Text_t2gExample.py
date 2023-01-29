
import manimpango
from manim import *
from manimlib import *


class t2gExample(Scene):
    def construct(self):
        t2gindices = Text(
            'Hello',
            t2g={
                '[1:-1]': (RED, GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'World',
            t2g={
                'World': (RED, BLUE),
            },
        ).next_to(t2gindices, RIGHT)

        self.play(Write(t2gindices))
        self.wait(5)

        self.play(Write(t2gwords))
        self.wait(5)
        