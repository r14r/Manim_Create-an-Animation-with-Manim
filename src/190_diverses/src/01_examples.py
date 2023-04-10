
from scipy.stats import binom
from manimlib.imports import *


class a20200509_10(Scene):
    def construct(self):

        fx = lambda x: x.get_value()**2

        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))


x_tex = Integer(x_value.get_value()).add_updater(
    lambda v: v.set_value(x_value.get_value()))
        dot = Dot(radious=x_value.get_value()).add_updater(
            lambda x: x.move_to(0.1*x_value.get_value()))

        self.add(x_tex)
        self.add(dot)

        self.play(
            x_value.set_value, 30,
            rate_func=linear,
            run_time=10
            )
        self.wait()


class a20200509_08(Scene):
    def construct(self):


str = r"""
            C = {1 \over r} \sum^{n}_{j=0} {{n}\choose{j}} p^{j} (1-p)^{n-j}
            \max [ u^{j} d^{n-j} S - K , 0 ]
        """
        str = str.split()
        f_1 = TexMobject(*str)
        f_1.scale(0.7)
        self.play(Write(f_1))
        self.wait()
str = r"""
             = {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j}
            ( u^{j} d^{n-j} S - K )
        """
        str = str.split()
        f_2 = TexMobject(*str)
        f_2.scale(0.7)
        self.play(ApplyMethod(f_1.shift, UP*1.2))
        self.play(Write(f_2))
        self.wait()
str = r"""
             = S {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j} u^{j} d^{n-j}
             - K {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j}
        """
        str = str.split()
        f_3 = TexMobject(*str)
        f_3.scale(0.7)
        self.play(ApplyMethod(f_1.shift, UP*1.2),
                  ApplyMethod(f_2.shift, UP*1.2))
        self.play(Write(f_3))
        self.wait()
str = r"""
             = S {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} [ p u ]^{j} [ (1-p) d ]^{n-j}
             - K {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j}
        """
        str = str.split()
        f_4 = TexMobject(*str)
        f_4.scale(0.7)
        self.play(Write(f_4.shift(DOWN*1.2)))
        self.wait()
str = r"""
             = S \sum^{n}_{j=a} {{n}\choose{j}}
             \Big[ {p u \over r} \Big]^{j} \Big[ {(1-p) d \over r} \Big]^{n-j}
             - K {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j}
        """
        str = str.split()
        f_5 = TexMobject(*str)
        f_5.scale(0.7)
        self.play(Write(f_5.shift(DOWN*2.4)))
        self.wait()


class a20200507_10(GraphScene):

    CONFIG = {
        "y_max": 1,
        "x_max": 1,
        "axes_color": BLUE,
    }


def construct(self):


self.setup_axes(animate=True)
g = lambda x: 4 * x * (1-x)
graph = self.get_graph(
            g,
            color=GREEN
        )
self.play(
            Create(graph),
        )
        self.wait(1)
h = lambda x: x
graph = self.get_graph(
            h,
            color=RED
        )
self.play(
            Create(graph),
        )
        self.wait(1)
pt = Dot()
        # pt.move_to(self.coords_to_point(0.5, 0.3))
        # self.play(
        #     Create(pt),
        # )
# #pt.move_to(self.coords_to_point(0.5, 0.5))
        # self.play(
        #     ApplyMethod(pt.move_to, self.coords_to_point(0.5, 0.5) )
        # )
x = [0.1, 0.2, ]
        x = 0.3
        for i in range(30):

            self.play(ApplyMethod(pt.move_to, self.coords_to_point(x, g(x))))
            self.play(ApplyMethod(pt.move_to, self.coords_to_point(g(x,), g(x))))
            x = g(x)
self.graph_origin = RIGHT*2 + UP*2
        self.setup_axes(animate=True)
g = lambda x: 4 * x * (1-x)
graph = self.get_graph(
            g,
            color=GREEN
        )
self.play(
            Create(graph),
        )
        self.wait(1)
x = [0.1, 0.2, ]
        x = 0.3
        for i in range(30):

            self.play(ApplyMethod(pt.move_to, self.coords_to_point(x, g(x))))
            self.play(ApplyMethod(pt.move_to, self.coords_to_point(g(x,), g(x))))
            x = g(x)

a20200507_10.py
a20200509_12.py


class a20200509_12(GraphScene):

    CONFIG = {
            "y_min": 0,
            "y_max": 0.3,
            "x_min": 0,
            "x_max": 31,
            "y_axis_label": "$\\mathbb{P} (X=x)$",
        }


