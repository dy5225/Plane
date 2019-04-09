import random
import pygame
from utility import *


class EnemyPlane():
    def __init__(self, window):
        self.window = window
        self.__reset()

    def display(self):
        self.window.blit(self.img_ep, (self.x, self.y))

    def move(self):
        self.y += 5

        # 判断飞机有没有飞出屏幕
        if self.y > WINDOW_HEIGHT:
            self.__reset()

    def __reset(self):
        '''飞机飞出屏幕之后重置飞机'''
        self.img_ep = pygame.image.load("img/img-plane_%d.png" % random.randint(1, 7))
        self.img_ep_wideh = self.img_ep.get_width()
        self.img_ep_height = self.img_ep.get_height()


        min = -self.img_ep_wideh / 2
        max = WINDOW_WIGTH - self.img_ep_wideh / 2
        self.x = random.randint(min, max)
        self.y = -self.img_ep_height

    def beiza(self):
        self.__reset()
