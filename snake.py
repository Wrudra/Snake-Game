from turtle import Turtle
# Creating a snake body having 3 pieces from the start (each segment 20x20)
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

  def __init__(self):
    self.segments = [] 
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POSITION:      # Create Snake
      self.add_segment(position)
  
  def add_segment(self, position):
    new_segment = Turtle(shape="square")
    new_segment.color("White")
    new_segment.penup()     # Telling each turtles not to make a line
    new_segment.goto(position)
    self.segments.append(new_segment)
  
  # Adding a new segment to the snake
  def extend(self):
    self.add_segment(self.segments[-1].position())     # Lists -1 represents the last item in python

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):      # source, destination, increment
      new_x = self.segments[seg_num - 1].xcor()      # e.g. Extracting 2nd segs X-coordinate 
      new_y = self.segments[seg_num - 1].ycor()      # e.g. Extracting 2nd segs y-coordinate
      self.segments[seg_num].goto(new_x, new_y)      # e.g. 3rd seg will go to the 2nd segs position
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:     # Extracting snakes head position 
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP: 
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
