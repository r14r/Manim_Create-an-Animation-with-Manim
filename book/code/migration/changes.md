# Changes

## Constants

FRAMEWITDH:

class TextExample(Scene):
    frame_width = config["frame_width"]
    frame_height = config["frame_height"]

    def demo:
        self.frame_width

## Objects

TexMobject is renamed to Text, 
TextMobject is renamed to MathTex

## Methods

### ThreeDScene

set_camera_position -> move_camera
