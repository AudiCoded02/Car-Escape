from pygame import *
from math import *
from random import *
from tkinter import *

init()
root=Tk()
root.withdraw()

font.init()
timesFont=font.SysFont("Times New Roman",20)#Font for regular text
timeFont=font.SysFont("Times New Roman",50)#Font for title of game
size=width,height=800,600#Size
screen=display.set_mode(size)#Setting the screen
RED=(255,0,0)   #RED colour
GREEN=(0,255,0) #Green Colour
BLUE=(0,0,255) #Blue Colour
BLACK=(0,0,0) #Black Colour
WHITE=(255,255,255) #White Colour
rapid=20 

#######Opening all images (LEVEL 1)
carPic=image.load("Characters and Items/Car.png").convert_alpha()#for player
player_Car=transform.scale(carPic,(310,169))
backPic=image.load("Background for Game Levels/Road1.png").convert()#road background
backPic2=image.load("Background for Game Levels/Road2.png").convert()
road=transform.scale(backPic, (10000,700))
road2=transform.scale(backPic, (10000,700))
thug_carPic=image.load("Characters and Items/thugCar.png").convert_alpha()#enemies
thug_Car=transform.scale(thug_carPic,(345,165))
gunPic=image.load("Characters and Items/pistol.png")#pistol for player
pistol=transform.scale(gunPic, (30,50))
pbPic=image.load("Characters and Items/player_bullets.png").convert_alpha()#bullets for player's gun
player_Bullets=transform.scale(pbPic, (10,10))
playerB=transform.rotate(player_Bullets,-90)
menuPic=image.load("Background for Game Levels/menu.jpg")#background for menu
start=transform.scale(menuPic, (800,600))
lmgPic=image.load("Characters and Items/lmg.png")#gun for enemies
lm=transform.scale(lmgPic, (129,50))
lmg=transform.rotate(lm,180)
tbPic=image.load("Characters and Items/thug_bullets.png")#bullets for enemies gun
thug_bullet=transform.scale(tbPic,(25,25))
thugB=transform.rotate(thug_bullet,90)

arrowPic=image.load("Characters and Items/arrow.png")#arrow for navigation
arrow=transform.scale(arrowPic,(100,40))
leftArrow=transform.rotate(arrow,180)

storyPic=image.load("Story.jpg")#Story image
storys=transform.scale(storyPic, (800,600))
instPic=image.load("First Level Instructions.jpg")#First level instructions
firstInstructions=transform.scale(instPic, (800,600))
instPic2=image.load("Second Level Instructions.jpg")#second level instructions
secondInstructions=transform.scale(instPic2, (800,600))
credPic=image.load("Credits.jpg")#credits image
cred=transform.scale(credPic, (800,600))
storySecondPic=image.load("Second Level Story.jpg")#Second Level Story image
storys2nd=transform.scale(storySecondPic, (800,600))
congratsPic=image.load("Congratulate.jpg")#Winning game image
congrats=transform.scale(congratsPic,(800,600))

#######for level 2
mazePic=image.load("Background for Game Levels/Maze.bmp")#maze for 2nd level
maze=transform.scale(mazePic, (500,500))
car=transform.rotate(player_Car,-90)#changing size of player for 2nd level
car_Player=transform.scale(car,(15,20))

#screen.blit(carTransformed, (200,300))

#####
player=[20,275,0]#position for player
X=0
Y=1
VY=2#not needed
#thugs1=[[randint(900,5000000),randint(0,2),0] for i in range(200)]

thugs=[]#list for enemies
#adding enemies to list if they're not colliding
while True:
    rx=randint(900,50000)
    ry=randint(0,2)

    #newrect=Rect(rx,0,345,165)
    check=0
    for t in thugs:
    
        #thugrect=Rect(t[0],0,345,165)
        #if newrect.colliderect(thugrect):
        if abs(t[0]-rx)<750:
            check=1
            #print(t[0],rx)
    if check==0:
        thugs.append([rx,ry])
    if len(thugs)>=20:
        break


        
        
        


#thugs=[[1200,0,0],[1700,0,0],[3400,0,0]]
#thugs=[]


speed=5#how fast road is going
X1=0
Y1=1
VY1=2

r1 = [-1024,0,1024]#position for road
r2=[0,0,1024]#position for other road
XX=0
YY=1
H=2
playerBullets=[]#list for player bullets
thugBullets=[]#list for enemies bullets

p=[24,7,0]#position for player 2nd level

