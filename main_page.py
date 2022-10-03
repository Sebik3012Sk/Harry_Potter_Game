import pygame
from levels_menu import levels_menu

pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Harry Potter Game")

bg_music = pygame.mixer.Sound("music/bg-music-hp.wav")
success_collision_music = pygame.mixer.Sound("music/media_success_click.wav")
bg_music.play(-1,0)

class DataLoad:
    def __init__(self): pass

    global btn_play_img
    global btn_play_rect

    global bg_image
    global bg_image_rect

    btn_play_img = pygame.image.load("img/btn-play.png")
    btn_play_rect = btn_play_img.get_rect()
 

    def btn_play():
        screen.blit(btn_play_img,(450,250))

    def harry_potter_text():
        font_text_harry = pygame.font.Font("Harry.ttf",55)
        text_harry_potter = font_text_harry.render("Harry Potter Game",True,(255,255,255))
        screen.blit(text_harry_potter,(340,10))

    def header_draw_line():
        pygame.draw.line(screen,(255,255,255),(0,80),(1000,80))

class Listeners(DataLoad):

    def btn_play_click():
        if(event.type == pygame.MOUSEBUTTONDOWN and btn_play_rect.colliderect(btn_play_rect)):
            levels_menu()
        
        
  
run = True

while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    DataLoad.harry_potter_text()
    DataLoad.header_draw_line()
    DataLoad.btn_play()
    Listeners.btn_play_click()
    pygame.display.update()

pygame.quit()