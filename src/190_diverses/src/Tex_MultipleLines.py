from manim import *


class a20200514_20(Scene):
    def construct(self):
        f_1 = MathTex(r"""
            \Big( 1 + {1 \over n}\Big)^n    
        """)

        f_1.to_edge(UL, buff=0.5)

        f_2 = MathTex("""
            \Big( 1 + {1 \over n}\Big)^2 = 1 + 2 \Big( {1 \over n} \Big) + \Big( {1 \over n} \Big)^2  
        """)

        f_3 = MathTex(r"""
            \Big( 1 + {1 \over n}\Big)^3 
            = 1 + 3 \Big( {1 \over n} \Big) + 3 \Big( {1 \over n} \Big)^2 + \Big( {1 \over n} \Big)^3 
        """)

        f_4 = MathTex(r"""
                \vdots
        """)

        f_5 = MathTex(r"""
            \Big( 1 + {1 \over n}\Big)^n 
            = 1 + {n \choose 1} \Big( {1 \over n} \Big) + \cdots 
            + {n \choose j} \Big( {1 \over n} \Big)^j + \cdots
            + \Big( {1 \over n} \Big)^n   
        """)

        F = VGroup(f_1, f_2, f_3, f_4, f_5)

        F.arrange_submobjects(DOWN, buff=0.5)

        # self.play(FadeIn(F[:]))
        for f in F:
            self.play(FadeIn(f))
            self.wait(1)

        self.play(FadeOut(F))
