import Antenna 
import Wall 
import Space 
import Ray 
import numpy as np
import Line

if __name__ == "__main__" : 
    Walls = [  
        Wall.wall(20, 1, 1, 1, np.array([100, 0]), np.array([100, 300])), 
        Wall.wall(20, 1, 1, 1, np.array([250, 0]), np.array([250, 300]))]
        #Wall.wall(20, 1, 1, 1, np.array([300, 200]), np.array([250, 300]))] 
    Tx = [Antenna.Antenna(np.array([150, 100]), 100, [])] 
    Rx = [Antenna.Antenna(np.array([150, 200]), 0, [])] 

    env = Space.Space(Walls, Tx, Rx)
    rays = env.Predict(4)
    env.Draw(rays) 



