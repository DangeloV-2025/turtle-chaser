from turtle import Turtle

from random import randint

class Jumper (Turtle):
  def __init__(self, starting_x, starting_y):
    Turtle.__init__(self)
    self.starting_x = starting_x
    self.starting_y = starting_y
    
    starting_x = 10
    starting_y = 10
  

    self.color("blue")
    self.penup()
    self.shape("circle")
    self.random_location()
  
  def random_location(self):
    
    x = randint(-295, 295)
    while x in [-220, -100, 0, 100, 220]:
      x = randint(-295, 295)

        
    
    y = randint(-245, 240)
    while y  in [-175, -100, 0, 100, 175]:
      y = randint(-245, 240)

        
    self.goto(x, y)
          
          