import pygame
from random import randint
pygame.init()

game_width = 640
game_height = 480

PLAYER_X = 150
player_y = 200
player_width = 35
player_height = 35
passed1=False
passed2=False
passed3 =False
passed4 = False

tube_x1 = game_width
tube_x2= game_width+150
tube_x3= game_width+300
tube_x4=game_width+450
TUBES_GAP = 150
TUBE_WIDTH = 50
tube_height1 = randint(100,300)
tube_height2 = randint(100,300)
tube_height3 = randint(100,300)
tube_height4 = randint(100,300)

game_over = False
score = 0
best_score = 0

TUBE_VELOCITY =3
player_velocity = 0
GRAVITAATIO = 0.5

#tekstien kirjoittaminen
naytto = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("BARO BASO BOZO")
score_font=pygame.font.SysFont('freesansbold.ttf', 30)
font1 = pygame.font.SysFont('freesansbold.ttf', 50)
text1 = font1.render('YOU LOST', True, (0,0,0))
textRect1 = text1.get_rect(center=(320,240))
text2 = font1.render('PRESS R TO RESTART', True, (0,0,0))
textRect2 = text2.get_rect(center=(320,200))


player = pygame.Rect(PLAYER_X, player_y, player_width, player_height)

clock = pygame.time.Clock()

def draw():
    pygame.draw.rect(naytto, (0,200,0), player, 5)  
    pygame.display.update()  

def reset_game():
    global game_over, player_velocity, TUBE_VELOCITY
    global tube_x1, tube_x2, tube_x3, tube_x4
    global tube_height1, tube_height2, tube_height3, tube_height4
    global score

    game_over = False
    player.y = 200
    player_velocity = 0
    TUBE_VELOCITY = 3

    tube_x1 = game_width
    tube_x2 = game_width + 150
    tube_x3 = game_width + 300
    tube_x4 = game_width + 450

    tube_height1 = randint(100,300)
    tube_height2 = randint(100,300)
    tube_height3 = randint(100,300)
    tube_height4 = randint(100,300)


    score = 0
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

#törnien liike
    if not game_over:
        tube_x1 -= TUBE_VELOCITY 
        tube_x2 -= TUBE_VELOCITY 
        tube_x3 -= TUBE_VELOCITY
        tube_x4 -= TUBE_VELOCITY



#pisteiden laskeminen
    if tube_x1 + TUBE_WIDTH < PLAYER_X and not passed1:
        score += 1
        passed1 = True
    if tube_x2 + TUBE_WIDTH < PLAYER_X and not passed2:
        score += 1
        passed2 = True
    if tube_x3 + TUBE_WIDTH< PLAYER_X and not passed3:
        score +=1
        passed3 = True
    if tube_x4 + TUBE_WIDTH < PLAYER_X and not passed4:
        score += 1
        passed4 = True    
        
    TUBE_VELOCITY = 3 + score * 0.05


    #törnien uudestaan luominen
    if tube_x1 <= -50:
        tube_height1 = randint(100,300)
        tube_x1 = game_width
        passed1 = False
    if tube_x2 <= -50:
        tube_height2 = randint(100,300)
        tube_x2 = game_width
        passed2=False
    if tube_x3 <= -50:
        tube_height3 = randint(100,300)
        tube_x3 = game_width
        passed3= False
    if tube_x4 <= -50:
        tube_height4 = randint(100,300)
        tube_x4 = game_width
        passed4= False  

#pisteiden tulostaminen
    text3 = score_font.render(f"Score: {str(score)}", True, (0,0,0))
    textRect3 = text3.get_rect(center=(80,40))
    naytto.blit(text3, textRect3)

    text4 = score_font.render(f"Best Score: {str(best_score)}", True, (0,0,0))
    textRect4 = text4.get_rect(center=(80,60))
    naytto.blit(text4, textRect4)

#control
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player_velocity = -7

            if event.key == pygame.K_r and game_over:
                reset_game()
                
#gravitaatio
    if not game_over:
            player_velocity += GRAVITAATIO
            player.y += player_velocity

#losing conditions
    if player.top == -35:
        game_over = True 
    if player.bottom >= game_height:
        game_over = True       

    if game_over:
        player_velocity = 0
        naytto.blit(text1, textRect1)
        naytto.blit(text2, textRect2)


    if player.colliderect(tube1) or player.colliderect(inv_tube1) \
or player.colliderect(tube2) or player.colliderect(inv_tube2) \
or player.colliderect(tube3) or player.colliderect(inv_tube3) \
or player.colliderect(tube_4) or player.colliderect(inv_tube4):
        game_over = True

    if game_over and score > best_score:
        best_score = score
    draw()

    

            

        
       