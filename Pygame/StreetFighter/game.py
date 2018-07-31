import pygame
from pygame.locals import *
from os import path


WIDTH = 1200
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'sounds')

class Spritesheet():

    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name

    def getImage(self, x, y, width, height):

        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey(BLACK)

        return image


class Player_1(pygame.sprite.Sprite):

    standingFrames = []
    kickFrames = []
    punchFrames = []
    walkingFrames = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        sprites = Spritesheet(player_sprite)
        self.image = sprites.getImage(48,247,106,239)
        self.standingFrames.append(self.image)
        self.image = sprites.getImage(264,240,113,249)
        self.standingFrames.append(self.image)
        self.image = sprites.getImage(482,248,106,237)
        self.standingFrames.append(self.image)
        self.image = sprites.getImage(687,247,112,241)
        self.standingFrames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 - 250, HEIGHT / 2 + 70)
        self.pos = 0

    def update(self):
        self.pos += 5

        frame = (self.pos // 30) % len(self.standingFrames)
        print("Position",self.pos//30)
        print("Frame",frame)
        self.image = self.standingFrames[frame]


pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street Fighter")
clock = pygame.time.Clock()

player_sprite = pygame.image.load(path.join(img_dir, "ken_.png")).convert_alpha()

all_sprites = pygame.sprite.Group()
player = Player_1()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()