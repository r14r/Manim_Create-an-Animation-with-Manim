# ../../repositories/ManimCommunity_manim/docs/source/tutorials/using_text.rst

from manim import *


class IterateColor(Scene):
     def construct(self):
          text = Text("Colors", font_size=96)
          for letter in text:
                letter.set_color(random_bright_color())

          self.add(text)
          self.wait()
