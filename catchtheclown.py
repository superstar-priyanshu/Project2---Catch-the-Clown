from curses import KEY_DOWN
import pygame, random
pygame.init()

WINDOW_HEIGHT = 945
WINDOW_WIDTH = 600
display = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
caption =  pygame.display.set_caption('Catch The Clown')

#setting the FPS
FPS = 60
clock = pygame.time.Clock()

#set game values
PLAYER_LIVES = 5
PLAYER_STARTING_VELOCITY = 2
CLOWN_ACCELERATION = .5

player_lives = PLAYER_LIVES
score = 0
clown_velocity = PLAYER_STARTING_VELOCITY
clown_dx = random.choice([-1,1])
clown_dy = random.choice([-1,1])

#set Fonts
font = pygame.font.Font("Franxurter.ttf", 30)
#set texts
title_text = font.render('CATCH THE CLOWN', True, (255,0,0))
title_text_rect = title_text.get_rect()
title_text_rect.topleft = (50,10)
score_text = font.render('Score: '+ str(score), True, (255,0,0))
score_text_rect = score_text.get_rect()
score_text_rect.topright = (WINDOW_HEIGHT - 50, 10)
lives_text = font.render('Lives: '+ str(player_lives), True, (255,0,0))
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_HEIGHT - 50, 50)
game_over = font.render('GAME OVER', True, (0,0,0))
game_over_rect = game_over.get_rect()
game_over_rect.center = (WINDOW_HEIGHT//2, WINDOW_WIDTH//2)
continue_text = font.render('Click any button to play again', True, (0,0,0))
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_HEIGHT//2, WINDOW_WIDTH//2 + 64)

#adding sounds
click_sound = pygame.mixer.Sound('click_sound.wav')
miss_sound = pygame.mixer.Sound('miss_sound.wav')
pygame.mixer.music.load('ctc_background_music.wav')
pygame.mixer.music.play(-1,0.0)

#adding images 

clown_image = pygame.image.load('clown.png')
clown_image_rect = clown_image.get_rect()
clown_image_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
background_image = pygame.image.load('background.png')
background_image_rect = background_image.get_rect()
background_image_rect.topleft = (0,0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
             #if the clown is being clicked
            if clown_image_rect.collidepoint(mouse_x, mouse_y):
                click_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION

                #giving the clown new direction after being clicked

                a = clown_dx
                b = clown_dy
                while(a== clown_dx and b==clown_dy):
                    clown_dx = random.choice([-1,1])
                    clown_dy = random.choice([-1,1])
            else:
                miss_sound.play()
                player_lives -= 1


    #moiving the clown

    clown_image_rect.x += clown_dx*clown_velocity
    clown_image_rect.y += clown_dy*clown_velocity

    if clown_image_rect.left<=0 or clown_image_rect.right>=WINDOW_HEIGHT:
        clown_dx = -1*clown_dx
    if clown_image_rect.top<=0 or clown_image_rect.bottom>= WINDOW_WIDTH:
        clown_dy = -1*clown_dy

    score_text = font.render('Score: '+ str(score), True, (255,0,0))
    lives_text = font.render('Lives: '+ str(player_lives), True, (255,0,0))

    #game over

    if player_lives==0:
        display.blit(game_over, game_over_rect)
        display.blit(continue_text, continue_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_LIVES
                    clown_image_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                    clown_velocity = PLAYER_STARTING_VELOCITY
                    clown_dx = random.choice([-1,1])
                    clown_dy = random.choice([-1,1])
                    pygame.mixer.music.play(-1,0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    

    display.blit(background_image, background_image_rect)
    display.blit(title_text,title_text_rect)
    display.blit(score_text, score_text_rect)
    display.blit(lives_text, lives_text_rect)
    display.blit(clown_image, clown_image_rect)

    clock.tick(FPS)

    pygame.display.update()


pygame.quit()