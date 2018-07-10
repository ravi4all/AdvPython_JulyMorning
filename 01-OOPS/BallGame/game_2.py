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

numberOfBalls = int(input("Enter the number of balls : "))

ballList = []
for i in range(numberOfBalls):
    ball = Ball()
    ballList.append(ball)


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
    for i in range(len(ballList)):
        pygame.draw.circle(screen,black,(ballList[i].x,ballList[i].y),40)
        ballList[i].moveBall()

        for j in range(len(ballList) - i):
            distX = abs(ballList[j].x - ballList[i].x)
            distY = abs(ballList[j].y - ballList[i].y)

            if distX <= 80 and distY <= 80:
                ballList[i].moveX *= -1
                ballList[i].moveY *= -1
                ballList[j].moveX *= -1
                ballList[j].moveY *= -1

    pygame.display.update()
    clock.tick(FPS)