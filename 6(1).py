import turtle
t=turtle.Turtle()
t.reset()
t.seth(90)
t.width(2)
t.speed(20)
k = 10 #коэффициент для увеличения масштаба
for i in range(5):
    t.seth(0)
    t.circle(5*k,180)
    t.seth(90)
    t.circle(5*k,180)
    t.seth(180)
    t.circle(5*k,180)
    t.seth(270)
    t.circle(5*k,180)
t.penup()
for x in range(-15,6,1):
    for y in range(-5,16):
        t.goto(x*k , y*k ) 
        t.dot(5)
t.penup()  
turtle.mainloop()
