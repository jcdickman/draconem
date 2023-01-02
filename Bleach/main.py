import pgzrun

WIDTH = 800
HEIGHT = 600

player = Actor("standing_still_1", center=(400,300))


#def update():


def draw():
    player.draw()



pgzrun.go()
