
def game2_start():

    import sys
    import time
    import random

    import pygame
    from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    IMAGEWIDTH = 140
    IMAGEHEIGHT = int(IMAGEWIDTH/9*16)
    FPS = 10
    line_x_position = 53
    line_y_position = 233
    show_probability1 = 60  # 每次顯示通知機率 (%)
    # show_probability2 = 30
    path2 = 'G2-game2_msg1.png'
    path1 = 'G2-game2_msg2.png'
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

    def print_sirting(point, academic_performance, romantic_relationship, interpersonal_relationship, health_value, text_surface_list):
        my_final_font = pygame.font.SysFont(None, 60)
        my_space_font = pygame.font.SysFont(None, 10)
        list_ = [point, romantic_relationship, health_value, academic_performance,
                 interpersonal_relationship]
        list_[0] = '      = ' + str(list_[0])
        text_surface_list.append(my_final_font.render(
            list_[0], True, (0, 0, 0)))
        for i in range(1, len(list_)):
            if list_[i] >= 0:
                list_[i] = '+' + str(list_[i])
            else:
                list_[i] = str(list_[i])

            text_surface_list.append(my_final_font.render(
                list_[i], True, (0, 0, 0)))
            # text_surface_list.append(my_space_font.render(
            # ' ', True, (0, 0, 0)))

        return text_surface_list

    pygame.init()

    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Stop Procrastinating!')

    line = Line(IMAGEWIDTH, IMAGEHEIGHT, WINDOW_WIDTH,
                WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, path1)
    reload_line_event = USEREVENT + 1
    pygame.time.set_timer(reload_line_event, 2000)  # 更新頻率(unit = ms)

    increase_score_event = USEREVENT + 2
    pygame.time.set_timer(increase_score_event, 5000)  # 加分頻率(unit = ms)

    i = 4
    points = gpa_lsit[i]  # 初始分數 : 3.0
    my_font = pygame.font.SysFont(None, 30)
    my_final_font = pygame.font.SysFont(None, 50)
    hit_text_surface = None
    main_clock = pygame.time.Clock()
    game_over_time = 2
    seconds = 0
    milliseconds = 0

    while True:

        if game_over_time == 0 and pygame.time.get_ticks()-start_ticks > 30001:  # 遊戲打開 {} 秒後結束
            game_over_time = 1

        # 偵測事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == reload_line_event and game_over_time == 0:
                ran_number = random.randrange(0, 100)
                # 重新整理
                if ran_number < show_probability1 and i <= 1:  # GPA >= 4.0
                    # show
                    PATH = path1  # 小美生氣圖
                    line = Line(IMAGEWIDTH, IMAGEHEIGHT, line_x_position,
                                line_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                elif ran_number < show_probability1 and i > 1:  # GPA < 4.0
                    # show
                    PATH = path2
                    line = Line(IMAGEWIDTH, IMAGEHEIGHT, line_x_position,
                                line_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                else:
                    # hide (藏在右下)
                    PATH = path1
                    line = Line(IMAGEWIDTH, IMAGEHEIGHT, WINDOW_WIDTH,
                                WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)

            elif event.type == MOUSEBUTTONDOWN and game_over_time == 0:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在圖片上
                if line.rect.topleft[0] < pygame.mouse.get_pos()[0] < line.rect.topleft[0] + IMAGEWIDTH \
                        and line.rect.topleft[1] < pygame.mouse.get_pos()[1] < line.rect.topleft[1] + IMAGEHEIGHT:

                    PATH = path1
                    line = Line(IMAGEWIDTH, IMAGEHEIGHT, WINDOW_WIDTH,
                                WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)

                    # 算分
                    i += 1
                    if i < 10:
                        points = gpa_lsit[i]
                    else:
                        points = 0

            elif event.type == increase_score_event and game_over_time == 0:  # 每十秒加一個等第
                if i > 0:
                    i -= 1
                    points = gpa_lsit[i]

            # 遊戲結束之後按下 RESUME 之後的動作
            elif event.type == MOUSEBUTTONDOWN and game_over_time == 1:
                if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                        and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                    return romantic_relationship, money_value, health_value, academic_performance,\
                        interpersonal_relationship

            elif event.type == MOUSEBUTTONDOWN and game_over_time == 2:
                if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                        and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                    start_ticks = pygame.time.get_ticks()
                    game_over_time = 0

        if game_over_time == 0:  # 遊戲畫面
        
            # cursor
            if line.rect.topleft[0] < pygame.mouse.get_pos()[0] < line.rect.topleft[0] + line.width \
                and line.rect.topleft[1] < pygame.mouse.get_pos()[1] < line.rect.topleft[1] + line.height:
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)

            # 倒數計時器
            seconds = 30 - (pygame.time.get_ticks()-start_ticks)//1000

            clock_surface = my_font.render(
                "00:%02d" % seconds, True, (0, 0, 0))

            # milliseconds += 1/FPS*1000*2  #returns the time since the last time we called the function, and limits the frame rate to 60FPS

            # 遊戲分數儀表板
            text_surface = my_font.render(
                'GPA = {}'.format(round(points, 2)), True, (0, 0, 0))
            # 渲染物件
            background_raw = pygame.image.load(
                'G2-background.jpg')
            # 調整背景圖片大小
            background = pygame.transform.scale(
                background_raw, (WINDOW_WIDTH, WINDOW_HEIGHT))
            background.convert()
            window_surface.blit(background, (0, 0))
            # phone = Line(360, 360, 28,
                                # 140, WINDOW_WIDTH, WINDOW_HEIGHT, 'G2-iphone7.png')
            # window_surface.blit(phone.image, phone.rect)
            window_surface.blit(line.image, line.rect)
            window_surface.blit(text_surface, (10, 25))
            window_surface.blit(clock_surface, (10, 5))

        elif game_over_time == 1:  # 計分畫面

            # 計算分數
            money_value = 0  # 本遊戲不計算 money 分數
            if points <= 1:
                academic_performance = -30
                romantic_relationship = 30
                interpersonal_relationship = 10
                health_value = -20

            elif 1 < points <= 2:
                academic_performance = -10
                romantic_relationship = 20
                interpersonal_relationship = 10
                health_value = 0

            elif 2 < points <= 3:
                academic_performance = 0
                romantic_relationship = 10
                interpersonal_relationship = 10
                health_value = -10

            elif 3 < points <= 4:
                academic_performance = 10
                romantic_relationship = -10
                interpersonal_relationship = 0
                health_value = 10

            else:
                academic_performance = 30
                romantic_relationship = 0  # 學霸加成
                interpersonal_relationship = 10
                health_value = 20


            text_surface_list = []

            text_surface_list = print_sirting(points,
                                              academic_performance, romantic_relationship,
                                              interpersonal_relationship, health_value, text_surface_list)

            GPA = Line(int(141*0.9), int(68*0.9), 50, 50,
                       WINDOW_WIDTH, WINDOW_HEIGHT, 'G2-gpa.png')
            love = Line(60, 60, 50, 50 + 70*1,
                        WINDOW_WIDTH, WINDOW_HEIGHT, 'love.png')
            #money = Line(60, 60, 50,
                         #50+70*2, WINDOW_WIDTH, WINDOW_HEIGHT, 'money.png')
            health = Line(60, 60, 50,
                          50+70*2, WINDOW_WIDTH, WINDOW_HEIGHT, 'health.png')
            study = Line(60, 60, 50,
                         50+70*3, WINDOW_WIDTH, WINDOW_HEIGHT, 'study.png')
            friend = Line(60, 60, 50,
                          50+70*4, WINDOW_WIDTH, WINDOW_HEIGHT, 'friend.png')
            item_list = [GPA, love, health, study, friend]
            group = pygame.sprite.Group()
            for item in item_list:
                group.add(item)
                
            # cursor
            if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                

            # 渲染物件
            background_raw = pygame.image.load(
                'G2-background2.jpg')
            # 調整背景圖片大小
            background = pygame.transform.scale(
                background_raw, (WINDOW_WIDTH, WINDOW_HEIGHT))
            background.convert()
            window_surface.blit(background, (0, 0))
            group.draw(window_surface)
            RESUME = Line(157, 34, 400,
                          500, WINDOW_WIDTH, WINDOW_HEIGHT, 'G2-resume.png')
            window_surface.blit(RESUME.image, RESUME.rect)
            for i in range(len(text_surface_list)):
                window_surface.blit(
                    text_surface_list[i], (int(141*0.9), int(68*0.9) + 70*i))  # text position
                    
            

        elif game_over_time == 2:  # 遊戲說明畫面
        
            RESUME = Line(int(185/2), int(67/2), 400,
                          430, WINDOW_WIDTH, WINDOW_HEIGHT, 'G2-play.png')
            # cursor
            if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)       
                
            background_raw = pygame.image.load(
                'G2-intro1.png')
            # 調整背景圖片大小
            background = pygame.transform.scale(
                background_raw, (WINDOW_WIDTH, WINDOW_HEIGHT))
            background.convert()
            window_surface.blit(background, (0, 0))
            window_surface.blit(RESUME.image, RESUME.rect)
            # intro_text = my_final_font.render('this is the introduction.', True, (0, 0, 0))
            # window_surface.blit(intro_text, (10, 10))
            

        pygame.display.update()
        # 控制遊戲迴圈迭代速率
        main_clock.tick(FPS)


if __name__ == '__main__':
    print(game2_start())