def construct(self):

        self.setup_axes(animate=True,)


N = 10
        p = 0.6
v_1 = self.plot_things(4, p)
        self.add(v_1)

        for N in range(5, 31):
            v = self.plot_things(N, p)
            self.play(Transform(v_1, v))
self.add(v_1)
        self.wait()


def plot_things(self, N, p):


string = "N = {}, p = {}".format(N, p)
        string = string.split()
        f_1 = TexMobject(*string)
        f_1.move_to(UP*3+RIGHT)
things = VGroup()
for i in range(N+1):
            thing = Dot()
            thing.move_to(self.coords_to_point(i, binom.pmf(i, n=N, p=p)))
            things.add(thing)

        return VGroup(f_1, things)

a20200509_12.py
a20200510_05.py
2.5 is related to graph orientation.
from manimlib.imports import *
from scipy.stats import binom
class a20200510_05(GraphScene):
    
    CONFIG = {
            "y_min" : 0,
            "y_max" : 0.3,
            "x_min" : 0,
            "x_max" : 31,
            "y_axis_label": "$\\mathbb{P} (X=x)$",
        }
def construct(self):
        
        self.setup_axes(animate=True,)
N = 10
        p = 0.2
v_1 = self.plot_things(4,p)
        self.add(v_1)
        
        for N in range(5,31):
            v = self.plot_things(N, p)
            self.play(Transform(v_1, v))
self.add(v_1)
        self.wait()
def plot_things(self, N, p):
string = "N = {}, p = {}".format(N,p)
        string = string.split()
        f_1 = TexMobject(*string)
        f_1.move_to(UP*3+RIGHT)
things = VGroup()
for i in range(N+1):
            thing = Dot()
            line = Line(start=[0,0.01,0], end=[0,0,0])
            line.set_length(self.coords_to_point(i, binom.pmf(i, n=N, p=p))[1] + 2.5)
            thing.move_to(self.coords_to_point(i, binom.pmf(i, n=N, p=p)))
            line.move_to(self.coords_to_point(i, binom.pmf(i, n=N, p=p)/2))
            things.add(thing, line)
        
        return VGroup(f_1, things)

a20200510_05.py
Next
1








More from A Ydobon
Follow

Ydobon is nobody.

May 1, 2020

[Financial Engineering] Reformulating the formula
We might be satisfied with our current formula. However, by reformulating the formula we can obtain more insights from it. Moreover, it will be much easier to deal with other relationships that will be covered in the following sessions. The goal is to find the minimum number of upward movements…

Financial Engineering
3 min read



[Financial Engineering] Reformulating the formula
Share your ideas with millions of readers.

Write on Medium
Mar 19, 2020

[Economic Theory]4. Demand in Depth
Hello, everyone! How’s everything where you are at? WHO announced that we are at pandemic situation and my friends in Milan told me that they aren’t allowed to go out without permission. It is depressing situation, however, I think it is extremely crucial to stay calm and follow the rules…

Economic Theory
6 min read



[Economic Theory]4. Demand in Depth
Mar 9, 2020

[Economic Theory]3.b. Slutsky Equation
How’s everyone? This is such a frustrating time in South Korea. Everyone seems to be calm but worried at the same time. The worst part is the boredom around. I hope we could get over this 🙏. I. Introduction. This will the last posting on the demand part in Microeconomics. …

Economic Theory
5 min read



[Economic Theory]3.b. Slutsky Equation
Feb 25, 2020

[Economic Theory]3-a. Indifference Curves
Hello, how’s everyone? I’m focusing on moving my body at a gym despite the nCoV crisis. Also, I’ve got more spare time for yoga, so this week I’m focusing on my shoulders and upper body🧘🏻‍♀️. …

Microeconomics
8 min read



[Economic Theory]3-a. Indifference Curves
Feb 17, 2020

[Economic Theory]2-b. Elasticities
Hello, everyone. This week we are going to deal with utility maximization and demand curve, in other words, “RATIONALITY”. However, in this post, we will recap on what elasticities are. 1. Elasticity of Demand We sometimes underestimate the feature of elasticity; independent of units. The elasticity is defined at each point on a demand…

Economics
4 min read



[Economic Theory]2-b. Elasticities
Love podcasts or audiobooks? Learn on the go with our new app.

Try Knowable
Search
A Ydobon
A Ydobon
84 Followers

Ydobon is nobody.

Follow

Help

Status

Writers

Blog

Careers

Privacy

Terms

About

Knowable

