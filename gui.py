import pygame
from pygame.locals import *


class Line(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Line, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()


class GUI:
    def __init__(self):
        pygame.init()

        pygame.font.init()
        myfont = pygame.font.SysFont('Courier New', 120)
        textsurface = myfont.render('X', False, (0, 0, 0))

        self.lines = [Line(450, 5), Line(450, 5), Line(5, 450), Line(5, 450)]
        self.line_positions = [(0, 150), (0, 300), (150, 0), (300, 0)]


        self.screen = pygame.display.set_mode((450, 450))
        self.screen.fill((255, 255, 255))

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                self.screen.blit(textsurface, (35, 10))

                self.blit_lines()

                pygame.display.flip()

    def blit_lines(self):
        for i in range(4):
            self.screen.blit(self.lines[i].surf, self.line_positions[i])


if __name__ == '__main__':
    gui = GUI()