ammo=50#ammo
thug=20# # of enemies
damage=0#damage 
#######text
#for beating game already
beatText="You Have Already Beaten The Game"
beatPic=timesFont.render(beatText,TRUE,WHITE)
#For losing game
overText="GAME OVER, YOU LOST"
overPic=timeFont.render(overText,TRUE,WHITE)
#for ammo remaining on gun
ammoText="Ammo: "
ammoCount=str(ammo)
ammoPic=timesFont.render(ammoText+ammoCount+"/50",TRUE,BLACK)
#how many thugs are left
thugText="Thugs Remaining: "
thugsCount=str(thug)
thugsPic=timesFont.render(thugText+thugsCount+"/20",TRUE,BLACK)
#damage taken
damageText="% Damage"
damageCount=str(damage)
damagePic=timesFont.render(damageCount+damageText,TRUE,BLACK)
#title for game
titleText="Car Escape"
titlePic=timeFont.render(titleText,TRUE,WHITE)


#different pages
different_pages=["Play","Second Level","Instructions","Credits","Story"]
storyText=different_pages[4]
creditsText=different_pages[3]
instructionsText=different_pages[2]
secondText=different_pages[1]
firstText=different_pages[0]

storyPic=timesFont.render(storyText,TRUE,WHITE)
creditsPic=timesFont.render(creditsText,TRUE,WHITE)
instructionsPic=timesFont.render(instructionsText,TRUE,WHITE)
secondPic=timesFont.render(secondText,TRUE,BLACK)
firstPic=timesFont.render(firstText,TRUE,WHITE)

aaa=0

game1=True#game 1st level if running
game2=True#game 2nd level if running

def game():#the first level of game
    
    running=True
    global ammo,aaa
    offset=200-player[X]

    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        if ammo==0:#if ammo reaches 0
            running=False
            game1=False
            return "Game Over"
        
        
            
        if damage>=100:#if damage reaches or is above 100%
            running=False
            game1=False
            return "Game Over"
            
        
        #Calling function for first level
        movePlayer(player)
        bullets()
        moveThugs(thugs)
        drawScene1st(screen,player,thugs,playerBullets)
        checkCollision(playerBullets,thugs)
        enemyCheckCollision(thugBullets)
        aaa+=1
        if aaa%60==0: #only call out bullets if even number
            enemyBullets()
        

        #how road is moving
        r1[XX]+=speed
        if r1[XX]+speed < r1[H]: 
            r1[XX] = -r2[H]
        r2[XX] = r2[XX]+speed 
        if r2[XX] +speed > r2[H]:
            r2[XX] = -r1[H]

        #if number of enemies is 0
        if len(thugs)==0:
            running=False
            game1=False
            return "Second Story"
        
        
    return "exit"


#The first level of the game where car is moving along road
def drawScene1st(screen,player,thugs,playerBullets): #showing the stuff for first level
    
    offset=20-player[X]
    #for player and roads
    screen.blit(road,(r1[XX],0))
    screen.blit(road2,(r2[XX],0))
    screen.blit(player_Car,(20,player[Y]))
    screen.blit(pistol, (20,player[Y]+50))

    #for thug enemies
    for t in thugs:
       if t[Y]==0:
           screen.blit(thug_Car,(t[X]+offset,0))
           screen.blit(lmg,(t[X]+100,55))
       elif t[Y]==1:
           screen.blit(thug_Car,(t[X]+offset,255))
           screen.blit(lmg,(t[X]+100,310))
       else:
           screen.blit(thug_Car,(t[X]+offset,450))
           screen.blit(lmg,(t[X]+100,505))
    #for player bullets
      
    for pb in playerBullets:
            
           screen.blit(playerB, (pb[0],int(pb[1])))
    #for thug bullets
   
    for t in thugs: 
        for tb in thugBullets:
               if tb[1]==0:
                   screen.blit(thugB, (tb[0]-50,55))
                   
               elif tb[1]==1:
                    screen.blit(thugB, (tb[0]-50,310))
                    
               else:
                   screen.blit(thugB, (tb[0]-50,505))
    #updating number of ammo              
    ammoCount=str(ammo)
    ammoPic=timesFont.render(ammoText+ammoCount+"/50",TRUE,BLACK)
    screen.blit(ammoPic,(10,575))
    
    #updating damage
    damageCount=str(damage)
    damagePic=timesFont.render(damageCount+damageText,TRUE,BLACK)
    screen.blit(damagePic,(400,575))
    #updating number of thugs
    thugsCount=str(thug)
    thugsPic=timesFont.render(thugText+thugsCount+"/20",TRUE,BLACK)
    screen.blit(thugsPic,(590,575))
   

    display.flip()
    

    
        
    
    
#moving the player up and down via arrow keys, car will continiously move forward
def movePlayer(player):
    keys=key.get_pressed()
    if keys[K_UP] and player[Y]>25:
        player[Y]-=4
    if keys[K_DOWN] and player[Y]<450:
        player[Y]+=4
            
    
    
    #player[X]+=50
    #if keys[K_RIGHT] and player[X]<99500:
    #    player[X]+=10
