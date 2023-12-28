import turtle as t

screen = t.Screen()

screen.setup(width=700, height=700)
screen.bgcolor('black')
screen.title('Welcome - Galactic Defender')



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

invaders = []
bullets = []


def shoot_bullets():
    bullet = t.Turtle()
    bullet.color('yellow')
    bullet.shape('circle')
    bullet.shapesize(stretch_len=0.5, stretch_wid=0.4)
    bullet.penup()
    bullet.speed(0)
    bullet.goto(spaceship.xcor(), spaceship.ycor())
    bullet.setheading(90)
    bullets.append(bullet)




for row in range(3):
    for col in range(5):
        invader = t.Turtle()
        invader.shape('square')
        invader.color('white')
        invader.shapesize(stretch_len=1, stretch_wid=0.4)
        invader.penup()
        invader.speed(0)
        x = -200 + col * 100
        y = 200 - row * 50
        invader.goto(x,y)
        invaders.append(invader)



screen.listen()
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')
screen.onkey(shoot_bullets, 'space')


invader_speed = 4
bullet_speed = 10
while True:
    for invader in invaders:
        x = invader.xcor()
        x += invader_speed
        invader.setx(x=x)

        if invader.xcor() > 390 or invader.xcor() < -390:
            for invader in invaders:
                y = invader.ycor()
                y -= 40
                invader.sety(y)
            invader_speed *= -1
        for bullet in bullets:
            y = bullet.ycor()
            y += bullet_speed
            bullet.sety(y)

            if y > 290:
                bullet.hideturtle()
                bullets.remove(bullet)
        for bullet in bullets:
            if bullet.distance(invader) < 15:
                invader.hideturtle()
                invaders.remove(invader)
                bullet.hideturtle()
                bullets.remove(bullet)
        
   

    screen.update()










