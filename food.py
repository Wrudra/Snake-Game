from turtle import Turtle
import random

class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    # Allows to stretch the turtle along its length and width
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # 10x10 circle
    self.color("white")
    self.speed("fastest")
    self.refresh_food()

  def refresh_food(self):     # New coordination of the food if the snake head collides with it
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    self.goto(random_x, random_y)