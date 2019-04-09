from pygame.locals import *
import pygame
import sys
import plane
from enemyPlane import EnemyPlane
import utility
import Bomb
import time

if __name__ == '__main__':

    # 初始化窗体
    pygame.init()
    # 窗体
    screen = pygame.display.set_mode((utility.WINDOW_WIGTH, utility.WINDOW_HEIGHT))

    # 背景
    bg = pygame.image.load('img/img_bg_level_2.jpg')

    # 字体
    font = pygame.font.Font('font/happy.ttf', 24)
    font2 = pygame.font.Font('font/happy.ttf', 36)

    fps = 0

    # 标题
    pygame.display.set_caption("飞机大战")

    # 图标
    pygame.display.set_icon(pygame.image.load("img/app.ico"))

    # 玩家飞机对象
    player = plane.Player_Plane(screen)

    # 敌方飞机对象
    utility.enemys = []
    for i in range(1, 11):
        utility.enemys.append(EnemyPlane(screen))

    game_over = False

    while True:
        start = time.time()
        screen.blit(bg, (0, 0))

        if not game_over:

            # 判断玩家飞机个地方飞机相撞
            playRect = pygame.Rect(player.x, player.y, player.img_width, player.img_height)
            for enemy in utility.enemys:
                enemyRect = pygame.Rect(enemy.x, enemy.y, enemy.img_ep_wideh, enemy.img_ep_height)
                ico = pygame.Rect.colliderect(playRect, enemyRect)
                if ico:
                    x = player.x - player.img_width / 2
                    y = player.y - player.img_height / 2
                    player.bombs.append(Bomb.Bomb(x, y, screen))

                    # 游戏结束
                    game_over = True
                    break
        if not game_over:
            # 显示玩家飞机
            player.display()
        if not game_over:
            # 显示敌方飞机
            for enemyPlane in utility.enemys:
                enemyPlane.display()
                enemyPlane.move()

            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                player.plane_left()
            if keys[K_RIGHT]:
                player.plane_right()
            if keys[K_UP]:
                player.plane_up()
            if keys[K_DOWN]:
                player.plane_down()
            if keys[K_SPACE]:
                player.fire()

        # 2. 根据字体去渲染文字
        # 通过字体去渲染想写的文字，--》类似图片
        text_score = font.render("得分:%d" % utility.score, True, (0xff, 0xff, 0xff))

        # 3. 把文字放到具体的位置
        screen.blit(text_score, (10, 10))

        # 2. 根据字体去渲染文字
        # 通过字体去渲染想写的文字，--》类似图片
        text_fps = font.render("FPS:%d" % fps, True, (0xff, 0xff, 0xff))

        # 3. 把文字放到具体的位置
        screen.blit(text_fps, (420, 10))




        #游戏结束显示
        if game_over:
            text_over = font2.render('Game Over', True, (255, 0, 0))
            rect = text_over.get_rect(center=(utility.WINDOW_WIGTH / 2, utility.WINDOW_HEIGHT / 2))

            screen.blit(text_over, rect)

            text_over = font2.render("点击Enter重新开始", True, (0xff, 0x00, 0x00))
            rect = text_over.get_rect(center=(utility.WINDOW_WIGTH / 2, utility.WINDOW_HEIGHT / 2 + 30))

            # 3. 把文字放到具体的位置
            screen.blit(text_over, rect)

        # 刷新窗体
        pygame.display.flip()

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_RETURN and game_over:
                    utility.score = 0
                    # 敌军飞机回收
                    for enemy in utility.enemys:
                        enemy.beiza()
                    player.re_buller()

                    # 重新开始
                    game_over = False

        # 控制飞机移动
        end = time.time()

        try:
            fps = 1 / (end - start)
        except Exception as e:
            pass
