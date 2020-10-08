import sys
from random import randint
import pygame
import paddle

class main:
    def __init__(self,width,height):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width,height))
        self.width = width
        self.height = height
        self.blocks = []
        self.paddle = paddle.paddle(self.width, self.height)

    def draw(self):
        self.screen.fill((20,20,20))
        self.paddle.draw(self.screen)
        pygame.display.flip()

    def handleinput(self):
        input = pygame.event.get()
        for event in input:
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while True:
            self.clock.tick(60)
            self.handleinput()
            self.draw()

run = main(500,500)
run.run()