#moving player up,down,left,right for 2nd level
def movePlayer2nd(player):
    
    keys=key.get_pressed()
    if keys[K_UP]:
        
        player[Y]-=5
        
    if keys[K_DOWN]:
        player[Y]+=5
    if keys[K_LEFT]:
        player[X]-=5
    if keys[K_RIGHT]:
        player[X]+=5
    
    
#moving thugs at the opposite direction of player 
def moveThugs(thugs):
    for t in thugs:
        t[X]-=2
        if t[X]<=-450:
            t[0]+=50000
    
    

def enemyCheckCollision(ebullet):#checking collision if enemy bullets hit player
    global thug,damage,damagePic
    offset=20-player[X]

    pr=Rect(20,player[Y],310,169)

    for tb in ebullet:
        if tb[1]==0:
            tbr=Rect(tb[0],55,25,25)
        elif tb[1]==1:
            tbr=Rect(tb[0],310,25,25)
        else:
            tbr=Rect(tb[0],505,25,25)
        #print(pr,tbr)
        
        if tbr.colliderect(pr):
            ebullet.remove(tb)
            damage+=2
            print("Hello")
        for t in thugs:
            if t[Y]==0:
                tr=Rect(t[0]+offset,0,345,165)
            elif t[Y]==1:
                tr=Rect(t[0]+offset,255,345,165)
            else:
                tr=Rect(t[0]+offset,450,345,165)
            if tr.colliderect(pr):
                damage+=5
                
                t[0]+=50000
   
    
#checking collision if player bullets hit thugs
def checkCollision(bullet,thugs):
   
    global thug
    global damage
    global damagePic
    offset=20-player[X]
    
    pr=Rect(20,player[Y],310,169)


    #print(thugs,bullet)
    
    for b in bullet:
        br=Rect(b[0],b[1],10,10)
        mmm=0
        for t in thugs:
            mmm+=1
            if t[Y]==0:
                tr=Rect(t[0]+offset,0,345,165)
                
            elif t[Y]==1:
                tr=Rect(t[0]+offset,255,345,165)
            else:
                tr=Rect(t[0]+offset,450,345,165)
          
            if br.colliderect(tr):
                
                bullet.remove(b)
                thugs.remove(t)
                thug-=1
                
            

                
            
                                
        display.flip()
    
    
    
#if either side of player hits a wall for 2nd level
def wallCollision():
    global damage
    mx,my = mouse.get_pos()
    wallC=screen.get_at((10,9))
   



    try:
        if screen.get_at((p[0]+p[2]+1,p[1]))==wallC \
            or screen.get_at((p[0]-p[2]-1,p[1]))==wallC \
            or screen.get_at((p[0],p[1]+p[2]+1))==wallC \
            or screen.get_at((p[0],p[1]-p[2]+1))==wallC:
            damage+=4
            p[0]=24
            p[1]=7
    except:
        pass
##    try:
##        if screen.get_at((p[0],p[1]))==wallC:
##            
##            or screen.get_at((p[0],p[1]))==wallC \
##            or screen.get_at((p[0],p[1]))==wallC \
##            or screen.get_at((p[0],p[1]))==wallC:
##            damage+=4
##            p[0]=24
##            p[1]=7
##    except:
##        pass
    
#showing enemy bullets when in range and moving it across screen       
def enemyBullets():
    tt=randint(0,4)
    for t in thugs:
        if t[0]<=750 and tt==0 or t[0]<=775 and tt==1:
            thugBullets.append([t[0]-25,t[1]])
    for tb in thugBullets[:]:
        tb[0]-=200
       

  
    
 
    
            
            
#placing and moving bullets across screen
def bullets():
    global rapid
    global ammo
    global ammoPic
    keys=key.get_pressed()
    if rapid>0:
        rapid-=1
    
    
    if keys[K_SPACE] and rapid==0:
        rapid=20
        ammo-=1
            
            
        playerBullets.append([player[0]+25,player[1]+58])
    for pb in playerBullets[:]:
        pb[0]+=10
        if pb[0]>800:
            playerBullets.remove(pb)

      
        
    display.flip()
    
    
    
#showing the stuff for 2nd level   
def drawScene2nd(screen,player):
    global newCar
    #changing size of screen to adjust with the maze size
    size=width,height=500,500
    screen=display.set_mode(size)
    screen.blit(maze,(0,0))
    #updating damage sustained after first level
    damageCount=str(damage)
    damagePic=timesFont.render(damageCount+damageText,TRUE,WHITE)
    screen.blit(damagePic,(100,475))
    #showing player
    screen.blit(car_Player,(player[0],player[1]))
    display.flip()
