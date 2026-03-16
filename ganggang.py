<<<<<<< Updated upstream
import random

x = ["Bao on komea","Toivo on homo","Davut on homo"]

for i in range(10):
    gang = random.choice(x)
    print(gang)
   
=======
import pygame  
pygame.init()  


game_height = 640
game_width = 480    
PLAYER_X = 200
player_y = 200
player_width = 35
player_height =35
score = 0 

player_velocity = 0
GRAVITAATIO = 0.5


naytto = pygame.display.set_mode((game_height, game_width))  
naytto.fill((0,30,150))   #valitaan taustaväriksi musta RGB

player = pygame.draw.rect(naytto, (0,200,0), (PLAYER_X, player_y, player_width,player_height), 5)

pygame.display.set_caption("BARO BASO BOZO")

time = pygame.time.Clock()



def draw():
    global player
    naytto.fill((0,30,150))
    player = pygame.draw.rect(naytto, (0,200,0), (PLAYER_X, player_y, player_width,player_height), 5)

    
pygame.display.flip()
    
while True:
    
    keys = pygame.key.get_pressed()

    
    player_y += player_velocity
    player_velocity+=GRAVITAATIO
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player_velocity =0
                player_y -=50
            
        if player_y <= game_height :
            player_y += 10 # just use any small distance to push you back to place every frame
        
    draw()
    pygame.display.update()  


    time.tick(60)

            

        
       
>>>>>>> Stashed changes
