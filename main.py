from turtle import Screen, ontimer
import time 
from moving_turtle import KeyboardTurtle
from wall import Wall
from jumper import Jumper
from scoreboard import *



speed_of_ball = input("what difficulty level do you want" + 
"Easy: 5 difficult: 3 Impossible: 1")
ball_speed = speed_of_ball
if (speed_of_ball == "1"):
  ball_speed = 1
elif (speed_of_ball == "3"):
  ball_speed = 3
elif (speed_of_ball == "5"):
  ball_speed = 5

def set_timer(run_time):
  global timer_running, end_time
  timer_running = True
  start_time = time.time()
  end_time = start_time + run_time

def check_timer():
  global timer_running, end_time, ball_speed
  if timer_running:
    if (time.time() >= end_time):
      timer_running = False
      mick.random_location()
      set_timer(ball_speed)
      #change this


# set up instance of the screen
window = Screen()
window.bgcolor("grey")
screen_width = 600
screen_height = 500
window.setup(screen_width, screen_height)

timer_running = False
end_time = 0 

wall_list = []
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check_ball_hit(KeyboardTurtle, Jumper):
  turtle_rad = 10
  jumper_rad = 10
  distance_x = mick.xcor() - greg.xcor()
  distance_x = abs(distance_x)

  distance_y = mick.ycor() - greg.ycor()
  distance_y = abs(distance_y)
  if distance_x < turtle_rad + (jumper_rad) and distance_y < turtle_rad + (jumper_rad):
   return True
  else:
   return False
#!!!!!!!!!!{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
#set up player
mick = Jumper(10, 10)
set_timer(ball_speed)
greg = KeyboardTurtle(window, "d", "s", "w", "a", walls=wall_list, other_player=mick)
sally = Text()
greg.sb = sally 
def check_mick():
  check_timer()
  check_ball_hit(greg, mick)
  ontimer(check_mick, ball_speed)
  


greg.shape("circle")
greg.color("red")
greg.goto(0, 0)

#center
wall_list.append(Wall(100, 0, 1, 5))
wall_list.append(Wall(0, 100, 5, 1))
wall_list.append(Wall(0, -100, 5, 1))
wall_list.append(Wall(-100, 0, 1, 5))
#border
wall_list.append(Wall(-300, 0, 1, 40))
wall_list.append(Wall(300, 0, 1, 40))
wall_list.append(Wall(0, 250, 40, 1))
wall_list.append(Wall(0, -250, 40, 1))
# 2nd center
wall_list.append(Wall(-220, 0, 1, 16))
wall_list.append(Wall(220, 0, 1, 16))
wall_list.append(Wall(0, 175, 16, 1))
wall_list.append(Wall(0, -175, 16, 1))



# set target of other player(our collison check) to the opposite player
check_mick()
# This is needed to listen for inputs
window.listen()
window.mainloop()



