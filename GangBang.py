import pygame
from random import randint
pygame.init()

game_width = 640
game_height = 480

PLAYER_X = 150
player_y = 200
player_width = 35
player_height = 35
game_over = False

tube_x1 = 250
tube_x2= 400
tube_x3= 550
tube_x4=700

TUBES_GAP = 150
TUBE_WIDTH = 50
tube_height1 = randint(100,400)
tube_height2 = randint(100,400)
tube_height3 = randint(100,400)
tube_height4 = randint(100,400)


TUBE_VELOCITY =3




player_velocity = 0
GRAVITAATIO = 0.5

naytto = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("BARO BASO BOZO")

font1 = pygame.font.SysFont('freesansbold.ttf', 50)
text1 = font1.render('YOU LOST', True, (0,0,0))
textRect1 = text1.get_rect(center=(320,240))

text2 = font1.render('PRESS R TO RESTART', True, (0,0,0))
textRect2 = text1.get_rect(center=(320,200))


player = pygame.Rect(PLAYER_X, player_y, player_width, player_height)

clock = pygame.time.Clock()

def draw():
    pygame.draw.rect(naytto, (0,200,0), player, 5)  
    pygame.display.update()  

    
while True:
    clock.tick(60)
    naytto.fill((0,30,150))

    #törnien piirtäminen
    tube1 = pygame.draw.rect(naytto, (0,255,0), (tube_x1, 0, TUBE_WIDTH, tube_height1))
    tube2  = pygame.draw.rect(naytto, (0,255,0), (tube_x2, 0, TUBE_WIDTH, tube_height2))
    tube3  = pygame.draw.rect(naytto, (0,255,0), (tube_x3, 0, TUBE_WIDTH, tube_height3))
    tube_4  = pygame.draw.rect(naytto, (0,255,0), (tube_x4, 0, TUBE_WIDTH, tube_height4))

    inv_tube1 = pygame.draw.rect(naytto, (0,255,0),(tube_x1, tube_height1+TUBES_GAP, TUBE_WIDTH, game_height-TUBES_GAP-tube_height1) )
    inv_tube2 = pygame.draw.rect(naytto, (0,255,0),(tube_x2, tube_height2+TUBES_GAP, TUBE_WIDTH, game_height-TUBES_GAP-tube_height2) )
    inv_tube3 = pygame.draw.rect(naytto, (0,255,0),(tube_x3, tube_height3+TUBES_GAP, TUBE_WIDTH, game_height-TUBES_GAP-tube_height3) )
    inv_tube4 = pygame.draw.rect(naytto, (0,255,0),(tube_x4, tube_height4+TUBES_GAP, TUBE_WIDTH, game_height-TUBES_GAP-tube_height4) )


    tube_x1 -= TUBE_VELOCITY 
    tube_x2 -= TUBE_VELOCITY 
    tube_x3 -= TUBE_VELOCITY
    tube_x4 -= TUBE_VELOCITY

    if tube_x1 <= -50:
        tube_height1 = randint(100,400)
        tube_x1 = game_width
    if tube_x2 <= -50:
        tube_height2 = randint(100,400)
        tube_x2 = game_width
    if tube_x3 <= -50:
        tube_height3 = randint(100,400)
        tube_x3 = game_width
    if tube_x4 <= -50:
        tube_height4 = randint(100,400)
        tube_x4 = game_width



    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player_velocity =-12
    
        

    if not game_over:
            player_velocity += GRAVITAATIO
            player.y += player_velocity
    
    if player.bottom >= game_height:
        game_over = True       

    if game_over:
        player_velocity = 0
        TUBE_VELOCITY=0
        naytto.blit(text1, textRect1)
        naytto.blit(text2, textRect2)


    if player.colliderect(tube1):
        game_over = True
    if player.colliderect(tube2):
        game_over = True
    if player.colliderect(tube3):
        game_over = True
    if player.colliderect(tube_4):
        game_over = True
    draw()


    

            

        
       