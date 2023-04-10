from manim import *


class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2cwords = Text('World', t2c={'rl': RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)

        self.wait()
