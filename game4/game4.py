import sys, time
import random
import os

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BOSSWIDTH = 150
BOSSHEIGHT = 470
COMPUTERWIDTH = 300
COMPUTERHEIGHT = 320
PHONEWIDTH = 40
PHONEHEIGHT = 50
FPS = 10
boss_x_position = 30
boss_y_position = 120
computer_x_position = 150
computer_y_position = 220
phone_x_position = 400
phone_y_position = 470
show_probability1 = 60  # 每次顯示通知機率 (%)
# show_probability2 = 30
bosspath = os.path.abspath('boss.gif')
computerpath = os.path.abspath('computer.gif')
phonepath = os.path.abspath('phone.gif')


def print_sirting(academic_performance, romantic_relationship, wealth, health, text_surface_list):
    my_final_font = pygame.font.SysFont(None, 50)
    list_ = [academic_performance, romantic_relationship, wealth, health]
    for i in range(len(list_)):
        if list_[i] >= 0:
            list_[i] = '+' + str(list_[i])
        else:
            list_[i] = str(list_[i])

    text_surface_list.append(my_final_font.render('academic performance = ' + list_[0], True, (0, 0, 0)))
    text_surface_list.append(my_final_font.render('romantic relationship = ' + list_[1], True, (0, 0, 0)))
    text_surface_list.append(my_final_font.render('wealth = ' + list_[2], True, (0, 0, 0)))
    text_surface_list.append(my_final_font.render('health = ' + list_[3], True, (0, 0, 0)))

    return text_surface_list

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
    pygame.display.set_caption('Maximize Your Utility!')
    computer = Line(COMPUTERWIDTH, COMPUTERHEIGHT, computer_x_position, computer_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, computerpath)
    phone = Line(PHONEWIDTH, PHONEHEIGHT, phone_x_position, phone_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, phonepath)
    boss = Line(BOSSWIDTH, BOSSHEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, bosspath)
    reload_line_event = USEREVENT + 1
    pygame.time.set_timer(reload_line_event, 2000)  # 更新頻率(unit = ms)

    salary = 1000  # 初始薪水 : 1000
    satisfaction = 1000  #初始滿足程度
    my_font = pygame.font.SysFont('mingliu', 30)
    my_final_font = pygame.font.SysFont(None, 50)
    hit_text_surface = None
    main_clock = pygame.time.Clock()
    game_over_time = 0


    while True:
        if pygame.time.get_ticks() > 10000:  # 遊戲打開 {} 秒後自動關閉
            game_over_time = 1

        # 偵測事件
        for event in pygame.event.get():
            BossIsHere = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == reload_line_event and game_over_time == 0:
                ran_number = random.randrange(0, 100)
                if ran_number < show_probability1:
                    PATH = bosspath
                    boss = Line(BOSSWIDTH, BOSSHEIGHT, boss_x_position, boss_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                    BossIsHere = True  #老闆出現
                else:
                    # hide (藏在右下)
                    PATH = bosspath
                    boss = Line(BOSSWIDTH, BOSSHEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                    BossIsHere = False

            if event.type == MOUSEBUTTONDOWN and game_over_time == 0 and BossIsHere is True:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在電腦上
                if computer.rect.topleft[0] < pygame.mouse.get_pos()[0] < computer.rect.topleft[0] + COMPUTERWIDTH \
                   and computer.rect.topleft[1] < pygame.mouse.get_pos()[1] < computer.rect.topleft[1] + COMPUTERHEIGHT:
                    # 算分
                    salary += 300
                else:
                    salary -= 300

                if salary <= 0:
                    salary = 0

            elif event.type == MOUSEBUTTONDOWN and game_over_time == 0 and BossIsHere is False:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在手機上
                if phone.rect.topleft[0] < pygame.mouse.get_pos()[0] < phone.rect.topleft[0] + PHONEWIDTH \
                   and phone.rect.topleft[1] < pygame.mouse.get_pos()[1] < phone.rect.topleft[1] + PHONEHEIGHT:
                   
                    # 算分
                    satisfaction += 300
                
                else:
                    satisfaction -= 300

                if satisfaction <= 0:
                    satisfaction = 0

        if game_over_time == 0:  # 遊戲畫面

            # 遊戲分數儀表板
            text_surface = my_font.render('salary = {}'.format(round(salary,2)), True, (0, 0, 0))
            # 渲染物件
            background_raw = pygame.image.load(os.path.abspath('background.jpg'))
            # 調整背景圖片大小
            background = pygame.transform.scale(background_raw, (WINDOW_WIDTH , WINDOW_HEIGHT ))
            background.convert()
            window_surface.blit(background, (0,0))
            window_surface.blit(boss.image, boss.rect)
            window_surface.blit(computer.image, computer.rect)
            window_surface.blit(phone.image, phone.rect)
            window_surface.blit(text_surface, (10, 5 ))

        elif game_over_time == 1:
            # 計算分數

            if salary >= 1800:
                academic_performance = 30
                wealth = 30

            elif 1200 <= salary < 1800:
                academic_performance = 20
                wealth = 20

            elif 800 <= salary < 1200:
                academic_performance = 10
                wealth = 10

            elif 0 <= salary < 800:
                academic_performance = 0
                wealth = 0

            if satisfaction >= 1800:
                romantic_relationship = 30
                health = 30
            elif 1200 <= satisfaction < 1800:
                romantic_relationship = 20
                health = 20
            elif 800 <= satisfaction < 1200:
                romantic_relationship = 10
                health = 10
            elif 0 <= satisfaction < 800:
                romantic_relationship = 0
                health = 0
            text_surface_list = []

            text_surface_list.append(my_final_font.render('salary = {}'.format(round(salary,2)), True, (0, 0, 0)))

            text_surface_list = print_sirting(academic_performance, romantic_relationship, wealth, health, text_surface_list)
            # 渲染物件
            background_raw = pygame.image.load(os.path.abspath('background2.png'))
            # 調整背景圖片大小
            background = pygame.transform.scale(background_raw, (WINDOW_WIDTH , WINDOW_HEIGHT ))
            background.convert()
            window_surface.blit(background, (0,0))
            for i in range(len(text_surface_list)):
                window_surface.blit(text_surface_list[i], (10, 5 + 50*i))  # text position

        # 顯示提示文字(oops)
        # if hit_text_surface:
            # window_surface.blit(hit_text_surface, (400, 300))
            # hit_text_surface = None


        pygame.display.update()
        # 控制遊戲迴圈迭代速率
        main_clock.tick(FPS)


if __name__ == '__main__':
    main()
