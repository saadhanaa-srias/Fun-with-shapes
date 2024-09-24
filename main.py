import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red','yellow'] 
s.bgcolor('grey') 
t.speed('fastest')
t.hideturtle()
turtle.title("simple shape")

while True:
  for x in range(20,10,-5):
    t.pencolor('red') 
    t.width(x/2.5 + 8)
    t.forward(x)
    t.left(50)
    t.pendown()
    for x in range(16):
      t.pencolor('orange')
      t.forward(90)
      t.left(90)
      x =  x+2
    for x in range(16):
      t.pencolor(colors[x%len(colors)])
      t.width(x/10 + 1)
      t.forward(x) 
      t.left(19)
      t.right(39)  
    turtle.done()