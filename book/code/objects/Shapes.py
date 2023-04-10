import numpy as np

from manim import *


class Shapes(Scene):

    def anim(self, text, mob):
        title = Title(text)

        self.add(title)
        self.play(Create(mob))
        self.play(FadeOut(mob))
        self.remove(title)

    def construct(self):
        circulo = Circle()  # Creación de circulo
        createCircle = Create(circulo)  # Animación de creación
        self.play(createCircle)  # Mostrar la animación
        fadeOutCircle = FadeOut(circulo)  # Animación de desaparición
        self.play(fadeOutCircle)  # Mostrar la animación

        # Rectangulo con color
        rect = Rectangle(color="blue", height=3, width=1)
        # rect = Rectangle(color="#0000FF") # Rectangulo con color en hexadecimal
        self.play(Create(rect))
        self.play(FadeOut(rect))

        cuadrado = Square()  # Cuadrado
        # Llevas al cuadrado a la posición designada
        cuadrado.move_to(np.array([-4, 2, 0]))
        #                         ( x, y, z)
        cuadrado2 = Square()
        cuadrado2.to_edge(UP)  # LLeva una figura al borde
        # Hay cuatro direcciónes UP, LEFT, RIGHT, DOWN
        self.play(Create(cuadrado), Create(cuadrado2))
        self.play(FadeOut(cuadrado), FadeOut(cuadrado2))

        linea = Line(np.array([2, 0, 0]), np.array([-2, 1, 0]))
        self.play(Create(linea))
        self.play(FadeOut(linea))

        self.wait()

        self.anim("Arc", Arc(radius=0.5))
        self.anim("ArcBetweenPoints", ArcBetweenPoints(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim("CurvedArrow", CurvedArrow(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim("CurvedDoubleArrow", CurvedDoubleArrow(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim("Circle", Circle())
        self.anim("Dot", Dot())
        # self.anim("SmallDot", SmallDot())
        self.anim("Ellipse", Ellipse())
        self.anim("AnnularSector", AnnularSector())
        self.anim("Sector", Sector())
        self.anim("Annulus", Annulus())
        self.anim("Line", Line(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim("DashedLine", DashedLine(np.array([2, 0, 0]), np.array([-2, 0, 0])))

        # Tangent line requires a mobject
        c = Circle()
        self.play(Create(c))
        self.anim("TangentLine", TangentLine(c, 0.2))
        self.play(FadeOut(c))

        self.anim("Elbow", Elbow())
        self.anim("Arrow", Arrow(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim("Vector", Vector(np.array([1, 0, 0])))
        self.anim("DoubleArrow", DoubleArrow(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim("Polygon", Polygon(np.array([2, 0, 0]), np.array(
            [-2, 0, 0]), np.array([1, 1, 0]), np.array([-2, -3, 0])))
        self.anim("RegularPolygon", RegularPolygon(n=5))
        self.anim("Triangle", Triangle())
        #self.anim("ArrowTip", ArrowTip())
        self.anim("Rectangle", Rectangle())
        self.anim("Square", Square())
        self.anim("RoundedRectangle", RoundedRectangle())
