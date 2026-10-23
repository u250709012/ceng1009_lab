import turtle

# --setup--
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

# --functions--

def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)

def drawSpiral(someturtle, angel):
    size = 1
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angel)
        size = size + 2

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)

def drawStar(someturtle, size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)

def drawSprite(someturtle, legs, length):
    angle = 360 / legs
    for i in range(legs):
        someturtle.forward(length)
        someturtle.backward(length)
        someturtle.left(angle)



# --exercise--

# --exercise 1--
# tess.pencolor("hotpink")
# tess.pensize(3)
# drawPoly(tess, 8, 50)

#--exercise 2--
# tess.pencolor("blue")
# tess.pensize(2)
# for i in range(20):
#     drawPoly(tess, 4, 100)
#     tess.left(18)

#--exercise 3--
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-100, 0)
# tess.pendown()
# drawSpiral(tess, 90)
#
# tess.penup()
# tess.goto(150, 0)
# tess.pendown()
# drawSpiral(tess, 91)

#--exercise 4--
# drawEquitriangle(tess, 100)

#--exercise 5--
# tess.pencolor("hotpink")
# tess.pensize(5)
# for i in range(5):
#     drawStar(tess, 50)
#     tess.penup()
#     tess.forward(200)
#     tess.right(144)
#     tess.pendown()

#--exercise 6--
drawSprite(tess,15, 150)







#--finish--
wn.exitonclick()









