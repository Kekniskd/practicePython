import turtle

wn = turtle.Screen()
tr = turtle.Turtle()

def star(tr):
    for _ in range(5):
        tr.backward(100)
        tr.right(-144)

star(tr)

wn.mainloop()