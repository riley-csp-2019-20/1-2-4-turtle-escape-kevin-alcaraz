#importing tutle 
import turtle as trtl
juan = trtl.Turtle()
player = trtl.Turtle()
import random 


#================variables===============
juan.color("blue")
numwalls=30
walldist=600
wall_width = 20
door_width = 40

#===============setup===================

juan.speed(0)
juan.pensize(5)
juan.ht()
juan.penup()
juan.goto(300,300)
juan.right(90)
juan.pendown()
juan.ht()
player.speed(0)
#================code====================

def draw_barrier():
    juan.right(90)
    juan.forward(door_width)
    juan.backward(door_width)
    juan.left(90)


def draw_door():
    juan.penup()
    juan.forward(door_width)
    juan.pendown()

def up():
    player.setheading(90)
    player.forward(10)

def left():
    player.setheading(180)
    player.forward(10)
def down():
    player.setheading(270)
    player.forward(10)

def right():
    player.setheading(0)
    player.forward(10)
#===============code====================



for i in range(numwalls):
    if i < numwalls - 5:
        door = random.randint(door_width, walldist- door_width)

        barrier =  random.randint(2 * wall_width, walldist - 2 * door_width)

        if door < barrier:
            juan.forward(door)
            draw_door()
            juan.forward(barrier - door  - door_width)
            draw_barrier()
            juan.forward(walldist - barrier)

        else:
            juan.forward(barrier)
            draw_barrier()
            juan.forward(door - barrier)
            draw_door()
            juan.forward(walldist - door - door_width)


    juan.right(90)
    walldist = walldist - wall_width



wn = trtl.Screen()
wn.onkeypress(up,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.listen()

wn.mainloop()