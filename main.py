import turtle as t

screen = t.Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')




spaceship = t.Turtle()
spaceship.shape('triangle')
spaceship.color('white')
spaceship.penup()
spaceship.left(90)
spaceship.goto(0,-250)



def move_left():
    x = spaceship.xcor()
    x -= 20
    spaceship.setx(x)


def move_right():
    x = spaceship.xcor()
    x += 20
    spaceship.setx(x)



screen.listen()
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')











screen.mainloop()
