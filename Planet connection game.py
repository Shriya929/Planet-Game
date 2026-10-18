import pgzrun
import random
import time
WIDTH = 700
HEIGHT = 500


planet_List = []
planet_names = ["sun","mercury","venus","earth","mars","jupiter","saturn","uranus","neptune"]

next = 0
lines = []
start = time.time()
total = 0

for name in planet_names:
    x = random.randint(10,490)
    y = random.randint(10,390)
    p = Actor(name)
    p.x = x
    p.y = y
    planet_List.append(p)


def draw():
    global total,start,planet_List,next
    screen.blit("background",(0,0))
    for i in planet_List:
        i.draw()
    for line in lines:
        screen.draw.line(line[0],line[1],"red")
    if next < len(planet_List):
        total = time.time() - start
        screen.draw.text(str(round(total, 2)), (10, 470), color="white")
    else:
        screen.draw.text(str(round(total, 2)), (10, 470), color="white") 
    if next == len(planet_List):
        screen.draw.text("Congratulations! You connected all the planets!",center=(WIDTH / 2, HEIGHT / 2), fontsize=25,color="yellow")
def on_mouse_down(pos):
    global next, lines
    if next < len(planet_List):
        if planet_List[next].collidepoint(pos):
            if next > 0:
                lines.append((planet_List[next - 1].pos, planet_List[next].pos))
            next = next + 1
        else:
            lines = []
            next = 0
def update():
    pass
pgzrun.go()
