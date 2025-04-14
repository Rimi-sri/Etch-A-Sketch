from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(100)
def move_backwards():
    tim.backward(100)
def move_counter_clockwise():
   new_heading = tim.heading() + 10
   tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s",fun= move_backwards)
screen.onkey(key="a",fun = move_counter_clockwise)
screen.onkey(key="d", fun= clockwise)
screen.onkey(key="c",fun=clear_screen)
screen.exitonclick()
