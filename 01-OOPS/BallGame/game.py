import pygame
import random

pygame.init()

class Ball():

    def __init__(self):
        self.x = random.randint(40,400)
        self.y = random.randint(40,400)
        self.moveX = random.randint(0,10)
        self.moveY = random.randint(0,10)
        self.radius = 40

    def moveBall(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > WIDTH - 40:
            self.moveX = -self.moveX
        elif self.x < 0 :
            self.moveX = abs(self.moveX)

        if self.y > HEIGHT - 40:
            self.moveY = -self.moveY
        elif self.y < 0 :
            self.moveY = abs(self.moveY)

# numberOfBalls = int(input("Enter the number of balls : "))

# ballList = []
# for i in range(numberOfBalls):
#     ball = Ball()
#     ballList.append(ball)

ball_1 = Ball()
ball_2 = Ball()

WIDTH = 1000
HEIGHT = 500

white = 255,255,255
black = 0,0,0
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
FPS = 80

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # for i in range(len(ballList)):
    #     pygame.draw.circle(screen,black,(ballList[i].x,ballList[i].y),40)
    #     ballList[i].moveBall()

    pygame.draw.circle(screen,black,(ball_1.x, ball_1.y),ball_1.radius)
    ball_1.moveBall()

    pygame.draw.circle(screen, black, (ball_2.x, ball_2.y), ball_2.radius)
    ball_2.moveBall()

    distX = abs(ball_2.x - ball_1.x)
    distY = abs(ball_2.y - ball_1.y)

    if distX <= 80 and distY <= 80:
        ball_1.moveX *= -1
        ball_1.moveY *= -1
        ball_2.moveX *= -1
        ball_2.moveY *= -1

    pygame.display.update()
    clock.tick(FPS)