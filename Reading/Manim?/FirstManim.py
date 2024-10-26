from manim import *


class ShowScreenResolution(Scene):
    def construct(self):
        text = Tex("\frac{2}{2}")
        pixel_height = config["pixel_height"]  #  1080 is default
        pixel_width = config["pixel_width"]  # 1920 is default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        self.add(Text(str(pixel_height)))
