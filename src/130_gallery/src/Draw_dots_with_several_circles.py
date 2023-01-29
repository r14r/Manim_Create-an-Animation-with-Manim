# https://infograph.tistory.com/239

from manimlib.imports import *


# draw dots instead the lines
class Rotate_Circles3_DrawDots(Scene):
    def construct(self):
        running_time = 10.2

        ### 1. circles and dots
        circles_radius = [2.5, 1, 0.8, 0.4, 0.1]
        circle_orgins = [
            np.array([0, 0, 0]), np.array([0 + 2.5, 0, 0]),
            np.array([2.5 + 1, 0, 0]), np.array([3.5 + 0.8, 0, 0]),
            np.array([4.3 + 0.1, 0, 0]),
        ]
        curve_start = np.array([4.4, 0, 0])
        circles = [Circle(radius=r, name=str(i)) for i, r in enumerate(circles_radius)]
        for c, p in zip(circles, circle_orgins): c.move_to(p)

        dots = [Dot(radius=0.01, name=str(i)) for i in range(len(circles) - 1)]
        dots.append(Dot(radius=0.06, name=str(len(circles) - 1), color=YELLOW))
        for i in range(len(dots)):
            dots[i].move_to(circles[i].point_from_proportion(0))
        freqs = [0.1, 0.2, 0.3, 0.2, 1]  # how many times rotate in a second

        self.add(*(circles), *(dots))

        self.play(Write(*(circles), *(dots)))

        ### 2. rotates them
        # base timer
        self.t_offset = 0  # will be same as real time. 1 means one second

        def update_time(mob, dt):
            self.t_offset += dt

        circles[0].add_updater(update_time)

        # update circles
        def update_circle(mob):
            circle = mob.copy()
            idx = int(circle.name)
            circle.move_to(dots[idx - 1].get_center())  # circle2 move to dot1's center
            mob.become(circle)

        # update dots
        def update_dot(mob):
            dot = mob.copy()
            idx = int(dot.name)
            prop = (self.t_offset * freqs[idx]) % 1
            dot.move_to(circles[idx].point_from_proportion(prop))
            mob.become(dot)

        # draw curve with dots
        def update_curve(mob):
            group = mob.copy()
            new_dot = Dot(point=dots[-1].get_center(),radius=0.05, color=YELLOW_D)
            group.add(new_dot)
            mob.become(group)

        # run: circle, dot, line, curve
        for c in circles[1:]: c.add_updater(update_circle)  # caution: start with 1
        for d in dots: d.add_updater(update_dot)

        curve = VGroup(Dot(point=dots[-1].get_center(), radius=0.05, color=YELLOW_D))
        self.add(curve)
        curve.add_updater(update_curve)

        self.wait(running_time)

        circles[0].remove_updater(update_time)