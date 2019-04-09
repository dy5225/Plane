import main
from buller import *
from utility import *
import Bomb
import enemyPlane as eenemyPlane
import time


class Player_Plane:
    def __init__(self, window):
        '''初始化玩家飞机'''
        self.x = 210
        self.y = 730
        self.image = pygame.image.load("img/hero2.png")
        # 飞机图片的宽度、高度
        self.img_width = self.image.get_width()
        self.img_height = self.image.get_height()
        self.window = window

        # 飞机的子弹属性
        self.bullets = []

        # 子弹发射时间间隔
        self.__bullet_start = 0
        self.__bullet_end = 0.3

        #爆炸物集合
        self.bombs = []

    def display(self):
        '''显示飞机'''
        self.window.blit(self.image, (self.x, self.y))

        # 显示子弹
        # 当子弹超过屏幕，将子弹回收
        for bullet in list(self.bullets):
            if bullet.y < - bullet.img_bullet_height:
                self.bullets.remove(bullet)

            #当子弹和敌人相撞的时候，收回子弹和敌人
            rect_buller = pygame.Rect(bullet.x,bullet.y,bullet.img_bullet_width,bullet.img_bullet_height)
            for enemy in utility.enemys:
                rect_enemy = pygame.Rect(enemy.x, enemy.y,enemy.img_ep_wideh,enemy.img_ep_height)
                collide = pygame.Rect.colliderect(rect_buller,rect_enemy)
                if collide:
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

                     #爆炸效果
                    x = enemy.x + enemy.img_ep_wideh/2
                    y = enemy.y + enemy.img_ep_height/2

                    self.bombs.append(Bomb.Bomb(x,y,self.window))


                    #敌机被炸，回收敌机
                    enemy.beiza()

                    #得分

                    utility.score += 10

            bullet.display()
            bullet.move()

        # 显示爆炸物
        for bomb in list(self.bombs):
            if bomb.isDestroy:
                self.bombs.remove(bomb)
            bomb.display()




    def re_buller(self):
        self.bullets.clear()


    def plane_left(self):
        '''向左'''
        self.x -= 5

        if self.x < -self.img_width / 2:
            self.x = -self.img_width / 2

    def plane_right(self):
        '''向右'''
        self.x += 5

        if self.x > WINDOW_WIGTH - self.img_width / 2:
            self.x = WINDOW_WIGTH - self.img_width / 2

    def plane_up(self):
        '''向上'''
        self.y -= 5

        if self.y < -self.img_height / 2:
            self.y = -self.img_height / 2

    def plane_down(self):
        '''向下'''
        self.y += 5

        if self.y > WINDOW_HEIGHT - self.img_height / 2:
            self.y = WINDOW_HEIGHT - self.img_height / 2

    def fire(self):
        '''玩家发射子弹'''
        now = time.time()
        if now - self.__bullet_start < self.__bullet_end:
            return


        self.__bullet_start = now

        # 子弹从飞机正前方发出
        x = self.x + self.img_width / 2
        y = self.y
        self.bullets.append(Bullet(x, y, self.window))

        # 左侧
        x = self.x + self.img_width / 4
        y = self.y
        self.bullets.append(Bullet(x, y, self.window))

        # 右侧
        x = self.x + self.img_width * 3 / 4
        y = self.y
        self.bullets.append(Bullet(x, y, self.window))

        # 右侧
        x = self.x + self.img_width / 10
        y = self.y
        self.bullets.append(Bullet(x, y, self.window))

        # 右侧
        x = self.x + self.img_width * 9 / 10
        y = self.y
        self.bullets.append(Bullet(x, y, self.window))
