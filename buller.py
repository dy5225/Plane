from main import *


class Bullet:
    def __init__(self, x, y, window):
        self.img_bullet = pygame.image.load("img/hero2.png")
        self.img_bullet_width = self.img_bullet.get_width()
        self.img_bullet_height = self.img_bullet.get_height()
        self.window = window

        self.x = x - self.img_bullet_width / 2
        self.y = y - self.img_bullet_height / 2

    def display(self):
        '''将子弹显示在窗体上'''
        self.window.blit(self.img_bullet, (self.x, self.y))

    def move(self):
        '''子弹移动'''
        self.y -= 5

    def re_buller(self):
        self.bullets.clear()
