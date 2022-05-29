# import colorgram
#
# colors = colorgram.extract("colored-dots.jpg", 20)
# rgb_color = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)
import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_extract = [(254, 253, 249), (247, 254, 252), (254, 249, 252), (176, 155, 18), (239, 247, 252), (31, 112, 165),
                 (150, 55, 123), (191, 7, 36), (24, 132, 123), (18, 91, 50), (213, 183, 62), (223, 206, 97),
                 (118, 170, 196), (16, 70, 40), (34, 155, 195), (199, 135, 164), (129, 177, 165), (41, 58, 114),
                 (183, 92, 122), (76, 153, 146)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_of_dots = 1000

for count_dot in range(1, numbers_of_dots + 1):
    tim.dot(5, random.choice(color_extract))
    tim.forward(5)
    if count_dot % 100 == 0:
        tim.setheading(90)
        tim.forward(5)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

my_screen = t.Screen()
my_screen.exitonclick()
