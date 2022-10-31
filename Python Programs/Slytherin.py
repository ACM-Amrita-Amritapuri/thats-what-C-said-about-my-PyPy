import pygame
import time
import random

pygame.init()
win_l=600
win_b=800

red = (200,0,0)
light_red = (255,0,0)

yello = (200,200,0)
light_yello = (255,255,0)

green = (34,177,36)
light_green = (0,255,0)

black = (0,0,0)
white = (255,255,255)

win=pygame.display.set_mode((win_b,win_l))
pygame.display.set_caption("Slytherin")

img = pygame.image.load('Snakehead.png')
appleimg= pygame.image.load('frog.png')
icon=pygame.image.load('icon.png')

eat=pygame.mixer.Sound("Eat.wav")
colide=pygame.mixer.Sound("colide.wav")

pygame.display.set_icon(icon)
clock = pygame.time.Clock()

scrsurf=40

FPS=12
pause=True

AppleThickness = 20

smallfont= pygame.font.SysFont("comicsansms", 20)
midfont= pygame.font.SysFont("comicsansms", 30)
largefont= pygame.font.SysFont("comicsansms", 80)

direction = "right"
    

def snake(Block_side, snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = pygame.transform.rotate(img,0)
    if direction == "down":
        head = pygame.transform.rotate(img,180)
    win.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(win, (155,0,185), [XnY[0], XnY[1], Block_side,Block_side])
        
def randApple():
     randappleX = round(random.randrange(0+scrsurf,win_b-AppleThickness)/20.0)*20.0
     randappleY = round(random.randrange(0+scrsurf,(win_l-(AppleThickness+scrsurf)))/20.0)*20.0
     return  randappleX, randappleY

def Text_Object (text,colour,size):
    if size == "small":
        text_surface = smallfont.render(text,True,colour)
    if size == "medium":
        text_surface = midfont.render(text,True,colour)
    if size == "large":
        text_surface = largefont.render(text,True,colour)
    return text_surface, text_surface.get_rect()

def massage_to_button (msg,colour,buttonX,buttonY,button_b,button_l,size="small"):
    textsurf, text_rect = Text_Object(msg,colour,size)
    text_rect.center= (buttonX+(button_b/2) , buttonY+(button_l/2))
    win.blit(textsurf,text_rect)
def gameControl ():
    gameC=True
    
    while gameC:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        win.fill(white)
        massage_to_screen("Controls",(0,0,255),-100,"large")
        massage_to_screen("Move: w,a,s,d or num8,num4,num2,num6",black,0,"small")
        massage_to_screen("Pause: Space",black,25,"small")
        
        
        button("BACK",0,0,120,50,yello,light_yello,"back")
        button("1",150,450,100,50,light_green,light_red,"1")
        button("2",250,450,100,50,green,light_red,"2")
        button("3",350,450,100,50,light_yello,light_red,"3")
        button("4",450,450,100,50,yello,light_red,"4")
        button("5",550,450,100,50,red,light_red,"5")
        
        pygame.display.update()
        clock.tick(FPS)
        
def button (text, x, y, length, breath,ina_clr,a_clr,action):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    global pause
    global FPS
    if x+length > cur[0] > x and y < cur[1] < y+breath:
        pygame.draw.rect(win,a_clr,(x,y,length,breath))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "play":
                GameLoop(3)
            if action == "PLAY":
                pause=False
            if action == "controls":
                gameControl()
            if action == "back":
                Start_screen()
            if action == "1":
                FPS=8
                GameLoop(1)
            if action == "2":
                FPS=10
                GameLoop(2)
            if action == "3":
                FPS=12
                GameLoop(3)
            if action == "4":
                FPS=14
                GameLoop(4)
            if action == "5":
                FPS=16 
                GameLoop(5)
    else:
        pygame.draw.rect(win,ina_clr,(x,y,length,breath))
        
    massage_to_button(text,black,x,y,length,breath)

def massage_to_screen (msg,colour,y_displace=0,size="small"):
    textsurf, text_rect = Text_Object(msg,colour,size)
    '''screen_text = font.render(msg,True,colour)
    win.blit(screen_text,[win_b/2 , win_l/2])'''
    text_rect.center= (win_b/2) , (win_l/2)+y_displace
    win.blit(textsurf,text_rect)

def Start_screen():
    intro=True
    
    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        win.fill(white)
        massage_to_screen("Slytherin",(25,0,155),-100,"large")
        
        button("PLAY",150,350,100,50,green,light_green,"play")
        button("CONTROLS",350,350,120,50,yello,light_yello,"controls")
        button("QUIT",570,350,100,50,red,light_red,"quit")
        
        pygame.display.update()
        clock.tick(FPS)

def pause():
    
    global pause
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        massage_to_screen("PAUSED",black,-100,"large")
        
        button("PLAY",150,350,100,50,green,light_green,"PLAY")
        button("CONTROLS",350,350,120,50,yello,light_yello,"controls")
        button("QUIT",570,350,100,50,red,light_red,"quit") 
        pygame.display.update()         
   
    pygame.display.update()
    clock.tick(15)
        

def score(score):
    win.fill((0,0,0),rect=[0,0,win_b,40])
    text = midfont.render("Score: "+str(score),True,(255,255,255))
    win.blit(text,[0,0])
    
def GameLoop (point):
    global direction
    #global life
    Lead_x=win_b/2
    Lead_y=win_l/2
    
    snakeList = []
    snakeLength = 1
    
    Lead_x_change=0
    Lead_y_change=0
    
    Block_side=20
    velocity=20
    
    randappleX , randappleY= randApple()
    
    
    GameExit=False
    GameOver=False
    
   
    
    while not GameExit:
        
        while GameOver:
            
            
            massage_to_screen("Game Over",(255,0,0),-55,"large")
            button("PLAY",150,350,100,50,green,light_green,"play")
            button("CONTROLS",350,350,120,50,yello,light_yello,"controls")
            button("QUIT",570,350,100,50,red,light_red,"quit")
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                     quit()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and direction != "right" or event.key == pygame.K_KP4 and direction != "right":
                    direction = "left"
                    Lead_x_change = -velocity
                    Lead_y_change = 0
                elif event.key == pygame.K_d and direction != "left" or event.key == pygame.K_KP6 and direction != "left":
                    direction = "right"
                    Lead_x_change = velocity
                    Lead_y_change = 0
                elif event.key == pygame.K_w and direction != "down" or event.key == pygame.K_KP8 and direction != "down":
                    direction = "up"
                    Lead_y_change = -velocity
                    Lead_x_change = 0
                elif event.key == pygame.K_s and direction != "up" or event.key == pygame.K_KP2 and direction != "up":
                    direction = "down"
                    Lead_y_change = velocity
                    Lead_x_change = 0
                    
                elif event.key == pygame.K_SPACE:
                    pause()
                    
        if Lead_x >= win_b-Block_side or Lead_x <0 or Lead_y > win_l-Block_side or Lead_y < scrsurf:
            pygame.mixer.Sound.play(colide)
            time.sleep(0.3)
            GameOver=True
           
        
        Lead_x += Lead_x_change
        Lead_y += Lead_y_change
        
        win.fill((255,255,255 ))
        win.blit(appleimg,(randappleX,randappleY))
        snakeHead = []
        snakeHead.append(Lead_x)
        snakeHead.append(Lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]
            
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                GameOver = True
                
        snake(Block_side, snakeList)
        score((snakeLength-1)*point)
        pygame.display.update()  
       
            
        if Lead_x > randappleX and Lead_x <= randappleX + AppleThickness or Lead_x + Block_side > randappleX and Lead_x + Block_side <= randappleX + AppleThickness: #or Lead_x  < randappleX and Lead_x + Block_side > randappleX + AppleThickness:# and Lead_x < randappleX + AppleThickness:
            if Lead_y > randappleY and Lead_y <= randappleY + AppleThickness:
                pygame.mixer.Sound.play(eat)
                randappleX , randappleY= randApple()
                snakeLength +=1
            elif  Lead_y + Block_side > randappleY and Lead_y + Block_side <= randappleY + AppleThickness:# or Lead_y + Block_side > randappleY and Lead_y + Block_side < randappleY + AppleThickness:
                pygame.mixer.Sound.play(eat)
                randappleX , randappleY= randApple()
                snakeLength +=1
            elif  Lead_y > randappleY and Lead_y <= randappleY + AppleThickness:
                pygame.mixer.Sound.play(eat)
                randappleX , randappleY= randApple()
                snakeLength +=1
                    
        clock.tick(FPS) 
        
    pygame.quit()
    quit()

Start_screen()   
