from manim import *


class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            Tex(r'$A^2 + B^2 = C^2$'),
            Tex(r'$A^2 = C^2 - B^2$'),
            Tex(r'$A^2 = (C + B)(C - B)$'),  # , isolate=["A^2", *to_isolate]),
            Tex(r'$A^2 = (C + B) * (C - B)$'), # , isolate = ["A", *to_isolate])
            #Tex(r'$A = \\sqrt{(C + B)(C - B)} $'),
        )

        lines.arrange(DOWN, buff=LARGE_BUFF)

        if False:
            for line in lines:
                line.set_color_by_tex_to_color_map({
                    "A": BLUE,
                    "B": TEAL,
                    "C": GREEN,
                })

        self.play(Write(lines))
        self.wait(5)

        return

        play_kw = {"run_time": 2}

        self.add(lines[0])
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

        return

        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()

        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # And to finish off, a simple TransformMatchingShapes would work
        # just fine.  But perhaps we want that exponent on A^2 to transform into
        # the square root symbol.  At the moment, lines[2] treats the expression
        # A^2 as a unit, so we might create a new version of the same line which
        # separates out just the A.  This way, when TransformMatchingTex lines up
        # all matching parts, the only mismatch will be between the "^2" from
        # new_line2 and the "\sqrt" from the final line.  By passing in,
        # transform_mismatches=True, it will transform this "^2" part into
        # the "\sqrt" part.
        # , isolate=["A", *to_isolate])
        new_line2 = MathTex("A^2 = (C + B)(C - B)")
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # Alternatively, if you don't want to think about breaking up
        # the tex strings deliberately, you can TransformMatchingShapes,
        # which will try to line up all pieces of a source mobject with
        # those of a target, regardless of the submobject hierarchy in
        # each one, according to whether those pieces have the same
        # shape (as best it can).
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()
