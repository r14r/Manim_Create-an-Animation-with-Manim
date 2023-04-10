from manim import *


class LaTeXAlignEnvironment(Scene):
    def demo1(self):
        lines = MathTex(
            r'       9 * 9 + 7 = 88        \\'
            r'      98 * 9 + 6 = 888       \\'
            r'     987 * 9 + 5 = 8888      \\'
            r'    9876 * 9 + 4 = 88888     \\'
            r'   98765 * 9 + 3 = 888888    \\'
            r'  987654 * 9 + 2 = 8888888   \\'
            r' 9876543 * 9 + 1 = 88888888  ', font_size=36)

        # self.play(FadeIn(lines), run_time=10)
        # self.wait(5)

        # Create Text objects
        t1 = MathTex(r'       9 * 9 + 7 &= 88        \\')
        t2 = MathTex(r'      98 * 9 + 6 &= 888       \\')
        t3 = MathTex(r'     987 * 9 + 5 &= 8888      \\')

        # Position second line underneath first line
        t2.next_to(t1, DOWN)
        t3.next_to(t2, DOWN)

        # Displaying text
        self.wait(1)
        self.play(FadeIn(t1))
        self.play(FadeIn(t2))
        self.play(FadeIn(t3))
        self.wait(5)

        self.play(ReplacementTransform(t1, t3))
        self.wait(1)

        # self.play(FadeOut(t3))
        self.wait(2)

    def MovingFrameBox(self):
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=",
            "f(x)\\frac{d}{dx}g(x)",
            "+",
            "g(x)\\frac{d}{dx}f(x)",
        )
        self.play(Write(text))

        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1),)
        self.wait()

        self.play(ReplacementTransform(framebox1, framebox2),)
        self.wait()

    def demo2(self):
        elements = [
            '      9 * 9 + 1', '=', '88888888'
            '     98 * 9 + 2', '=', '88888888'
            '    987 * 9 + 3', '=', '88888888'
            '   9876 * 9 + 4', '=', '88888888'
            '  98765 * 9 + 5', '=', '88888888'
            ' 987654 * 9 + 6', '=', '88888888'
            '9876543 * 9 + 7', '=', '88888888'
        ]

        math = [MathTex(element) for element in elements]

        # Write equations
        sign1 = MathTex("=")

        el_l1 = MathTex("2x^2-5x+2")
        el_l1.next_to(sign1, LEFT)

        el_r1 = MathTex("2x^2-4x-x+2")
        el_r1.next_to(sign1, RIGHT)

        sign2 = MathTex("=")
        el_r2 = MathTex("(x-2)(2x-1)")

        # Put each equation or sign in the appropriate positions
        sign2.shift(DOWN)
        el_r2.shift(DOWN)

        # Align bottom equations with the top equations
        sign2.align_to(sign1, LEFT)
        el_r2.align_to(el_r1, LEFT)

        # Group equations and sign
        group = VGroup(el_l1,
                       sign1,
                       el_r1,
                       sign2,
                       el_r2)

        # Create animation
        for element in group:
            self.play(Write(element))

        self.wait()

        framebox1 = SurroundingRectangle(el_r1, buff=0.1)
        framebox2 = SurroundingRectangle(el_r2, buff=0.1)
        self.play(Create(framebox1),)
        self.wait()

        self.play(ReplacementTransform(framebox1, framebox2),)
        self.wait()

    def demo5(self):
        elements = [
            '      9 * 9 + 1' + '&=' + '88888888' + r'\\' +
            '     98 * 9 + 2' + '&=' + '88888888' + r'\\' +
            '    987 * 9 + 3' + '&=' + '88888888' + r'\\' +
            '   9876 * 9 + 4' + '&=' + '88888888' + r'\\' +
            '  98765 * 9 + 5' + '&=' + '88888888' + r'\\' +
            ' 987654 * 9 + 6' + '&=' + '88888888' + r'\\' +
            '9876543 * 9 + 7' + '&=' + '88888888'
        ]

        group = MathTex(elements)
        group.scale(0.8)

        self.play(Write(group))

        self.wait(50)

    def demo6(self):
        elements = MathTable(
            [
                ['      9 * 9', '+', '1', '=', '88'],
                ['     98 * 9', '+', '2', '=', '888'],
                ['    987 * 9', '+', '3', '=', '8888'],
                ['   9876 * 9', '+', '4', '=', '88888'],
                ['  98765 * 9', '+', '5', '=', '888888'],
                [' 987654 * 9', '+', '6', '=', '8888888'],
                ['9876543 * 9', '+', '7', '=', '88888888']
            ],
            include_outer_lines=True,

            # row_labels=[Text("R1"), Text("R2")],
            # col_labels=[Text("C1"), Text("C2")]
        )

        # elements.add_highlighted_cell((2, 2), color=YELLOW)
        elements.get_horizontal_lines()[:].set_color(YELLOW)
        elements.get_vertical_lines()[:].set_color(BLACK)

        group = VGroup(
            elements
        ).scale(0.7).arrange_in_grid(buff=1)

        self.add(group)

        for element in group:
            self.play(Write(element))
            self.wait(4)

        self.wait(50)

        return
        group = VGroup()

        prev_op, prev_sg = None, None

        for indx, item in enumerate(elements):
            print(indx, item)

            l1 = MathTex(item[0])  # left
            op = MathTex(item[1])  # operator
            l2 = MathTex(item[2])  # left
            sg = MathTex(item[3])  # sign
            r1 = MathTex(item[4])  # right

            op.next_to(l1, RIGHT)
            l2.next_to(op, RIGHT)
            sg.next_to(l2, RIGHT)
            r1.next_to(sg, RIGHT)

            l1.shift((indx + 1) * DOWN)
            op.shift((indx + 1) * DOWN)
            l2.shift((indx + 1) * DOWN)
            sg.shift((indx + 1) * DOWN)
            r1.shift((indx + 1) * DOWN)

            if indx > 0:
                op.align_to(prev_op, LEFT)
                sg.align_to(prev_sg, LEFT)
            else:
                prev_op, prev_sg = op, sg

            group.add(l1, op, l2, sg, r1)

        # Create animation
        for element in group:
            self.play(Write(element))

        self.wait()

    def construct(self):
        elements = [
            ['      9 * 9', '+', '1', '=', '88'],
            ['     98 * 9', '+', '2', '=', '888'],
            ['    987 * 9', '+', '3', '=', '8888'],
            ['   9876 * 9', '+', '4', '=', '88888'],
            ['  98765 * 9', '+', '5', '=', '888888'],
            [' 987654 * 9', '+', '6', '=', '8888888'],
            ['9876543 * 9', '+', '7', '=', '88888888']
        ]

        group = VGroup()

        title = Title("Fun with Multiplication", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))

        prev_op, prev_sg = None, None

        for indx, item in enumerate(elements):
            print(indx, item)

            l1 = MathTex(item[0])  # left
            op = MathTex(item[1])  # operator
            l2 = MathTex(item[2])  # left
            sg = MathTex(item[3])  # sign
            r1 = MathTex(item[4])  # right

            l1.next_to(op, LEFT)
            l2.next_to(op, RIGHT)
            sg.next_to(l2, RIGHT)
            r1.next_to(sg, RIGHT)

            step = (indx + 1) * DOWN

            if indx > 0:
                op.align_to(prev_op, LEFT)
                sg.align_to(prev_sg, LEFT)

            else:
                prev_op, prev_sg = op, sg

            l1.shift(step)
            op.shift(step)
            l2.shift(step)
            sg.shift(step)
            r1.shift(step)

            group.add(l1, op, l2, sg, r1)

        # Create animation
        for element in group:
            self.play(FadeIn(element))

        self.wait()
