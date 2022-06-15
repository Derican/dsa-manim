from manimlib.imports import *
from random import uniform
from itertools import combinations


def calc_area(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1[:2], p2[:2], p3[:2]
    return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)


class Opening(Scene):
    def construct(self):
        context0 = TextMobject(
            "To measure is to know. If you can not measure it,")
        context1 = TextMobject("you can not imporve it.").next_to(
            context0, DOWN).align_to(context0, LEFT)
        context2 = TextMobject("- Lord Kelvin").next_to(context1,
                                                        DOWN).align_to(
                                                            context1, LEFT)

        self.play(Write(context0))
        self.play(Write(context1))
        self.play(Write(context2))
        self.wait(2)
        self.play(FadeOut(context0))
        self.play(FadeOut(context1))
        self.play(FadeOut(context2))
        self.wait()


class Main(Scene):
    def construct(self):
        t00 = TextMobject("Algorithm").scale(2)
        t01 = TextMobject("Accuracy", color=RED).next_to(t00, UP)
        t02 = TextMobject("Cost", color=RED).next_to(t00, DOWN)

        self.play(Write(t00))
        self.wait(2)
        self.play(FadeInFromDown(t01))
        self.play(FadeInFrom(t02, UP))
        self.wait()

        t03 = TextMobject("complex math tools").move_to([-3, 2, 0])
        arr0 = Arrow(start=t01.get_corner(LEFT + UP), end=t03.get_bottom())
        t04 = TextMobject("can be measured in advance").move_to([3, -2, 0])
        arr1 = Arrow(start=t02.get_corner(RIGHT + DOWN), end=t04.get_top())

        self.play(Indicate(t01))
        self.play(ShowCreation(arr0))
        self.play(Write(t03))
        self.wait(2)
        self.play(Indicate(t02))
        self.play(ShowCreation(arr1))
        self.play(Write(t04))
        self.wait(3)

        t05 = TextMobject("Time").scale(0.8).next_to(t02, LEFT)
        t06 = TextMobject("Memory").scale(0.8).next_to(t02, LEFT)

        self.play(FocusOn(t04))
        self.play(FadeInFromDown(t05))
        self.play(FadeOutAndShift(t05, UP), FadeInFromDown(t06))
        self.wait()
        height = t02.get_height()
        t05.shift([0, height / 2, 0])
        self.play(FadeInFrom(t05, UP), t06.shift, [0, -height / 2, 0])
        self.wait()

        rec0 = Rectangle(color=BLUE).surround(VGroup(t00, t02, t05, t06))
        f00 = TexMobject(r"T_A(P)").next_to(rec0, UP)

        self.play(FadeOut(VGroup(t01, arr0, arr1, t04, t03)),
                  ShowCreation(rec0))
        self.wait()
        self.play(Write(f00))
        self.wait()
        # debugTeX(self, f00[0])

        self.play(Indicate(f00[0][1]))
        self.play(Indicate(t00))
        self.wait()
        self.play(Indicate(f00[0][3]))
        self.wait()

        self.play(f00.shift, [0, 2, 0],
                  FadeOut(VGroup(t00, t02, t05, t06, rec0)))
        self.wait()
        self.play(Indicate(f00[0][3]))
        self.wait()

        f01 = TexMobject(r"T_A(n)").move_to(f00)
        f02 = TexMobject(r"|P|=n").next_to(f01, RIGHT)

        self.play(ReplacementTransform(f00, f01))
        self.play(Write(f02))
        self.wait()
        self.play(FadeOut(f02))
        self.wait()

        t07 = TextMobject(
            "Is there a triangle whose area is bigger than 4?").next_to(
                f01, DOWN).align_on_border(LEFT)
        dots = [
            Dot([uniform(-3.0, 3.0), uniform(-4.0, 1.0), 0]) for i in range(8)
        ]

        anims = LaggedStart(*[ShowCreation(dot) for dot in dots])
        self.play(anims)
        self.wait()
        self.play(Write(t07))
        self.wait(2)

        self.play(Indicate(f01[0][3]))
        self.wait()
        self.play(LaggedStart(*[Indicate(dot) for dot in dots]))
        self.wait(2)

        t08 = TextMobject("Area=").next_to(t07, DOWN).align_to(t07, LEFT)
        tri = Polygon(dots[0].get_arc_center(),
                      dots[1].get_arc_center(),
                      dots[2].get_arc_center(),
                      fill_color=TSINGHUA,
                      fill_opacity=0.7)
        area = DecimalNumber(calc_area(dots[0].get_arc_center(),
                                       dots[1].get_arc_center(),
                                       dots[2].get_arc_center()),
                             num_decimal_places=5).next_to(t08, RIGHT)

        self.play(DrawBorderThenFill(tri))
        self.wait()
        self.play(Indicate(tri), Write(t08))
        self.play(Write(area))
        self.wait()

        area.add_updater(lambda a: a.set_value(calc_area(*tri.get_vertices())))
        for i, j, k in combinations(range(8), 3):
            self.play(tri.set_points_as_corners, [
                dots[i].get_arc_center(), dots[j].get_arc_center(),
                dots[k].get_arc_center(), dots[i].get_arc_center()
            ])
            self.wait(2)
            if (area.get_value() > 4.0):
                break

        self.wait(2)
        self.play(
            LaggedStart(*[
                ApplyMethod(dot.move_arc_center_to,
                            [uniform(-3.0, 3.0),
                             uniform(-4.0, 1.0), 0]) for dot in dots
            ]))
        self.wait(2)
        for i, j, k in combinations(range(8), 3):
            self.play(tri.set_points_as_corners, [
                dots[i].get_arc_center(), dots[j].get_arc_center(),
                dots[k].get_arc_center(), dots[i].get_arc_center()
            ])
            self.wait(2)
            if (area.get_value() > 4.0):
                break

        self.wait(2)
        t09 = TextMobject(r"$\binom{n}{3}$ in total!").scale(1.5).next_to(
            t08, DOWN, aligned_edge=LEFT)
        self.play(Write(t09))
        self.wait()

        f03 = TexMobject(r"=\max{\lbrace T_A(P)\bigm | |P|=n \rbrace}")
        self.play(f01.shift, [-3, 0, 0])
        f03.next_to(f01, RIGHT)
        self.play(Write(f03))
        self.wait()

        self.clear()
        self.play(FadeIn(t00))
        self.wait()
        self.play(t00.shift, [0, 2, 0])

        t10 = TextMobject("Programmer").move_to([-4, 1, 0])
        t11 = TextMobject("Language").move_to([0, 1, 0])
        t12 = TextMobject("Compiler").move_to([4, 1, 0])
        t13 = TextMobject("Structure").move_to([-2, 0, 0])
        t14 = TextMobject("System").move_to([2, 0, 0])
        rec1 = Rectangle(color=BLUE).surround(
            VGroup(t00, t10, t11, t12, t13, t14))

        self.play(Write(t10))
        self.play(Write(t11))
        self.play(Write(t12))
        self.play(Write(t13))
        self.play(Write(t14))
        self.play(ShowCreation(rec1))
        self.wait()
        self.play(Indicate(t00))
        self.wait()
