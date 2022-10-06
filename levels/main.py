import pygame
import socket
import random


def main_level_one():
    pygame.init()

    # adress github : https://github.com/Sebik3012Sk/Harry_Potter_Game.git

    width = 1000
    height = 600

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Game Harry Potter")

    harry_potter = pygame.image.load("img/harryPotter.png")
    goblet = pygame.image.load("img/goblet-icon.png")
    hedvika = pygame.image.load("img/owl-icon.png")
    background = pygame.image.load("img/hogwarts-castle.jpg")
    icon = pygame.image.load("img/harryPotter.png")
    bullet = pygame.image.load("img/egg-icon.png")
    btn_quit_game = pygame.image.load("img/quit-game.png")


    harry_potter_rect = harry_potter.get_rect()
    hedvika_rect = hedvika.get_rect()
    background_image_rect = background.get_rect()
    goblet_rect = goblet.get_rect()
    bullet_rect = bullet.get_rect()
    btn_quit_rect = btn_quit_game.get_rect()

    background_image_rect.center = (width//2,400)

    run = True


    pygame.display.set_icon(icon)

    # load_sounds
    bg_music = pygame.mixer.Sound("music/bg-music-hp.wav")
    success_collision_music = pygame.mixer.Sound("music/media_success_click.wav")
    bg_music.play(-1,0)


    font_root = pygame.font.Font("Harry.ttf",50)
    font_root_harry = pygame.font.Font("Harry.ttf",64)
    font_lives = pygame.font.Font("Harry.ttf",50)

    score = 0

    harry_potter_text = font_root.render("Level 1",True,(255,255,255))
    victory_text = font_root_harry.render("",True,(255,255,255))

    angle = 0
    angle_s = 0

    x = 300
    y = 300

    vel = 8

    harry_potter_rect.centerx = 350
    harry_potter_rect.centery = 350

    hedvika_rect.centerx = 400
    hedvika_rect.centery = 400

    goblet_rect.centery = 75
    goblet_rect.centerx = 0

    bullet_rect.centerx = -3
    bullet_rect.centery = -3

    fps = 120
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or event.type == pygame.K_ESCAPE):
                run = False
            elif(event.type == pygame.MOUSEMOTION):
                harry_potter_rect.x = event.pos[0]
                harry_potter_rect.y = event.pos[1]

            
        
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_UP] and harry_potter_rect.top > 75):
            harry_potter_rect.y -= vel
        elif(keys[pygame.K_DOWN] and harry_potter_rect.bottom < height):
            harry_potter_rect.y += vel
        elif(keys[pygame.K_RIGHT] and harry_potter_rect.right < width):
            harry_potter_rect.x += vel
        elif(keys[pygame.K_LEFT] and harry_potter_rect.left > 0):
            harry_potter_rect.x -= vel


        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(btn_quit_rect.colliderect(btn_quit_rect)):
                run = False

        if(keys[pygame.K_f]):
            bullet_rect.centerx = harry_potter_rect.x + 23
            bullet_rect.centery = harry_potter_rect.y + 23


        if(bullet_rect.centerx < -2):
            pass
        else:
            bullet_rect.centerx += vel   


        if(bullet_rect.colliderect(hedvika_rect)):
            score += 1
            goblet_rect.centerx += 25
            hedvika_rect.centerx = random.randint(0,750)
            hedvika_rect.centery = random.randint(85,600)

            


            
            text_victory = "You Won"
            

            if(goblet_rect.x > width):

                victory_text = font_root.render(text_victory,True,(255,255,255))
                

            if(score >= 40):
                victory_text = font_root.render("You won",True,(255,255,255))
                score = 0
                

        if(harry_potter_rect.colliderect(hedvika_rect)):
            hedvika_rect.centerx = random.randint(10,890)
            hedvika_rect.centery = random.randint(85,600)
            goblet_rect.centerx += 25
            goblet_rect.centery = 75
            score += 1
            success_collision_music.play()


            text_victory = "You Won"
            

            if(goblet_rect.x > width):

                victory_text = font_root.render(text_victory,True,(255,255,255))
                

                if(score >= 40):
                    victory_text = font_root.render("You won",True,(255,255,255))
                    score = 0
        


        text_score = font_root.render(f"Score : {score}",True,(255,255,255))

        angle += 10
        angle %= 360
        trn = pygame.transform.rotate(hedvika,angle)
        

        screen.fill((0,0,0))  
        pygame.draw.line(screen,(255,255,255),(0,75),(1000,75),2)
        screen.blit(background,background_image_rect)
        screen.blit(harry_potter_text,(350,21))
        screen.blit(goblet,goblet_rect)  
        screen.blit(harry_potter,(harry_potter_rect.x,harry_potter_rect.y))
        screen.blit(trn,hedvika_rect)
        screen.blit(text_score,(30,30))
        screen.blit(bullet,bullet_rect)
        screen.blit(victory_text,(width//2,350))
        screen.blit(btn_quit_game,(930,21))
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

