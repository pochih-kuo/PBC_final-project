import sys, time
import random
import os

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
IMAGEWIDTH = 100
IMAGEHEIGHT = 100
FPS = 10
SPACING = 50
FIRST_X_POSITION = 100
FIRST_Y_POSITION = 100


pathes = ['clothes1.png', 'clothes2.png', 'clothes3.png', 'pants1.png', 'pants2.png', 'pants3.png', 'shoes1.png', 'shoes2.png', 'shoes3.png']
point_list = [1,2,3, 4, 5, 6, 7, 8, 9]

class Picture(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, path, point):
        super().__init__()
        # 載入圖片
        self.raw_image = pygame.image.load(path).convert_alpha()
        #self.raw_image = pygame.image.load(os.path.abspath('./game2/'+path)).convert_alpha()
        # 縮小圖片
        self.image = pygame.transform.scale(self.raw_image, (IMAGEWIDTH, IMAGEHEIGHT))
        #  回傳位置
        self.rect = self.image.get_rect()
        #  定位
        self.rect.topleft = (x_position, y_position)
        self.width = IMAGEWIDTH
        self.height = IMAGEHEIGHT
        self.window_width = WINDOW_WIDTH
        self.window_height = WINDOW_HEIGHT
        self.point = point

def main():
    pygame.init()

    # load window surface
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Choose Wisely')
    group = pygame.sprite.Group()
    ok = Picture(600, 400,'ok.png', 0)
    ok.image = pygame.transform.scale(ok.raw_image, (80, 80))
    square_for_clothes = Picture(WINDOW_WIDTH, WINDOW_HEIGHT, 'square.png', 0)  # 把 square 藏在右下角
    square_for_pants = Picture(WINDOW_WIDTH, WINDOW_HEIGHT, 'square.png', 0)  # 把 square 藏在右下角
    square_for_shoes = Picture(WINDOW_WIDTH, WINDOW_HEIGHT, 'square.png', 0)  # 把 square 藏在右下角
    clothes1 = Picture(FIRST_X_POSITION, FIRST_Y_POSITION, \
                        ''+pathes[0], point_list[0])
    clothes2 = Picture(FIRST_X_POSITION + IMAGEWIDTH + SPACING, FIRST_Y_POSITION, \
                        ''+pathes[1], point_list[1])
    clothes3 = Picture(FIRST_X_POSITION + 2*IMAGEWIDTH + 2*SPACING, FIRST_Y_POSITION, \
                        ''+pathes[2], point_list[2])
    pants1 = Picture(FIRST_X_POSITION, FIRST_Y_POSITION + IMAGEHEIGHT + SPACING, \
                        ''+pathes[3], point_list[3])
    pants2 = Picture(FIRST_X_POSITION + IMAGEWIDTH + SPACING, FIRST_Y_POSITION + IMAGEHEIGHT + SPACING, \
                        ''+pathes[4], point_list[4])
    pants3 = Picture(FIRST_X_POSITION + 2*IMAGEWIDTH + 2*SPACING, FIRST_Y_POSITION + IMAGEHEIGHT + SPACING, \
                        ''+pathes[5], point_list[5])
    shoes1 = Picture(FIRST_X_POSITION, FIRST_Y_POSITION + 2*IMAGEHEIGHT + 2*SPACING, \
                        ''+pathes[6], point_list[6])
    shoes2 = Picture(FIRST_X_POSITION + IMAGEWIDTH + SPACING, FIRST_Y_POSITION + 2*IMAGEHEIGHT + 2*SPACING, \
                        ''+pathes[7], point_list[7])
    shoes3 = Picture(FIRST_X_POSITION + 2*IMAGEWIDTH + 2*SPACING, FIRST_Y_POSITION + 2*IMAGEHEIGHT + 2*SPACING, \
                        ''+pathes[8], point_list[8])
    list = [clothes1, clothes2, clothes3, pants1, pants2, pants3, shoes1, shoes2, shoes3]
    for item in list:
        group.add(item)

    clothes_points = 0 
    pants_point = 0
    shoes_point = 0
    my_font = pygame.font.SysFont(None, 30)
    my_score_font = pygame.font.SysFont(None, 100)
    main_clock = pygame.time.Clock()
    i = 0
    t = 0
    
    while True:
        
        # 偵測事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN and i == 0:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在圖片上
                for item in list:
                    if FIRST_Y_POSITION < pygame.mouse.get_pos()[1] < FIRST_Y_POSITION + IMAGEHEIGHT:  #　choose clothes
                        if item.rect.topleft[0] < pygame.mouse.get_pos()[0] < item.rect.topleft[0] + IMAGEWIDTH \
                            and item.rect.topleft[1] < pygame.mouse.get_pos()[1] < item.rect.topleft[1] + IMAGEHEIGHT:
                            
                            square_for_clothes = Picture(item.rect.topleft[0], item.rect.topleft[1], 'square.png', 0)
                            clothes_points = item.point

                    elif FIRST_Y_POSITION + IMAGEHEIGHT + SPACING < pygame.mouse.get_pos()[1] < FIRST_Y_POSITION + 2*IMAGEHEIGHT + SPACING:  #　choose pants
                        if item.rect.topleft[0] < pygame.mouse.get_pos()[0] < item.rect.topleft[0] + IMAGEWIDTH \
                            and item.rect.topleft[1] < pygame.mouse.get_pos()[1] < item.rect.topleft[1] + IMAGEHEIGHT:
                            
                            square_for_pants = Picture(item.rect.topleft[0], item.rect.topleft[1], 'square.png', 0)
                            pants_point = item.point

                    elif FIRST_Y_POSITION + 2*IMAGEHEIGHT + 2*SPACING < pygame.mouse.get_pos()[1] < FIRST_Y_POSITION + 3*IMAGEHEIGHT + 2*SPACING:  #　choose shoes
                        if item.rect.topleft[0] < pygame.mouse.get_pos()[0] < item.rect.topleft[0] + IMAGEWIDTH \
                            and item.rect.topleft[1] < pygame.mouse.get_pos()[1] < item.rect.topleft[1] + IMAGEHEIGHT:
                            
                            square_for_shoes = Picture(item.rect.topleft[0], item.rect.topleft[1], 'square.png', 0)
                            shoes_point = item.point

                if ok.rect.topleft[0] < pygame.mouse.get_pos()[0] < ok.rect.topleft[0] + 80 \
                    and ok.rect.topleft[1] < pygame.mouse.get_pos()[1] < ok.rect.topleft[1] + 80:

                    for item in list:
                        item.kill()
                    square_for_clothes = Picture(WINDOW_WIDTH, WINDOW_HEIGHT, 'square.png', 0)  # 把 square 藏在右下角
                    square_for_pants = Picture(WINDOW_WIDTH, WINDOW_HEIGHT, 'square.png', 0)  # 把 square 藏在右下角
                    square_for_shoes = Picture(WINDOW_WIDTH, WINDOW_HEIGHT, 'square.png', 0)  # 把 square 藏在右下角
                    ok = Picture(WINDOW_WIDTH, WINDOW_HEIGHT,'ok.png', 0)
                    i = 1
   

        points = clothes_points + pants_point + shoes_point
        # 遊戲分數儀表板
        text_surface = my_font.render('$$ = {}'.format(round(points,2)), True, (0, 0, 0))
        # 渲染物件
        background_raw = pygame.image.load('background.jpg')
        # background_raw = pygame.image.load(os.path.abspath('./game2/background.jpg'))
        # 調整背景圖片大小
        background = pygame.transform.scale(background_raw, (WINDOW_WIDTH , WINDOW_HEIGHT ))
        background.convert()
        window_surface.blit(background, (0,0))
        group.draw(window_surface)
        window_surface.blit(square_for_clothes.image, square_for_clothes.rect)
        window_surface.blit(square_for_pants.image, square_for_pants.rect)
        window_surface.blit(square_for_shoes.image, square_for_shoes.rect)
        window_surface.blit(ok.image, ok.rect)
        window_surface.blit(text_surface, (10, 5 ))
        
        if i == 1 :  # 顯示分數    
            if t < FPS*3:  # 跑三秒後顯示最終分數
                score = random.randint(500, 1000) /10  # 分數為 50 至 100 到小數點後一位的數字
                score_surface = my_score_font.render('{}'.format(score), True, (0, 0, 0))
                window_surface.blit(score_surface, (WINDOW_WIDTH/2 - 50, WINDOW_HEIGHT/2 - 50))
                t += 1
            else:
                score_surface = my_score_font.render('{}'.format(score), True, (0, 0, 0))
                window_surface.blit(score_surface, (WINDOW_WIDTH/2 - 50, WINDOW_HEIGHT/2 - 50))

        pygame.display.update()
        # 控制遊戲迴圈迭代速率
        main_clock.tick(FPS)
        

if __name__ == '__main__':    
    main()