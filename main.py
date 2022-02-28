import turtle as t
o = t.Turtle()
num_of_sides = 8
for  po in range(num_of_sides):
    for _ in range(num_of_sides):
        angle = 360 / num_of_sides
        o.forward(100)
        o.right(angle)
    num_of_sides-=1
