import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Game rotate")

ball = pygame.image.load("img/egg-icon.png")

ball_rect = ball.get_rect()

angle = 0

run = True

while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()

    if(keys[pygame.K_LEFT]):
        angle += 10
        angle %= 360
        trns = pygame.transform.rotate(ball,angle)
        screen.blit(trns,(150,150))

    pygame.display.update()

pygame.quit()