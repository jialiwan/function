import turtle
turtle.colormode(250)
bob = turtle.Turtle()

def spikeFlower(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times *36)

def spik(distance):
    for times in range (20):
        c + times *12
        bob.color (c, c, c)
        bob.width (times *2 )
        bob.forward (distance)
        bob.left(10)

def tile(c):
     polygon (4 , 200 , c)
     for times in range(23):
         polygon(3 , 50 , "blue" )
         bob.forward(100)
         polygon(3 , 50 , "blue" )
         bob.forward(100)
         polygon(3 , 50 , "blue" )
         bob.forward(100)
         polygon(3 , 50 , "blue" )
         bob.forward(100)








