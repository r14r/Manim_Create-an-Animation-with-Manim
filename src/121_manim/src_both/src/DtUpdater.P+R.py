
from manim import *


class DtUpdater(Scene):
    def construct(self):
        line = Square()

        # Let the line rotate 90° per second
        line.add_updater(lambda mobject, dt: mobject.rotate(dt*90*DEGREES))
        self.add(line)
        self.wait(2)
