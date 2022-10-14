# ​SETUP
# ​Pygame ​Setup
from pygame import *
import random
init()

print("The game is about to start")
screen = display.set_mode((800, 600))
# ​Get ​the ​pics!
background_image = image.load("bg.png")
bird_image = image.load("bird.png")
pipe_image = image.load("pipe.png")
down_pipe_image = transform.flip(pipe_image, 0, 1)

# ​Set ​up ​the ​bird
bird_x = 10
bird_y = 200

# ​Set ​up ​the ​pipes

last_pipe_x = 0
pipes_info = []
for i in range(10):

    this_pipe_x = last_pipe_x +300
    pipe_y = random.randint (250,500)
    direction = random.choice (["up", "down"])
    if direction == "down":
        pipe_y = - pipe_y
    pipes_info.append([this_pipe_x, pipe_y, direction])
    last_pipe_x = this_pipe_x
    
# ​GAME ​TIME
game_mode = "playing"
while game_mode == "playing":

    # ​Moving ​the ​bird ​with ​buttons
    new_event = event.poll()
    if new_event.type == KEYDOWN:
        if new_event.key == 273:
            bird_y -= 10
       # shorter way of writing bird_y = bird_y - 1
        elif new_event.key == 274:
            bird_y += 10
        elif new_event.key == 113:
            game_mode = "not playing"
    # ​Pipe ​calculations
    new_pipes_info = []
    for pipe_x, pipe_y, direction in pipes_info:
        new_pipe_x = pipe_x - 5
        new_pipe = (new_pipe_x, pipe_y, direction)
        new_pipes_info.append(new_pipe)
    pipes_info = new_pipes_info
        # ​Show ​the ​pics!
    screen.blit(background_image, (0, 0))
    bird_object = screen.blit(bird_image, (bird_x, bird_y))
    for pipe_x, pipe_y, direction in pipes_info:
        if direction == "up":
            pipe_object = screen.blit(pipe_image, (pipe_x, pipe_y))
        elif direction == "down":
            pipe_object = screen.blit(down_pipe_image, (pipe_x, pipe_y))
            if bird_object.colliderect(pipe_object):
                game_mode = "game over"
                print("game over")
while new_event == event.poll():
  if new_event.key == 113:
    game_mode = "not playing"
    display.update()
quit()
