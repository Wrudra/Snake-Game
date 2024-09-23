from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen setup
screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)      # When tracer is off (0), screen.update() can be used for animation
scoreboard = ScoreBoard()

# Creating the snake
snake = Snake()

# Creating the food
food = Food()

# Commanding the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Moving the snake 
game_is_on = True
while game_is_on:
  screen.update()     # To tell our program when to refresh and redraw the screen, basically we update the screen once all of the segments have moved forwards.
  time.sleep(0.3)     # N sec delay after each segment is moved
  snake.move()      # Calling the snake to move

  # Detect collision with food
  # It can be (x,y) or an instance, e.g. distance between 2 turtles
  if snake.head.distance(food) < 15:    # If the snake head is  within 15 pixels of the food or closer
    food.refresh_food()
    snake.extend()      # Extend the snake when it gets food
    # Score board
    scoreboard.increase_score()

  # Detect Collision with wall
  if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
    game_is_on = False
    scoreboard.game_over()

  # Detect Collision with tail
  for segment in snake.segments[1:]: # Head itself is ignored using 'Slicing'
    if snake.head.distance(segment) < 10:   # Comparing heads distance with other segments
      game_is_on = False
      scoreboard.game_over()

screen.exitonclick()