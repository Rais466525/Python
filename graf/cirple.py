from turtle import *
t = Turtle
t.screen.setup(800, 800)
def circ(d, r, rBig):
   for i in range(d):
      t.circle(rBig)
      t.dot(r, "red")
t.up()
t.goto(350, 0)
t.down()
circ(45, 10, 200)
t.screen.exitonclick()
t.screen.mainloop()