
from manim import *


class ValueTrackerExample(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        label = Dot(radius=3).add_updater(
            lambda x: x.set_x(tracker.get_value()))
        self.add(label)
        self.add(tracker)
        tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(2)
