
import manimpango
from manim import *
from manimlib import *


class LineSpacing(Scene):
    def construct(self):
        a = Text("Hello\nWorld", line_spacing=1)
        b = Text("Hello\nWorld", line_spacing=4)
        
        self.add(Group(a, b).arrange(LEFT, buff=5))
