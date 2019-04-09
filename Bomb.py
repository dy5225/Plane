import pygame


class Bomb:
    def __init__(self, x, y, window):
        self.window = window
        self.img_bombs = []
        # 爆炸效果图存入列表
        for i in range(1, 15):
            self.img_bombs.append(pygame.image.load("img/image %d.png" % i))

        self.index = 0
        self.img_bomb = self.img_bombs[self.index]

        # 爆炸图片是否循环完
        self.isDestroy = False

        # 爆炸图片的尺寸
        self.width = self.img_bomb.get_width()
        self.height = self.img_bomb.get_height()

        self.x = x - self.width / 2
        self.y = y - self.height / 2

        # 播放爆炸的声音
        snd = pygame.mixer.Sound("snd/bomb.wav")
        snd.play()

    def display(self):
        if self.isDestroy:
            return

        self.window.blit(self.img_bomb, (self.x, self.y))

        self.index += 1
        if self.index >= len(self.img_bombs):
            self.isDestroy = True
        else:
            self.img_bomb = self.img_bombs[self.index]
