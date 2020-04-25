import Ray
import Antenna 
import Wall
from typing import List
import pickle 
import pygame 
import main 

class Space : 
    def __init__(self, Walls : List[Wall.wall], Tx : List[Antenna.Antenna], Rx : List[Antenna.Antenna]) : 
        self.Walls = Walls 
        self.Tx = Tx 
        self.Rx = Rx 
        pygame.init()
        self.canvas = pygame.display.set_mode((1000, 1000))
        self.canvas.fill((49,150,100))
        pygame.display.flip()
    
    def CreateImageFor_AllWalls(self, transmitter : Antenna.Antenna) : 
        Images = [] 
        for w in self.Walls : 
            if (transmitter.Wall != w ) : 
                Images.append(transmitter.CreateImage(w))
        
        return Images

    def CreateImagesFor_AllTx_AllWalls(self, Transmitters : List[Antenna.Antenna]) :
        Images = [] 
        for t in Transmitters : 
            Images.extend(self.CreateImageFor_AllWalls(t)) 
        
        return Images

    def Predict(self, Reflexions) : 
        transmitters = self.Tx
        trajectories = [] 
        for _ in range(Reflexions) : 
            print("\n\nlevel of relfection : " + str(_) + "\n################\n")
            for t in transmitters : 
                myfont = pygame.font.SysFont("Comic Sans MS", 7)
                label = myfont.render(f"({int(t._pos[0])}, {int(t._pos[1])} ) ", 1, (0, 0, 255))
                self.canvas.blit(label, (int(t._pos[0]), int(t._pos[1])))
                pygame.draw.circle(self.canvas, (0, 0, 255), (int(t._pos[0]), int(t._pos[1])), 2)
                for r in self.Rx : 
                    ray = t.Propagate(r._pos, self.Walls)
                    if ray != None : 
                        print(f"\n adding a ray #############\n")
                        r.rays.append(ray) 
                        ray.draw(self.canvas)  
                        main.wait()                      
            transmitters = self.CreateImagesFor_AllTx_AllWalls(transmitters)


    def Draw(self): 
        for w in self.Walls : 
            w.draw(self.canvas) 
        pygame.display.flip()

    def Save(self): 
        pickle_out = open("save.pickle", "wb") 
        pickle.dump(self, pickle_out) 
        pickle_out.close() 

        

    

    