def game2nd():#2nd level
   
    running=True
    
    offset=200-player[X]
   
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
                
                
        if key.get_pressed()[27]:
            running = False
            


        #calling out functions for 2nd level
        wallCollision()
        drawScene2nd(screen,p)
        movePlayer2nd(p)
        
        
            
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        #if player reaches end, he win
        if p[1]>500:
            running=False
            game2=False
            return "Congratulations"
        #if damage is greater or equal to 100%, player loses
        if damage>=100:
            running=False
            game2=False
            return "Game Over"
        
    return "exit"
        
        
#instructions for how to play game, both first and second level    
def instructions():
    running = True
    secondRect=Rect(700,25,100,40)
    
    screen.blit(firstInstructions, (0,0))
    screen.blit(arrow,(700,25))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        
        draw.rect(screen,BLUE,secondRect,2)
        #if you click on arrow button, it will show second level and vice versa
        if mb[0]==1 and secondRect.collidepoint(mx,my):
            screen.blit(secondInstructions,(0,0))
            secondRect=Rect(5,25,100,40)
            screen.blit(leftArrow,(5,25))
            if mb[0]==1 and secondRect.collidepoint(mx,my):
                screen.blit(firstInstructions, (0,0))
                secondRect=Rect(700,25,100,40)
                screen.blit(arrow,(700,25))
            
            
            
        display.flip()
    return "menu"
#what happens if you lose
def gameOver():
    running=True
    game2=False
    game1=False
    size=width,height=800,600
    screen=display.set_mode(size)
    screen.blit(start, (0,0))
    screen.blit(overPic, (100,300))
    display.flip()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]:
            running = False
            

        display.flip()
    return "exit"
#credits for who to thank for and show support to - Me!
def credit():
    running=True
    screen.blit(cred, (0,0))
    display.flip()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        display.flip()
    return "menu"
    
#story for beginnings
def story():
    
    running=True
    screen.blit(storys, (0,0))
    display.flip()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        display.flip()
    return "menu"
#after first level is completed, show story for second level. Click arrow to advance
def storySecond():
    
    running=True
    nextRect=Rect(700,0,100,40)
    screen.blit(storys2nd, (0,0))
    screen.blit(arrow,(700,0))
    display.flip()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        draw.rect(screen,BLUE,nextRect,2)
        if mb[0]==1 and nextRect.collidepoint(mx,my):
            return "Second Level"
            



        
        display.flip()
    return "exit"

          
#what happens if you already beaten the game. No longer needed
def gameBeat():
    running=True
    screen.blit(start, (0,0))
    screen.blit(beatPic, (100,300))
    display.flip()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        display.flip()
    return "menu"
#what happens if you win and beat the game 
def congratulate():
    
    running=True
    size=width,height=800,600
    screen=display.set_mode(size)
    screen.blit(congrats, (0,0))
    
    display.flip()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        display.flip()
    return "exit"

#beginning menu of the game              
def menu():


    running = True
    myClock = time.Clock()

    different_pages=["Story","Credits","Instructions","Play"]
    buttonsPos=[Rect(300,250,100,40),Rect(300,300,100,40),Rect(300,350,100,40),Rect(300,200,100,40)]
    
    while running:
        
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        
        screen.blit(start,(0,0))
    
        screen.blit(storyPic,(300,250))
        screen.blit(creditsPic,(300,300))
        screen.blit(instructionsPic,(300,350))
        screen.blit(firstPic,(300,200))
        screen.blit(titlePic,(300,5))


    

        #displaying different buttons
        for i in range(len(buttonsPos)):
            draw.rect(screen,BLUE,buttonsPos[i],1)
            if buttonsPos[i].collidepoint(mx,my):
                draw.rect(screen,RED,buttonsPos[i],2)
                if mb[0]==1:
                    print(different_pages[i])
                    return different_pages[i]
                if mb[0]==1 and game1==False and game2==False:
                    return "Game Beaten"
                    
            else:
                draw.rect(screen,BLUE,buttonsPos[i],2)
        display.flip()
                
##Timer

myClock=time.Clock()
page="menu"
#if page is not exit
while page!="exit":
    

#what happend is page is different for menu, story, first level, second level, credits, etc. 

    
    if page=="menu":
        page=menu()
       
 
    if page == "Story":
        page = story()    
    if page == "Instructions":
        page = instructions()
    if page == "Play":
        page = game()

    if page == "Second Level":
        page = game2nd()
    
    if page == "Credits":
        page = credit()
    if page == "Second Story":
        page =  storySecond()
    if page == "Congratulations":
        page = congratulate()
    if page == "Game Over":
        page = gameOver()
    if page == "Game Beaten":
        page = gameBeat()
       


    
        

#################
    


    

quit()
