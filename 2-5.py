import turtle,time
t5 = turtle.Turtle()
t6 = turtle.Turtle()
num_sides = int(input('要畫幾邊形(3-10):'))
side_length = 70
angle =360.0 / num_sides
for s in range(num_sides):
    t5.forward(side_length)
    t6.forward(side_length)
    t6.left(angle)
    t5.right(angle)
    time.sleep(1)
turtle.done()