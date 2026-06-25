from turtle import Turtle, Screen
import random

mnz_turtle = Turtle()
# for _ in range(4):
#     mnz_turtle.forward(100)
#     mnz_turtle.left(90)
# mnz_turtle.forward(100)
# mnz_turtle.left(90)
# mnz_turtle.forward(100)
# mnz_turtle.left(90)
# mnz_turtle.forward(100)
# mnz_turtle.left(90)

# Draw dash line
# for _ in range(10):

#     mnz_turtle.forward(10)
#     mnz_turtle.penup()
#     mnz_turtle.forward(10)
#     mnz_turtle.pendown()


""" DRAW A TRAINGLE, SQUARE, PENTAGON, HEXAGON, HEPTAGON,
OCTAGON, NONAGON AND DECAGON"""

# def draw_shape(number_side):
#     angle = 360 / number_side
#     for _ in range(number_side):
#         mnz_turtle.forward(100)
#         mnz_turtle.left(angle)

# for shape_size_n in range(3, 12):
#     draw_shape(shape_size_n)

"""RANDOM WALK OF TURTLE"""

# directions = [0, 90, 180, 270]
# for _ in range(200):
#     mnz_turtle.forward(20)
#     mnz_turtle.setheading(random.choice(directions))


""" SPILOGRAPH """

my_screen = Screen()
my_screen.exitonclick