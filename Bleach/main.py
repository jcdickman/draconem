import pgzrun

WIDTH = 800
HEIGHT = 600



player = Actor("standing_still_1", center=(400,300))
standing_animation_list = ["standing_still_1", "standing_still_2", "standing_still_3", "standing_still_4"]
cur_standing_image = 0
delay_buffer = 0
delay_time = .10


def getStandingImage():

    return standing_animation_list[cur_standing_image]

def playerStandingStill():
    global cur_standing_image
    player.image = getStandingImage()
    cur_standing_image += 1
    if cur_standing_image >= len(standing_animation_list):
        cur_standing_image = 0




def update(dt):
    global delay_buffer
    global delay_time

    print(delay_buffer)
    if delay_buffer >= delay_time:
        delay_buffer = 0
        if keyboard.left:
            player.x -=
        elif keyboard.right:
            player.image = "run_right_1.png"
            player.x +=
        else:
            playerStandingStill()
    else:
        delay_buffer += dt



def draw():
    screen.clear()
    player.draw()



pgzrun.go()
