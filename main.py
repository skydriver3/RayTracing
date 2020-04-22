import Antenna 
import Wall 
import Space 
import Ray 
from pygame.locals import * 

if __name__ == "__main__" : 
    Walls = [Wall.wall(20, 1, 1, 1, (0, 300), (0, 0))] 
    Tx = [Antenna.Antenna((150, 0), 100, [])] 
    Rx = [Antenna.Antenna((150, 300), 0, [])] 

    env = Space.Space(Walls, Tx, Rx)
    rays = env.Predict(2)
    env.Draw(rays) 

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:

                sys.exit(0)

