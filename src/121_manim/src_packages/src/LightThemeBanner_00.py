
from manim import *


class LightThemeBanner(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner = ManimBanner(dark_theme=False)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
