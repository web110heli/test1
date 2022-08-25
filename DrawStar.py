import turtle
def star(len,color="red",startangle=0,x=0,y=0):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(startangle)
    for i in range(5):
        turtle.forward(len)
        turtle.right(144)
    turtle.end_fill()
    turtle.hideturtle()

if __name__=='__main__':
    star(100,"yellow",30,-100,100)
    turtle.done()
