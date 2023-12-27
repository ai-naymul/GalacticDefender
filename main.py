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


screen.mainloop()
