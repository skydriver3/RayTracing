import pygame, sys, math
import numpy as np
import Cam

def rotate2d(pos,rad) : x, y=pos; s,c = math.sin(rad),math.cos(rad); return x*c-y*s,y*c+x*s

class map : 
    def drawing(self,listeRayon, Tx, Rx, Walls):
        pygame.init()
        listeRayon = listeRayon
        Tx = Tx
        Rx = Rx
        Walls = Walls
        print(Walls,"walls")
        w,h = 500,500; cx, cy = 490, 10
        screen  = pygame.display.set_mode((500,500))
        Clock = pygame.time.Clock()
        cam = Cam.Cam((0,0,-11))
        
        ##pygame.event.get(); pygame.mouse.get_rel()
        ##pygame.mouse.set_visible(0); pygame.event.set_grab(1)
        radian = 0
                
        while True : 
            dt = Clock.tick()/1000
            radian+=dt
            for event  in pygame.event.get() : 
                if event.type == pygame.QUIT : pygame.quit();  sys.exit()
                
                #cam.events(event)
            screen.fill((000,000,000))
            
            
           
            for i in range(len(Rx)) :
                points  = []
                x, y = Rx[i][0], Rx[i][1]
                z=0
                x-=cam.pos[0]
                y-=cam.pos[1]
                z-=cam.pos[2]
                f= 25/z
                x,y = -x*f,y*f
                points += [(cx+int(x), cy+int(y))]
                pygame.draw.circle(screen, (255,0,0), (cx+int(x), cy+int(y)), 5)
              
            for i in range(len(Tx)) :
                points  = []
                x, y = Tx[i][0], Tx[i][1]
                z=0
                x-=cam.pos[0]
                y-=cam.pos[1]
                z-=cam.pos[2]
                f= 25/z
                x,y = -x*f,y*f
                points += [(cx+int(x), cy+int(y))]
                pygame.draw.circle(screen, (0,255,0), (cx+int(x), cy+int(y)), 5)
              
            
            
            for i in range(len(listeRayon)) : 
                points  = []
                for x,y in (listeRayon[i][0], listeRayon[i][1]):
                    z=0
                    x-=cam.pos[0]
                    y-=cam.pos[1]
                    z-=cam.pos[2]
                    
                    #x,z = rotate2d((x,z), cam.rot[1])
                    #y,z = rotate2d((y,z), cam.rot[0])
                    
                    
                    f= 25/z
                    x,y = -x*f,y*f
                    points += [(cx+int(x), cy+int(y))]
                pygame.draw.line(screen, (20,150,255), points[0], points[1], 1)
            
            for i in range(len(Walls)) : 
                points  = []
                for x,y in (Walls[i][0], Walls[i][1]):
                    z=0
                    x-=cam.pos[0]
                    y-=cam.pos[1]
                    z-=cam.pos[2]
                    
                    #x,z = rotate2d((x,z), cam.rot[1])
                    #y,z = rotate2d((y,z), cam.rot[0])
                    
                    
                    f= 25/z
                    x,y = -x*f,y*f
                    points += [(cx+int(x), cy+int(y))]
                pygame.draw.line(screen, (255,0,255), points[0], points[1], 1)

            pygame.display.flip()
            key = pygame.key.get_pressed()
            cam.update(dt, key)
    