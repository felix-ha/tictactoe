import pygame
from pygame.locals import *


class Object(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Object, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Courier New', 120)
textsurface = myfont.render('X', False, (0, 0, 0))

line1 = Object(450, 5)
line2 = Object(450, 5)
line3 = Object(5, 450)
line4 = Object(5, 450)

screen = pygame.display.set_mode((450, 450))
screen.fill((255, 255, 255))

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        screen.blit(textsurface, (35, 10))

        screen.blit(line1.surf, (0, 150))
        screen.blit(line2.surf, (0, 300))
        screen.blit(line3.surf, (150, 0))
        screen.blit(line4.surf, (300, 0))
        pygame.display.flip()
