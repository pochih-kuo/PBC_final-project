import sys, time
import random
import os

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
IMAGEWIDTH = 60
IMAGEHEIGHT = 110
FPS = 10
line_x_position = 80
line_y_position = 150
show_probability1 = 30  # 每次顯示通知機率 (%)
show_probability2 = 30
path1 = os.path.abspath('line.png')
path2 = os.path.abspath('line2.png')


gpa_lsit = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 0]
class Line(pygame.sprite.Sprite):
    def __init__(self, width, height, x_position, y_position, window_width, window_height, path):
        super().__init__()
        # 載入圖片
        self.raw_image = pygame.image.load(path).convert_alpha()
        # 縮小圖片
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        #  回傳位置
        self.rect = self.image.get_rect()
        #  定位
        self.rect.topleft = (x_position, y_position)
        self.width = width
        self.height = height
        self.window_width = window_width
        self.window_height = window_height

def main():
    pygame.init()

    # load window surface
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Stop Procrastinating!')
    line = Line(IMAGEWIDTH, IMAGEHEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, path1)
    reload_line_event = USEREVENT + 1
    pygame.time.set_timer(reload_line_event, 2000)  # 更新頻率(unit = ms)
    i = 0
    points = gpa_lsit[i]  # 初始分數 : 4.3
    my_font = pygame.font.SysFont(None, 30)
    my_hit_font = pygame.font.SysFont(None, 40)
    hit_text_surface = None
    main_clock = pygame.time.Clock()
    
    
    while True:
        if pygame.time.get_ticks() > 60000:  # 遊戲打開 60 秒後自動關閉
            pygame.quit()
            sys.exit()
        
        # 偵測事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == reload_line_event:
                # 重新整理
                if random.randrange(0, 100) < show_probability1:
                    # show
                    PATH = path1
                    line = Line(IMAGEWIDTH, IMAGEHEIGHT, line_x_position, line_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                elif show_probability1 < random.randrange(0, 100) < show_probability1 + show_probability2:
                    # show
                    PATH = path2
                    line = Line(IMAGEWIDTH, IMAGEHEIGHT, line_x_position, line_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                else:
                    # hide (藏在右下)
                    PATH = path1
                    line = Line(IMAGEWIDTH, IMAGEHEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                
            elif event.type == MOUSEBUTTONDOWN:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在圖片上
                if line.rect.topleft[0] < pygame.mouse.get_pos()[0] < line.rect.topleft[0] + IMAGEWIDTH \
                    and line.rect.topleft[1] < pygame.mouse.get_pos()[1] < line.rect.topleft[1] + IMAGEHEIGHT:

                    PATH = path1
                    line = Line(IMAGEWIDTH, IMAGEHEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                    hit_text_surface = my_hit_font.render('OOPS', True, (0, 0, 0))
                    # 算分
                    i += 1
                    if i < 10:
                        points = gpa_lsit[i]
                    else:
                     points = 0


        # 遊戲分數儀表板
        text_surface = my_font.render('GPA = {}'.format(round(points,2)), True, (0, 0, 0))
        # 渲染物件
        background_raw = pygame.image.load(os.path.abspath('background.jpg'))
        # 調整背景圖片大小
        background = pygame.transform.scale(background_raw, (WINDOW_WIDTH , WINDOW_HEIGHT ))
        background.convert()
        window_surface.blit(background, (0,0))
        window_surface.blit(line.image, line.rect)
        window_surface.blit(text_surface, (10, 5 ))

        # 顯示提示文字(oops)
        # if hit_text_surface:
            # window_surface.blit(hit_text_surface, (400, 300))
            # hit_text_surface = None

        pygame.display.update()
        # 控制遊戲迴圈迭代速率
        main_clock.tick(FPS)
        

if __name__ == '__main__':    
    main()