from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        self.play(ShowCreation(square))
        self.play(FadeOut(square), ShowCreation(circle))
        self.wait(1)
