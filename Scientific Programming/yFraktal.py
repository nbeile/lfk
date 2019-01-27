import turtle

# creatring a turtle-object
tu = turtle.Turtle()

# hide cursor
tu.hideturtle()

# set up the window as full
turtle.setup(width=1.0, height=1.0, startx=None, starty=None)

screen_height = turtle.screensize(canvwidth=None, bg=None)
screen_height = float(screen_height[0])
print(screen_height)
tu.penup()
tu.sety(-screen_height)
tu.pendown()

# set up the pensize of 2 pixels
tu.width(2)

# adjust the turtle by turning it on 90° to the left
tu.left(90)

# turtle speed - the parameters are
'''
“fastest”: 0
“fast”: 10
“normal”: 6
“slow”: 3
“slowest”: 1
'''
tu.speed(0)

# move the turtle 100 pixels forward
tu.forward(100)

# recursive function wich creates the fractal
def tree(length):
    # check if length is not to short
    if length < 10:
        return
    else:
        tu.forward(length)
        tu.left(30)
        tree(3*length/4)
        tu.right(60)
        tree(3*length/4)
        tu.left(30)
        tu.backward(length)

# call the function with a length of 100 pixels
tree(screen_height/2)

# close the window by mouse click
turtle.Screen().exitonclick()