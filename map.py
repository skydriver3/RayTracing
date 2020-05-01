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
        w,h = 200,100; cx, cy = 0, 0
        screen  = pygame.display.set_mode((600,600))
        Clock = pygame.time.Clock()
        cam = Cam.Cam((0,0,-1))
        
        bleu = (255,213,0)
        cyan = (255,159,0)
        vert_pale = (255,129,2)
        vert = (255,92,0)
        jaune = (255,64,35)
        orange = (255,43,0)
        rouge = (216,31,42)
        rouge_fonce = (202,0,42)
        rouge_fonce_1 = (161,40,48)
        rouge_fonce_2 = (94,10,11)
        rouge_fonce_3 = (0,0,0)
        rectangle =[[1, (0, 0),bleu], [2, (0, 0),bleu], [3, (0, 0),bleu], [4, (0, 0),bleu],
                    [5, (0, 0),bleu], [6, (0, 0),bleu], [7, (0, 0),bleu], [8, (0, 0),bleu],
                    [9, (0, 0),bleu]]
        rectangle1 = []
        ##pygame.event.get(); pygame.mouse.get_rel()
        ##pygame.mouse.set_visible(0); pygame.event.set_grab(1)
        
        
        
        radian = 0
                
        while True : 
            dt = Clock.tick()/6000
            radian+=dt
            for event  in pygame.event.get() : 
                if event.type == pygame.QUIT : pygame.quit();  sys.exit()
                
                #cam.events(event)
            screen.fill((000,00,000))
            
            
                
            for i in range(len(Rx)) :
                points  = []
                x, y = Rx[i][0][0], Rx[i][0][1]
                u = Rx[i][1]
                z=0
                x-=cam.pos[0]
                y-=cam.pos[1]
                z-=cam.pos[2]
                f= 20/z
                x,y = x*f,y*f
                
                if (u < -50):
                    pygame.draw.rect(screen,cyan, (cx+int(x)-1, cy+int(y)-1, f*0.15, f*0.075))
                elif (- 50 <= u < -47):
                    pygame.draw.rect(screen,vert_pale, (cx+int(x)-1, cy+int(y)-1, f*0.15, f*0.075))
                elif (- 47 <= u < -44):
                    pygame.draw.rect(screen,vert, (cx+int(x)-1, cy+int(y)-1, f*0.15, f*0.075))
                elif (- 44 <= u < -41):
                    pygame.draw.rect(screen,jaune, (cx+int(x)-1, cy+int(y)-1, f*0.15, f*0.075))
                elif (- 41 <= u < -38):
                    pygame.draw.rect(screen,orange, (cx+int(x)-1, cy+int(y)-1, f*0.15, f*0.075))
                    
                elif (- 38 <= u < -35):
                   pygame.draw.rect(screen,rouge, (cx+int(x)-1, cy+int(y)-1, f*0.15, f*0.075))
                elif (- 35 <= u < -32):
                   pygame.draw.rect(screen,rouge_fonce, (cx+int(x)-1, cy+int(y)-1,f*0.15, f*0.075))
                elif (- 32 <= u < -26):
                   pygame.draw.rect(screen,rouge_fonce_1, (cx+int(x)-1, cy+int(y)-1, f*0.15, f*0.075))
                elif (- 26 <= u < -24):
                   pygame.draw.rect(screen,rouge_fonce_2, (cx+int(x)-1, cy+int(y)-1, f*0.15, f*0.075))
                elif (-24 < u):
                   pygame.draw.rect(screen,rouge_fonce_3, (cx+int(x)-1, cy+int(y)-1, f*0.15, f*0.075))
               
                ##pygame.draw.circle(screen, (255,255,255), (cx+int(x), cy+int(y)), 1)
              
            for i in range(len(Tx)) :
                points  = []
                x, y = Tx[i][0], Tx[i][1]
                z=0
                x-=cam.pos[0]
                y-=cam.pos[1]
                z-=cam.pos[2]
                f= 20/z
                x,y = x*f,y*f
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
                    
                    
                    f= 20/z
                    x,y = x*f,y*f
                    points += [(cx+int(x), cy+int(y))]
                ##pygame.draw.line(screen, (20,150,255), points[0], points[1], 1)
            
            for i in range(len(Walls)) : 
                points  = []
                for x,y in (Walls[i][0], Walls[i][1]):
                    z=0
                    x-=cam.pos[0]
                    y-=cam.pos[1]
                    z-=cam.pos[2]
                    
                    #x,z = rotate2d((x,z), cam.rot[1])
                    #y,z = rotate2d((y,z), cam.rot[0])
                    
                    
                    f= 20/z
                    x,y = x*f,y*f
                    points += [(cx+int(x), cy+int(y))]
                pygame.draw.line(screen, (255,0,250), points[0], points[1], 4)
                
                
           
            
                       
            
            
                
            
           
            
            pygame.display.flip()
            key = pygame.key.get_pressed()
            cam.update(dt, key)
    
