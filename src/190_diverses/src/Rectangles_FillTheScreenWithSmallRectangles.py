from manim import *


class FillTheScreenWithSmallRectangles(Scene):
    rect_size = 0.25

    def fill_rect(self, m=1, n=1, h=rect_size, w=rect_size, column=True):
        rect = Rectangle(height=h, width=w).set_fill(
            YELLOW, opacity=0.8).set_stroke(width=0)

        if column:
            col = VGroup(*[rect.copy() for i in range(m)]).arrange(DOWN)
            result = VGroup(*[col.copy() for i in range(n)]).arrange(RIGHT)
        else:
            row = VGroup(*[rect.copy() for i in range(n)]).arrange(RIGHT)
            result = VGroup(*[row.copy() for i in range(m)]).arrange(DOWN)

        return result

    def col_rect(self, m, n):
        h = self.rect_size * (2 * m - 1)
        return self.fill_rect(m=1, n=n, h=h, w=self.rect_size, column=False)

    def row_rect(self, m, n):
        w = self.rect_size * (2 * n - 1)
        return self.fill_rect(m=m, n=1, h=self.rect_size, w=w, column=True)

    def construct(self):

        obj = self.fill_rect(m=10, n=10, column=False)
        self.play(Write(obj))
        self.wait()

        self.play(FadeOut(obj))

        obj = self.col_rect(m=10, n=10)
        self.play(Write(obj))
        self.wait()

        self.play(FadeOut(obj))

        self.play(Write(self.row_rect(m=10, n=10)))
        self.wait()
