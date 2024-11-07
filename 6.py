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



#####################
from turtle import *

t = Turtle()
t.speed(0)
t.tracer()
k = 23
t.left(180)
t.forward(5*k)
t.right(90)
for i in range(4):
    t.forward(14 * k)
    t.right(120)

t.right(30)

t.pu()

for x in range(-k/2, k):
    for y in range(-k/2, k):
        t.goto(x * k, y * k)
        t.dot(1)

done()
