from manimlib.imports import *
from random import randint


class Main(Scene):
    def construct(self):

        total = 9

        up_line = Line([-8, 1, 0], [8, 1, 0])
        dn_line = Line([-8, 0, 0], [8, 0, 0])

        first_block_x = -4
        vertical_lines = VGroup()
        for i in range(total):
            vertical_lines.add(
                Line([first_block_x + i, 1, 0], [first_block_x + i, 0, 0]))

        left_etc = TexMobject(r"\cdots").next_to(vertical_lines[0].get_left(),
                                                 LEFT)
        right_etc = TexMobject(r"\cdots").next_to(
            vertical_lines[-1].get_right(), RIGHT)

        self.play(ShowCreation(up_line), ShowCreation(dn_line))
        self.wait()

        lagged = LaggedStart(*[
            ShowCreation(line)
            for line in [left_etc, *vertical_lines, right_etc]
        ])
        self.play(lagged)
        self.wait()

        first_num_x = first_block_x + 0.5

        blanks = VGroup()
        for i in range(total - 1):
            blanks.add(TextMobject("B").move_to([first_num_x + i, 0.5, 0]))
        lagged = LaggedStart(*[Write(num) for num in blanks])
        self.play(lagged)
        self.wait()

        nums = VGroup()
        for i in range(total - 1):
            nums.add(
                TextMobject(
                    str(randint(0, 1) if i != 0 and i != total -
                        2 else "B")).move_to([first_num_x + i, 0.5, 0]))

        self.play(ReplacementTransform(blanks, nums))
        self.wait()

        pointer = Arrow(start=[first_num_x, 2, 0], end=[first_num_x, 1,
                                                        0]).scale(1.5)
        self.play(ShowCreation(pointer))
        for direction in [RIGHT, RIGHT, RIGHT, LEFT]:
            self.play(pointer.shift, direction)
        self.wait()
