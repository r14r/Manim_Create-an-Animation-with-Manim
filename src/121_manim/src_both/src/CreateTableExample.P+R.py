
from manim import *


class CreateTableExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
             ["Third", "Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            include_outer_lines=True)
        self.play(table.create())
        self.wait()
