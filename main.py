#Here how to get color from images
"""
# import colorgram as C
#
# colors = C.extract("images.jpg",30)
#
#
# list_new = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_tuple =(r, g, b)
#     list_new.append(new_tuple)
# print(list_new)
"""
import turtle as t
import random

tim = t.Turtle()
colors_list = [(202, 10, 34), (241, 245, 251), (247, 236, 36), (241, 231, 3),(34, 217, 77), (224, 159, 62), (39, 79, 185), (28, 38, 160), (212, 71, 14), (18, 151, 21), (241, 36, 152), (188, 15, 10), (219, 22, 129),
               (73, 8, 28), (219, 140, 198), (59, 13, 8), (225, 160, 5), (65, 202, 228),(18, 17, 41), (10, 97, 60), (83, 74, 216), (94, 206, 136), (238, 158, 219),
               (97, 235, 194), (4, 230, 242), (223, 79, 47), (5, 71, 45)]
screen = t.Screen()
screen.colormode(255)
tim.speed("slow")
tim.hideturtle()
d = -300
tim.penup()
for i in range(10):
    tim.goto(-300, d)
    for z in range(10):
        color_random = random.randint(0,26)
        tim.penup()
        tup = colors_list[color_random]
        tim.pencolor(tup)
        tim.dot(30)
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.forward(100)
    d += 50
screen.exitonclick()

