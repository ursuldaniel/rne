from turtle import *
tracer(0)

left(90)
k = 20
for i in range(4):
    # right(60)
    forward(12 * k)
    right(90)
    # forward(2 * k)
    # right(270)

right(30)

for i in range(3):
    forward(8 * k)
    right(60)
    forward(8 * k)
    right(120)


for i in range(4):
    forward(8 * k)
    right(60)
    forward(8 * k)
    right(120)

for i in range(3):
    forward(8 * k)
    right(60)
    forward(8 * k)
    right(120)


pu()

for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)

done()