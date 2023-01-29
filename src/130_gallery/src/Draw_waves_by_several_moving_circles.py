from manim import BLUE, YELLOW, YELLOW_D
from manimlib.imports import *


class Rotate_Circles(Scene):
    def construct(self):
        self.draw_axis()
        self.rotate_dots()

        self.wait()

    def draw_axis(self):
        #1. axis
        x_start = np.array([-6.5,0,0])
        x_axis = Line(x_start, np.array([6, 0, 0]), color=BLUE, )
        y_axis = Line(np.array([-4, 2, 0]), np.array([-4, -2, 0]), color=BLUE)


        self.add(x_axis, y_axis)

        #2. circles
        circles_radius = [1, 0.5, 0.3, 0.2, 0.6]
        circle_orgins = [
            np.array([-4,0,0]), np.array([-4+1,0,0]),
            np.array([-3+0.5,0,0]), np.array([-2.5+0.3,0,0]),
            np.array([-2.2+0.2,0,0]),
        ]
        curve_start = np.array([-2.0, 0, 0])
        circles = [Circle(radius=r, name=str(i) ) for i,r in enumerate(circles_radius)]
        for c, p  in zip(circles,circle_orgins): c.move_to(p)

        dots = [Dot(radius=0.01, name=str(i)) for i in range(len(circles)-1)]
        dots.append(Dot(radius=0.06, name=str(len(circles)-1), color=YELLOW))
        for i in range(len(dots)):
            dots[i].move_to(circles[i].point_from_proportion(0))
        freqs = [0.25, 0.25, 3/2, 3.5/2, 2] #how many times rotate in a second

        self.add(*(circles), *(dots))

        self.circles = circles
        self.dots = dots
        self.circles_radius = circles_radius
        self.freqs = freqs
        self.curve_start = curve_start

    def rotate_dots(self):
        circles = self.circles
        circles_radius = self.circles_radius
        dots = self.dots
        freqs = self.freqs
        running_time = 20

        # base timer
        self.t_offset = 0 #will be same as real time. 1 means one second

        def update_time(mob, dt):
            self.t_offset += dt

        circles[0].add_updater(update_time)

        # update circles
        def update_circle(mob):
            circle = mob.copy()
            idx = int(circle.name)
            circle.move_to(dots[idx-1].get_center()) #circle2 move to dot1's center
            mob.become(circle)

        # update dots
        def update_dot(mob):
            dot = mob.copy()
            idx = int(dot.name)
            prop = (self.t_offset * freqs[idx] ) % 1
            dot.move_to(circles[idx].point_from_proportion(prop))
            mob.become(dot)

        # update line from the last dot to the curve
        def update_line(mob):
            x = self.curve_start[0] + (self.t_offset * 7 / running_time)
            y = dots[-1].get_center()[1]
            line = Line(dots[-1].get_center(), np.array([x,y,0]))
            mob.become(line)

        # draw curve
        def update_curve(mob):
            line_group = mob.copy()
            last_line = line_group[-1]
            x = self.curve_start[0] + (self.t_offset * 7 / running_time)
            y = dots[-1].get_center()[1]
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            line_group.add(new_line)
            mob.become(line_group)

        # run: circle, dot, line, curve
        for c in circles[1:]: c.add_updater(update_circle) # caution: start with 1
        for d in dots: d.add_updater(update_dot)

        line = Line(dots[-1].get_center(), dots[-1].get_center())
        self.add(line)
        line.add_updater(update_line)

        curve = VGroup(Line(self.curve_start, self.curve_start))
        self.add(curve)
        curve.add_updater(update_curve)

        self.wait(running_time)

        circles[0].remove_updater(update_time)