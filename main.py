# main.py: This file contains the 'main' function.Program execution begins and ends there.
# Created On: 2025-03-14
# Created By: Edward Cromwell
# An exploration of using numerical methods to solve differential equations in Python.

import numpy as np
from manim import *

viridis_10: list[ManimColor] = [ManimColor("#440154"), ManimColor("#482878"), ManimColor("#3e4989"), ManimColor("#31688e"), ManimColor("#26828e"),
           ManimColor("#1f9e89"), ManimColor("#35b779"), ManimColor("#6ece58"), ManimColor("#b5de2b"), ManimColor("#fde725")]

class VectorMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        func = VectorField.scale_func(func, 0.5)
        vector_field = ArrowVectorField(func, min_color_scheme_value=0, max_color_scheme_value=2, colors=viridis_10)
        self.add(vector_field)

        dot = Dot()
        vector_field.nudge(dot, -2, 60)

        trace = TracedPath(dot.get_center, stroke_color=GRAY)

        dot.add_updater(vector_field.get_nudge_updater())
        self.add(trace, dot)
        self.wait(6)