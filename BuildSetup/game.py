import pygame
import random
pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width,height))
main_bg = pygame.image.load("images/background.png")
gun_sound = pygame.mixer.Sound("sounds/shot_sound.wav")
bg_music = pygame.mixer.Sound("sounds/background.wav")
bg_music.play(-1)
zombie_list = []
for i in range(4):
    zombie = pygame.image.load("images/zombie_{}.png".format(i+1))
    zombie_list.append(zombie)
gun_pointer = pygame.image.load("images/aim_pointer.png")
gun = pygame.image.load("images/gun_1.png")
def gameScreen():
    zombie_image = random.choice(zombie_list)
    zombie_x = random.randint(0, width - zombie_image.get_width())
    zombie_y = random.randint(0, height - zombie_image.get_height())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # gun_sound.play(-1) # infinite loop for music
                gun_sound.play()
                if pointer_rect.colliderect(zombie_rect):
                    zombie_image = random.choice(zombie_list)
                    zombie_x = random.randint(0, width - zombie_image.get_width())
                    zombie_y = random.randint(0, height - zombie_image.get_height())
        screen.blit(main_bg,(0,0))  # blit - render
        screen.blit(zombie_image, (zombie_x, zombie_y))
        posX, posY = pygame.mouse.get_pos()
        screen.blit(gun_pointer, (posX - gun_pointer.get_width()/2, posY - gun_pointer.get_height()/2))
        screen.blit(gun, (posX, height - gun.get_height()))
        pointer_rect = pygame.Rect(posX - gun_pointer.get_width()/2, posY - gun_pointer.get_height()/2, gun_pointer.get_width(), gun_pointer.get_height())
        zombie_rect = pygame.Rect(zombie_x, zombie_y,zombie_image.get_width(), zombie_image.get_height())
        pygame.display.update()
gameScreen()