from manim import *


class AlignColumnsInTable(Scene):
    def construct(self):
        table = VGroup(*[
            VGroup(*[
                Text(f"{t}") for t in row
            ]).arrange(DOWN, aligned_edge=RIGHT)
            for row in [
                ["Top"],
                ["Top", "Bottom"],
                ["Bottom", 40, 640, 200],
                ["Bottom", 160, 160, 800],
                [200, 800, 1000],
            ]],
        )

        table.scale(0.8)
        BUFF = 0.5
        rectangles = VGroup(*[
            Rectangle(
                width=mob.get_width()+BUFF,
                height=max(*[t.get_height() for t in table])+BUFF,
            ).move_to(mob)
            for mob in table
        ])

        for t, r, align_direction in zip(table, rectangles, [UP, None, None, None, DOWN]):
            if align_direction is not None:
                t.align_to(r, align_direction)
                t.shift(-align_direction*BUFF/2)

        table_group = VGroup(*[
            VGroup(t, r)
            for t, r in zip(table, rectangles)
        ])

        table_group.arrange(RIGHT, buff=0)
        self.add(table_group)

        self.wait()
