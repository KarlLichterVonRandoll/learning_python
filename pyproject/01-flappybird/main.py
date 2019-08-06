import pygame, time
from pygame.locals import *

img = pygame.image.load("350.jpeg")  # 加载图片素材


def GameOver():
    pygame.quit()  # 退出游戏


def main():
    pygame.init()  # 游戏初始化
    bird = Bird()
    windowSize = pygame.display.set_mode([480, 640])  # 游戏窗口界面
    pygame.display.set_caption('游戏名称')  # 游戏标题设置
    pygame.display.update()  # 游戏界面刷新
    while True:
        """
            游戏主体模块
            事件响应
        """
        flag = 0  # 加一个标志位
        for event in pygame.event.get():
            if event.type == QUIT:
                GameOver()  # 退出游戏
            elif event.type == KEYDOWN:  # 按键响应
                if event.key == K_SPACE:
                    bird.position[1] = bird.position[1] - bird.speed*50
                    flag = 1
        if flag == 0:
            bird.position[1] = bird.position[1] + bird.speed*10
        windowSize.fill(pygame.Color(199, 237, 204))
        DrawRect(windowSize, bird)

        pygame.display.update()
        time.sleep(1)


"""
    绘制简单图像并实现简单的按键响应
"""


# 胖鸟类
class Bird:
    position = [30, 200]  # 鸟的初始位置
    birdColor = pygame.Color(255, 255, 0)  # 黄色的小鸟
    speed = 1  # 鸟的速度
    bird_score = 0  # 得分


def DrawRect(windowSize, bird):
    pygame.draw.rect(windowSize, bird.birdColor,
                     Rect(bird.position[0], bird.position[1], 30, 30))


if __name__ == "__main__":
    main()
