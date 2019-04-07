import pygame
from pygame.locals import *
import numpy as np


class Line(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Line, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()


class GUI:
    def __init__(self):
        pygame.init()

        self.A = np.array([[1, -1, 1],
                  [1, 1, 1],
                  [-1, -1, -1]])

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Courier New', 120)

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

                self.blit_game(self.A)

                self.blit_lines()
                pygame.display.flip()

    def blit_lines(self):
        for i in range(4):
            self.screen.blit(self.lines[i].surf, self.line_positions[i])

    def blit_game(self, A):
        # messed up coordinate convention of pygame
        A = self.A.transpose()

        height = width = 150

        for i in range(3):
            for j in range(3):
                if A[i,j] == 0:
                    continue
                if A[i,j] == 1:
                    letter = 'X'
                if A[i,j] == -1:
                    letter = 'O'

                self.textsurface = self.myfont.render(letter, False, (0, 0, 0))
                self.screen.blit(self.textsurface, (35 + i * height, 10 + j * width))




if __name__ == '__main__':
    gui = GUI()