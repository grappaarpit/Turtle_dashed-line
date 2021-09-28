import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

########### Challenge 2 - Draw a Dashed Line ########
for i in range (0,10):
  tim.forward(10)
  tim.penup()
  tim.forward(10)
  tim.pendown()

