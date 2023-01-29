from manim import BLUE, YELLOW, YELLOW_A
from manimlib.imports import *


class LongSineCurve(Scene):
    def construct(self):
        self.show_axis()
        self.show_circle_dot()
        self.draw_several_cycle()

        self.wait()

    def show_axis(self):
        self.x_start = np.array([-6,0,0])
        x_axis = Line(self.x_start, np.array([6, 0, 0]))
        y_axis = Line(np.array([-4, -2, 0]), np.array([-4, 2, 0]))

        self.add(x_axis, y_axis)

        self.origin_point = np.array([-4, 0, 0])
        self.curve_start = np.array([-3, 0, 0])

        self.one_cycle_length = 2 * PI
        self.curve_end = np.array([self.curve_start[0] + self.one_cycle_length, 0, 0])

    def show_circle_dot(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(circle.point_from_proportion(0))

        self.add(circle, dot)
        self.circle = circle
        self.dot = dot
    def draw_several_cycle(self):
        dot = self.dot
        orgin_point = self.origin_point

        self.t_offset = 0
        rate = 0.25
        one_cycle_time= (1 / rate) + (1/self.camera.frame_rate) * rate

        def go_around_circle(mob, dt):
            self.t_offset += dt
            # print(self.t_offset)
            mob.move_to(self.circle.point_from_proportion((self.t_offset * rate) % 1))

        def get_line_to_circle():
            return Line(orgin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_end[0]  # fixing to the end of the curve
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        def get_sine_curve(dx=0):
            return FunctionGraph(
                lambda x: np.sin(x-self.curve_start[0]+dx),
                x_min=self.x_start[0], x_max=self.curve_end[0],
            )

        def get_updated_sine_curve():
            return get_sine_curve(dx=self.t_offset * ( PI / 2))


        dot.add_updater(go_around_circle)


        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)

        sine_curve = always_redraw(get_updated_sine_curve)

        self.add(origin_to_circle_line, dot_to_curve_line, sine_curve)
        self.wait(one_cycle_time*4)

        dot.remove_updater(go_around_circle)