
from turtle import Turtle
from jumper import Jumper
from scoreboard import Text

class KeyboardTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               window,  
               straight = "Up", 
               move_right = "Right", 
               move_left = "Left",
               down = "Down",
               #speed_up = "U"
               other_player = None, walls = None,
               sb = None):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.window = window
    self.straight = straight
    self.move_right = move_right
    self.move_left = move_left
    self.down = down
    self.other_player = other_player
    self.walls = walls
    self.sb = sb
    

    #set turtle starting states
    self.shape("turtle")
    self.color("green")
    self.penup()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Sets up keyboard command examples
    self.window.onkey(self.go_right, self.move_right)
    self.window.onkey(self.go_forward, self.straight)
    self.window.onkey(self.go_left, self.move_left)
    self.window.onkey(self.go_backward, self.down)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    #sets up controlling variables (y not implemented)
    self.movement_speed = 5
    self.turn_speed = 45
    self.amount = 0
    self.collision_distance = 20
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  # Movement Methods
  def go_forward(self):
    last_position = (self.xcor(), self.ycor())
    collided = False
    self.forward(self.movement_speed)


    if self.other_player != None:
      if self.check_collision(self.other_player):
        self.amount += 1
        self.sb.clear()
        self.sb.name = str(self.amount) + " seconds on ball"
        self.sb.draw_title()


    if self.walls != None:
      for wall in self.walls:
        if self.check_wall_collision(wall):
          collided = True
          break
      if collided:
        self.goto(last_position)
        #might make this quit
    



  
       
  def go_right(self):
    last_position = (self.xcor(), self.ycor())
    collided = False
    self.sety(self.ycor()-10)
    if self.other_player != None:
      if self.check_collision(self.other_player):
        self.amount += 1
        self.sb.clear()
        self.sb.name = str(self.amount) + " seconds on ball"
        self.sb.draw_title()

    if self.walls != None:
      for wall in self.walls:
        if self.check_wall_collision(wall):
          collided = True
          break
      if collided:
        self.goto(last_position)
        #might make this quit

  def go_left(self):
    last_position = (self.xcor(), self.ycor())
    collided = False
    self.sety(self.ycor()+10)
    if self.other_player != None:
      if self.check_collision(self.other_player):
        self.amount += 1
        self.sb.clear()
        self.sb.name = str(self.amount)  + " seconds on ball"
        self.sb.draw_title()



    if self.walls != None:
      for wall in self.walls:
        if self.check_wall_collision(wall):
          collided = True
          break
      if collided:
        self.goto(last_position)
        #might make this quit
  
  def go_backward(self):
    last_position = (self.xcor(), self.ycor())
    collided = False
    self.back(self.movement_speed)
    if self.other_player != None:
      if self.check_collision(self.other_player):
        self.amount += 1
        self.sb.clear()
        self.sb.name = str(self.amount)  + " seconds on ball"
        self.sb.draw_title()


    if self.walls != None:
      for wall in self.walls:
        if self.check_wall_collision(wall):
          collided = True
          break
      if collided:
        self.goto(last_position)
        #might make this quit
 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False
  
  def check_wall_collision(self, obj_to_check):
    turtle_rad = 10
    wall_rad = 10
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < turtle_rad + (wall_rad * obj_to_check.x_size ) and distance_y < turtle_rad + (wall_rad * obj_to_check.y_size):
      return True
    else:
      return False


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check_ball_hit(self, Jumper):
  turtle_rad = 10
  jumper_rad = 10
  distance_x = self.xcor() - Jumper.xcor()
  distance_x = abs(distance_x)

  distance_y = self.ycor() - Jumper.ycor()
  distance_y = abs(distance_y)
  if distance_x < turtle_rad + (jumper_rad) and distance_y < turtle_rad + (jumper_rad):
   return True
  else:
   return False
#!!!!!!!!!!{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}