from turtle import *
#Initialize the state dictionary
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn'] / 10
    right(angle)

    #Draw first dot
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)

    #Draw second dot
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)

    #Draw third dot
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)

    update()

def animate():
    state['turn' ] += 1
    spinner()
    ontimer(animate, 20)
def flick():
    state['turn' ] += 10
#Turtle grapihics windows setup
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
# Bind the spacebar key to the flip function
onkey(flick, 'space')
listen()
animate()
done()