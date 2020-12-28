
def game4_start():

    import sys, time
    import random
    import os

    import pygame
    import itertools
    from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    INTROWIDTH = 500
    INTROHEIGHT = 480
    BOSSWIDTH = 200
    BOSSHEIGHT = 300
    COMPUTERWIDTH = 300
    COMPUTERHEIGHT = 320
    PHONEWIDTH = 80
    PHONEHEIGHT = 100
    ADD300WIDTH = 200
    ADD300HEIGHT = 100
    MINUS300WIDTH = 200
    MINUS300HEIGHT = 100
    EMOJIWIDTH = 35
    EMOJIHEIGHT = 35
    FPS = 10
    intro_x_position = 50
    intro_y_position = 50
    boss_x_position = 5
    boss_y_position = 120
    computer_x_position = 200
    computer_y_position = 220
    phone_x_position = 480
    phone_y_position = 400
    add300_x_position = 150
    add300_y_position = 150
    minus300_x_position = 150
    minus300_y_position = 150
    emoji_x_position = 502
    emoji_y_position = 350
    show_probability1 = 50  # 每次顯示通知機率 (%)
    # show_probability2 = 30
    bosspath = os.path.abspath('G4-boss.png')
    computerpath = os.path.abspath('G4-computer.png')
    phonepath = os.path.abspath('G4-phone.png')
    intropath = os.path.abspath('G4-intro.png')
    add300path = os.path.abspath('G4-add300.gif')
    minus300path = os.path.abspath('G4-minus300.png')


    def print_sirting(academic_performance, romantic_relationship, wealth, health, text_surface_list):
        my_final_font = pygame.font.SysFont(None, 50)
        list_ = [academic_performance, romantic_relationship, wealth, health]
        for i in range(len(list_)):
            if list_[i] >= 0:
                list_[i] = '+' + str(list_[i])
            else:
                list_[i] = str(list_[i])

        text_surface_list.append(my_final_font.render(list_[1], True, (0, 0, 0)))
        text_surface_list.append(my_final_font.render(list_[2], True, (0, 0, 0)))
        text_surface_list.append(my_final_font.render(list_[3], True, (0, 0, 0)))
        text_surface_list.append(my_final_font.render(list_[0], True, (0, 0, 0)))
        



        return text_surface_list

    class Line(pygame.sprite.Sprite):
        def __init__(self, width, height, x_position, y_position, window_width, window_height, path):
            super().__init__()
            # 載入圖片
            self.raw_image = pygame.image.load(path).convert_alpha()
            # 縮小圖片
            self.image = pygame.transform.smoothscale(self.raw_image, (width, height))
            #  回傳位置
            self.rect = self.image.get_rect()
            #  定位
            self.rect.topleft = (x_position, y_position)
            self.width = width
            self.height = height
            self.window_width = window_width
            self.window_height = window_height
        

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
    game_over_time = 2
    ran_number = 10000


    while True:

        if game_over_time == 0 and pygame.time.get_ticks()-start_ticks > 20000:  # 遊戲打開 {} 秒後結束
            game_over_time = 1

        # 偵測事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == reload_line_event and game_over_time == 0:
                ran_number = random.randrange(0, 100)
                if ran_number < show_probability1:
                    BossIsHere = True
                    PATH = bosspath
                    boss = Line(BOSSWIDTH, BOSSHEIGHT, boss_x_position, boss_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                    #老闆出現
                elif ran_number > show_probability1:
                    # hide (藏在右下)
                    PATH = bosspath
                    boss = Line(BOSSWIDTH, BOSSHEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                    BossIsHere = False

            if event.type == MOUSEBUTTONDOWN and game_over_time == 0 and ran_number < show_probability1:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在電腦上
                if computer.rect.topleft[0] < pygame.mouse.get_pos()[0] < computer.rect.topleft[0] + COMPUTERWIDTH \
                   and computer.rect.topleft[1] < pygame.mouse.get_pos()[1] < computer.rect.topleft[1] + COMPUTERHEIGHT:
                    # 算分
                    salary += 300
                    PATH = add300path
                    add300 = Line(ADD300WIDTH, ADD300HEIGHT, add300_x_position, add300_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                    window_surface.blit(add300.image, add300.rect)
                    pygame.display.flip() 
                                        
                else:
                    salary -= 300
                    PATH = minus300path
                    minus300 = Line(MINUS300WIDTH, MINUS300HEIGHT, minus300_x_position, minus300_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, PATH) 
                    window_surface.blit(minus300.image, minus300.rect)
                    pygame.display.flip()
                
                if salary <= 0:
                    salary = 0

            elif event.type == MOUSEBUTTONDOWN and game_over_time == 0 and ran_number > show_probability1:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在手機上
                if phone.rect.topleft[0] < pygame.mouse.get_pos()[0] < phone.rect.topleft[0] + PHONEWIDTH \
                   and phone.rect.topleft[1] < pygame.mouse.get_pos()[1] < phone.rect.topleft[1] + PHONEHEIGHT:
                   
                    # 算分
                    satisfaction += 300
                    ran_number1 = random.randrange(0, 100)
                    if ran_number1 < 50:
                        emojipath = os.path.abspath('partyface.png')
                    else:
                        emojipath = os.path.abspath('love.png')
                    emoji = Line(EMOJIWIDTH, EMOJIHEIGHT, emoji_x_position, emoji_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, emojipath)
                    window_surface.blit(emoji.image, emoji.rect)
                    pygame.display.flip()
                
                else:
                    satisfaction -= 300
                    ran_number1 = random.randrange(0, 100)
                    

                if satisfaction <= 0:
                    satisfaction = 0
                    
            # 遊戲結束之後按下 RESUME 之後的動作
            elif event.type == MOUSEBUTTONDOWN and game_over_time == 1:
                if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                        and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                    return romantic_relationship, wealth, 0, academic_performance, health

            elif event.type == MOUSEBUTTONDOWN and game_over_time == 2:
                if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                        and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                    start_ticks = pygame.time.get_ticks()
                    game_over_time = 0

        if game_over_time == 0:  # 遊戲畫面

            # 倒數計時器
            seconds = 30 - (pygame.time.get_ticks()-start_ticks)//1000

            clock_surface = my_font.render(
                "00:%02d" % seconds, True, (0, 0, 0))

            # 遊戲分數儀表板
            text_surface = my_font.render(
                'salary = {}'.format(round(salary, 2)), True, (0, 0, 0))
            # 渲染物件
            background_raw = pygame.image.load(
                'G4-background.jpg')
            # 調整背景圖片大小
            background = pygame.transform.scale(
                background_raw, (WINDOW_WIDTH, WINDOW_HEIGHT))
            background.convert()
            window_surface.blit(background, (0, 0))
            window_surface.blit(computer.image, computer.rect)
            window_surface.blit(phone.image, phone.rect)
            window_surface.blit(boss.image, boss.rect)      
            window_surface.blit(text_surface, (10, 5))
            BossIsHere = False
            
            # cursor
            if computer.rect.topleft[0] < pygame.mouse.get_pos()[0] < computer.rect.topleft[0] + computer.width \
                and computer.rect.topleft[1] < pygame.mouse.get_pos()[1] < computer.rect.topleft[1] + computer.height:
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            elif phone.rect.topleft[0] < pygame.mouse.get_pos()[0] < phone.rect.topleft[0] + phone.width \
                and phone.rect.topleft[1] < pygame.mouse.get_pos()[1] < phone.rect.topleft[1] + phone.height:
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)

        elif game_over_time == 1:
            # 計算分數

            if salary >= 1800:
                academic_performance = 30
                wealth = 30

            elif 1200 <= salary < 1800:
                academic_performance = 20
                wealth = 20

            elif 800 <= salary < 1200:
                academic_performance = 0
                wealth = 0

            elif 0 <= salary < 800:
                academic_performance = -30
                wealth = -30

            if satisfaction >= 1800:
                romantic_relationship = 30
                health = 30
            elif 1200 <= satisfaction < 1800:
                romantic_relationship = 20
                health = 20
            elif 800 <= satisfaction < 1200:
                romantic_relationship = 0
                health = 0
            elif 0 <= satisfaction < 800:
                romantic_relationship = -30
                health = -30
            text_surface_list = []

            text_surface_list = print_sirting(academic_performance, romantic_relationship, wealth, health, text_surface_list)
            love = Line(60, 60, 50, 50,
                       WINDOW_WIDTH, WINDOW_HEIGHT, 'love.png')
            money = Line(60, 60, 50, 50 + 70*1,
                        WINDOW_WIDTH, WINDOW_HEIGHT, 'money.png')
            health = Line(60, 60, 50,
                         50+70*2, WINDOW_WIDTH, WINDOW_HEIGHT, 'friend.png')
            study = Line(60, 60, 50,
                          50+70*3, WINDOW_WIDTH, WINDOW_HEIGHT, 'study.png')

            item_list = [love, money, health, study]
            group = pygame.sprite.Group()
            for item in item_list:
                group.add(item)
            # 渲染物件
            background_raw = pygame.image.load(os.path.abspath('G4-background2.jpg'))
            # 調整背景圖片大小
            background = pygame.transform.scale(background_raw, (WINDOW_WIDTH , WINDOW_HEIGHT ))
            background.convert()
            window_surface.blit(background, (0,0))
            group.draw(window_surface)
            RESUME = Line(157, 34, 400,
                          500, WINDOW_WIDTH, WINDOW_HEIGHT, 'back_to_map.png')
            window_surface.blit(RESUME.image, RESUME.rect)
            for i in range(len(text_surface_list)):
                window_surface.blit(
                    text_surface_list[i], (int(141*0.9), int(68*0.9) + 70*i))  # text position
        
        elif game_over_time == 2:  # 遊戲說明畫面
            background_raw = pygame.image.load('G4-background2.jpg')
            # 調整背景圖片大小
            
            background = pygame.transform.scale(
                background_raw, (WINDOW_WIDTH, WINDOW_HEIGHT))
            background.convert()
            window_surface.blit(background, (0, 0))
            RESUME = Line(157, 34, 400,
                          500, WINDOW_WIDTH, WINDOW_HEIGHT, 'play.png')
            window_surface.blit(RESUME.image, RESUME.rect)
            
            # cursor
            if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            
            intro = Line(INTROWIDTH, INTROHEIGHT, intro_x_position, intro_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, intropath)
            window_surface.blit(intro.image, intro.rect)

        pygame.display.update()
        # 控制遊戲迴圈迭代速率
        main_clock.tick(FPS)

if __name__ == '__main__':
    print(game4_start())
