#Import all core components we need to use
# including all math functions
from manim import *
import math

# Define a PascalTriangleExplainer scene
# (In Manim, a scene is like a sillouete onto which we display things)
class PascalTriangleExplainer(Scene):
    
    # Funtion using combinations formula to calculate coefficients for nth row beginning with first row where n=0 
    def get_pascal_row(self, n):
        return [math.comb(n, k) for k in range(n + 1)]

    def construct(self):
        # Create 6 rows to display in the Pascal's triangle
        ROWS_TO_SHOW = 6  # Rows 0 through 5

        # Create 3 manim text objects to display as headings
        student_name = Text("Presented by Gavin Waako", font_size=48, color=YELLOW)
        class_name = Text("Intro to Computation", font_size=40, color=BLUE_B)
        school_name = Text("MassBay Community College", font_size=36, color=WHITE)

        # Combine the above 3 text mobjects into a single text group displaying them vertically downwards with some space between
        intro_group = VGroup(student_name, class_name, school_name).arrange(DOWN, buff=0.5)
        
        # Display the heading group on the screen using the write animation on it
        self.play(Write(intro_group), run_time=1.5)

        # Pause screen for 2 seconds
        self.wait(2.0)

        # Makes the text object above animate off screen moving upwards
        self.play(FadeOut(intro_group, shift=UP), run_time=1.0)

        # Creates a mathematical text mobject with 2 headings
        title = MathTex(
            r"\text{Commonly used in }", 
            r"\text{Binomial Theorem}", 
            font_size=64, 
            color=BLUE
        ).scale(1.2)
        
        # Animates the above mathematical text mobject on screen using a write animation
        self.play(Write(title), run_time=2.0)

        # Pause screen for 1 second
        self.wait(1.0)
        
        # Indicate creates a glow around the second part of the mathematical text mobject above
        # Then animates it on screen
        self.play(
            Indicate(title[1], scale_factor=1.1, color=YELLOW),
            run_time=1.5
        )

        # Pause screen for 0.5 seconds
        self.wait(0.5)

        # Animates the title above on screen fading it out upwards
        self.play(FadeOut(title, shift=UP))

        # Initializes empty VGroup to hold pascal triangle rows and values
        all_rows = VGroup()
        # Loop iterates from 0 to 5 (Number of rows)
        for i in range(ROWS_TO_SHOW):
            row_coeffs = self.get_pascal_row(i)
            row_mobjects = VGroup(*[MathTex(str(coeff), font_size=48) for coeff in row_coeffs])
            # Arranges all numbers in current row horizontally
            row_mobjects.arrange(RIGHT, buff=0.8)
            
            if i == 0:
                # Positions first row 1 point from top of screen
                row_mobjects.to_edge(UP, buff=1.0)
            else:
                # Stores reference to the last created row
                last_row = all_rows[-1]
                # Positions current row 0.7 points below the last row
                row_mobjects.next_to(last_row, DOWN, buff=0.7)
                # Sets horizontal center coordinate of current row to match that of the last row
                # Thereby centering all rows and creating the triangle
                row_mobjects.set_x(last_row.get_x())
            # Adds fully centered row to master row containing all rows created
            all_rows.add(row_mobjects)

        # Animates the appearance of every row on screen
        self.play(
            LaggedStart(*[FadeIn(row, shift=DOWN) for row in all_rows], lag_ratio=0.3),
            run_time=3.0
        )

        # Pause screen for 1 second
        self.wait(1.0)
        
        # Create another explanation text mobject
        explanation_text = Text("To find any number, find the sum of the 2 numbers above it.", font_size=32).to_edge(DOWN)
        
        # Using the write animation, display the above text mobject on the screen
        self.play(Write(explanation_text))

        # Pause screen for 1 second
        self.wait(1.0)
        
        row_2 = all_rows[2]
        row_3 = all_rows[3]
        
        num_a = row_2[1]  # The '2'
        num_b = row_2[2]  # The '1'
        pos_sum = row_3[2] # The '3' below them

        self.play(
            num_a.animate.set_color(GREEN), 
            num_b.animate.set_color(GREEN),
            Indicate(VGroup(num_a, num_b)),
            run_time=1.0
        )
        
        path_a = Line(num_a.get_bottom(), pos_sum.get_top(), color=GREEN, stroke_width=4)
        path_b = Line(num_b.get_bottom(), pos_sum.get_top(), color=GREEN, stroke_width=4)
        
        self.play(Create(path_a), Create(path_b), run_time=1.0)
        
        self.play(
            pos_sum.animate.set_color(YELLOW),
            path_a.animate.set_color(YELLOW),
            path_b.animate.set_color(YELLOW),
            run_time=1.0
        )

        # Pause screen for 0.5 seconds
        self.wait(0.5)

        self.play(
            FadeToColor(VGroup(num_a, num_b, pos_sum), WHITE),
            FadeOut(VGroup(path_a, path_b)),
            run_time=1.0
        )

        row_3 = all_rows[3]
        row_4 = all_rows[4]

        num_c = row_3[1] # The first '3'
        num_d = row_3[2] # The second '3'
        pos_sum_2 = row_4[2] # The '6' below them (3+3)

        self.play(
            num_c.animate.set_color(GREEN),
            num_d.animate.set_color(GREEN),
            Indicate(VGroup(num_c, num_d)),
            run_time=1.0
        )

        path_c = Line(num_c.get_bottom(), pos_sum_2.get_top(), color=GREEN, stroke_width=4)
        path_d = Line(num_d.get_bottom(), pos_sum_2.get_top(), color=GREEN, stroke_width=4)

        self.play(Create(path_c), Create(path_d), run_time=1.0)

        self.play(
            pos_sum_2.animate.set_color(YELLOW),
            path_c.animate.set_color(YELLOW),
            path_d.animate.set_color(YELLOW),
            run_time=1.0
        )

        # Pause screen for 1 second
        self.wait(1.0)

        self.play(
            FadeToColor(VGroup(num_c, num_d, pos_sum_2), WHITE),
            FadeOut(VGroup(path_c, path_d, explanation_text), shift=DOWN),
            run_time=1.5
        )

        # Pause screen for 0.5 seconds
        self.wait(0.5)
        
        # Pick out all the numbers in row number 4
        row_4_coeffs = all_rows[4] # [1, 4, 6, 4, 1]
        
        # Keep track of all rows that aren't in position 4
        rows_to_remove = VGroup(*[row for i, row in enumerate(all_rows) if i != 4])

        # Animate on screen while removing all rows except row 4
        # Move row number 4 to center of screen
        # Then move it again half a unit up
        self.play(
            FadeOut(rows_to_remove),
            row_4_coeffs.animate.move_to(ORIGIN).shift(UP * 0.5), # Move Row 4 to center
            run_time=1.5
        )

        # Create a manim mathtext object to display binormial formula
        # Then positions it 4 points above row_4_coeffs
        binomial_formula = MathTex(
            r"(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k",
            font_size=54,
            color=PURPLE
        ).next_to(row_4_coeffs, UP, buff=1.0)

        # Animate the binormial formula on screen using write effect for 2 seconds
        self.play(Write(binomial_formula), run_time=2.0)

        # Pause screen for 0.5 seconds
        self.wait(0.5)

        # Create MathText mobject to hold formula and position it below row number 4 elements
        expansion = MathTex(
            r"(a+b)^4 = ",
            r"1", r"a^4 + ",
            r"4", r"a^3b + ",
            r"6", r"a^2b^2 + ",
            r"4", r"ab^3 + ",
            r"1", r"b^4"
        ).next_to(row_4_coeffs, DOWN, buff=1.0)
        
        # Animate on screen using the write effect the expanded formula above
        self.play(Write(expansion[0]), run_time=0.5) 
        
        coeff_indices = [1, 3, 5, 7, 9]
        row_4_indices = [0, 1, 2, 3, 4]
        
        
        for exp_i, row_i in zip(coeff_indices, row_4_indices):
            self.play(
                Write(expansion[exp_i:exp_i+2]),
                row_4_coeffs[row_i].animate.scale(1.5).set_color(PURPLE).set_opacity(0.8),
                run_time=0.5
            )

            # Pause screen for 0.2 seconds
            self.wait(0.2)

            # Animate 
            self.play(
                row_4_coeffs[row_i].animate.scale(1/1.5).set_color(WHITE).set_opacity(1.0),
                run_time=0.3
            )
        
        # Pause screen for 2 seconds
        self.wait(2.0)
        
        # Animates while fading out the above 3 elements on screen
        self.play(
            FadeOut(row_4_coeffs),
            FadeOut(binomial_formula),
            FadeOut(expansion),
            run_time=2.0
        )

        # Create mobject to hold text and animate it on screen
        final_message = VGroup(
            Text("Thank you for watching!", font_size=36, color=YELLOW)
        ).arrange(DOWN, buff=0.8)

        # Animate final_message on screen with write effect
        self.play(Write(final_message), run_time=2.0)

        # Pause screen for 3 seconds
        self.wait(3.0)

        # Animate final_message on screen with fadeout effect
        self.play(FadeOut(final_message))

        # Pause screen for 1 second
        self.wait(1.0)