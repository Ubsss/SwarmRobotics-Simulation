import random
import time

# Import the Turtle module
import turtle

# Required by MacOSX to show the window
turtle.fd(0)

# Set the animations speed to the maximum
turtle.speed(0)

# Change the background color
turtle.bgcolor("white")

# Change the window title
turtle.title("Swarm Simulation using Python Turtle Library")

# Hide the default turtle
turtle.ht()

# This saves memory
turtle.setundobuffer(1)

# This speeds up drawing
turtle.tracer(0)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        numb = random.randrange(0, 360, 1)

        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(numb)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(numb)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(numb)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(numb)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 1)) and \
                (self.xcor() <= (other.xcor() + 1)) and \
                (self.ycor() >= (other.ycor() - 1)) and \
                (self.ycor() <= (other.ycor() + 1)):
            return True
        else:
            return False


class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 4

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4

    def forward(self, distance):
        self.fd(self.speed)


class Target(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)


class Game():
    def __init__(self):

        self.feature = "Swarm Demo"
        self.state = "playing"
        self.pen = turtle.Turtle()

    def draw_border(self):
        # Draw border
        self.pen.speed(0)
        self.pen.color("black")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def draw_line(self):
        # Draw line for bots to follow
        self.pen.speed(0)
        self.pen.color("red")
        self.pen.pensize(6)
        self.pen.penup()
        self.pen.goto(-230, 230)
        self.pen.pendown()
        for line in range(4):
            self.pen.fd(400)
            self.pen.rt(90)

        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "Simulation goal: Bots follow a red line on screen"
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))

    def end_simulation(self):
        turtle.bye()


class BotModes():
    def __init__(self):
        self.bot_mode = ""
        self.bot_mode_objective = ""

    def follow_the_master(self, main_bot, follower):
        follower.setheading(follower.towards(main_bot))
        follower.forward(4)

    # Create actual function for this!!
    def follow_the_line(self, bot):
        pass


# Create game object
game = Game()

# create the bots mode object
mode = BotModes()

# Draw the game border
game.draw_border()

# Show the game status
game.show_status()

# draw the line for the bots to follow
game.draw_line()

# Create my sprites
player = Player("triangle", "blue", -230, 230)

# create points on screen
point_a = Target("square", "red", -230, 230)
point_a.ht()

point_b = Target("square", "red", 170, 230)
point_b.ht()

point_c = Target("square", "red", 170, -170)
point_c.ht()

point_d = Target("square", "red", -230, -170)
point_d.ht()

# Create 6 enemies in random locations on the screen
enemies = []
for i in range (6):
    x = random.randrange(-290, 290, 1)
    y = random.randrange(-290, 290, 1)
    enemy = Enemy("circle", "blue", y, x)
    enemies.append(enemy)

# Keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(game.end_simulation, "q")
turtle.listen()

# Main game loop
while True:
    turtle.update()
    time.sleep(0.02)
    player.move()

    if player.is_collision(point_a):
        player.setheading(player.towards(point_b))
    elif player.is_collision(point_b):
        player.setheading(player.towards(point_c))
    elif player.is_collision(point_c):
        player.setheading(player.towards(point_d))
    elif player.is_collision(point_d):
        player.setheading(player.towards(point_a))

    for enemy in enemies:
         mode.follow_the_master(player, enemy)

turtle.mainloop()