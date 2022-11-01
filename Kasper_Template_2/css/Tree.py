import turtle as t

t.speed(1)
t.pensize(2)
t.left(90)
t.forward(100)
t.color("black")


def draw(l):
    if(l < 10):
        return
    else:
        t.forward(l)
        t.color("red")
        t.circle(2)
        t.color("black")
        t.left(30)
        draw(l/4)
        t.right(60)
        draw(l/4)
        t.left(30)
        t.backward(l)


draw('l')
