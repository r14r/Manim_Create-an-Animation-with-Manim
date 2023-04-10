
from manim import *


class JustifyText(Scene):
    def construct(self):
        ipsum_text = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            "Praesent feugiat metus sit amet iaculis pulvinar. Nulla posuere "
            "quam a ex aliquam, eleifend consectetur tellus viverra. Aliquam "
            "fermentum interdum justo, nec rutrum elit pretium ac. Nam quis "
            "leo pulvinar, dignissim est at, venenatis nisi. Quisque mattis "
            "dolor ut euismod hendrerit. Nullam eu ante sollicitudin, commodo "
            "risus a, vehicula odio. Nam urna tortor, aliquam a nibh eu, commodo "
            "imperdiet arcu. Donec tincidunt commodo enim a tincidunt."
        )
        justified_text = MarkupText(ipsum_text, justify=True).scale(0.4)
        not_justified_text = MarkupText(ipsum_text, justify=False).scale(0.4)
        just_title = Title("Justified")
        njust_title = Title("Not Justified")
        self.add(njust_title, not_justified_text)
        self.play(
            Transform(
                not_justified_text,
                justified_text,
            ),
            Transform(
                njust_title,
                just_title,
            ),
            run_time=2,
        )
        self.wait(1)
