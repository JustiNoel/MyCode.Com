from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # HSV to RGB conversion
        color(c)  # Set the color
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    # Use a valid RGB color (e.g., black)
    color((0, 0, 0))  # Black color as a placeholder

# Adding more patterns for completion
for i in range(36):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.01
    forward(i * 10)
    rt(144)

done()


