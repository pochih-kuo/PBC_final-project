

def game3():
    
    import sys, time
    import random

    import pygame
    from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT
    
    # ---------------------------
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    IMAGEWIDTH = 100
    IMAGEHEIGHT = 100
    FPS = 10
    SPACING = 50
    FIRST_X_POSITION = 100
    FIRST_Y_POSITION = 50

    pathes = ['clothes1.png', 'clothes2.png', 'clothes3.png', 'pants1.png', 'pants2.png', 'pants3.png', 'shoes1.png', 'shoes2.png', 'shoes3.png']
    point_list = [1,2,3, 4, 5, 6, 7, 8, 9]
    # ---------------------------

    class Picture(pygame.sprite.Sprite):
        def __init__(self, x_position, y_position, path, point):
            super().__init__()
            # 載入圖片
            self.raw_image = pygame.image.load('G3-'+path).convert_alpha()
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
    
    
    pygame.init()

    # load window surface
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Choose Wisely')
    group = pygame.sprite.Group()
    ok = Picture(300-40, 480,'ok.png', 0)
    ok.image = pygame.transform.scale(ok.raw_image, (94, 68))
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
    my_score_font = pygame.font.SysFont(None, 90)
    main_clock = pygame.time.Clock()
    page = 0
    t = 0
    
    while True:
        
        # 偵測事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN and page == 1:
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
                    page = 2

            elif event.type == MOUSEBUTTONDOWN and page == 0:
                if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                    and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                    page = 1

            elif event.type == MOUSEBUTTONDOWN and page == 2:
                if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                    and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                    return romantic_relationship, money, health, academic_performance, interpersonal_relationship
  
        if page == 1:  # 遊戲畫面
        
            # cursor
            touch = 0
            for item in list:
                if item.rect.topleft[0] < pygame.mouse.get_pos()[0] < item.rect.topleft[0] + IMAGEWIDTH \
                    and item.rect.topleft[1] < pygame.mouse.get_pos()[1] < item.rect.topleft[1] + IMAGEHEIGHT:
                    # pygame.mouse.set_cursor(*pygame.cursors.diamond)
                    touch = 1
                    break

            if ok.rect.topleft[0] < pygame.mouse.get_pos()[0] < ok.rect.topleft[0] + 80 \
                and ok.rect.topleft[1] < pygame.mouse.get_pos()[1] < ok.rect.topleft[1] + 80:
                touch = 1
                # pygame.mouse.set_cursor(*pygame.cursors.diamond)
            
            if touch == 1:
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            
            # 計分
            points = clothes_points + pants_point + shoes_point
            # 遊戲分數儀表板
            text_surface = my_font.render('$$ = {}'.format(round(points,2)), True, (0, 0, 0))
            # 渲染物件
            background_raw = pygame.image.load('G3-background.jpg')
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
        
        elif page == 2 :  # 顯示分數    
        
            # cursor
            if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            
            points = clothes_points + pants_point + shoes_point
            # 遊戲分數儀表板
            text_surface = my_font.render('$$ = {}'.format(round(points,2)), True, (0, 0, 0))
            # 渲染物件
            background_raw = pygame.image.load('G3-background2.jpg')
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
            
            class Line(pygame.sprite.Sprite):
                def __init__(self, width, height, x_position, y_position, window_width, window_height, path):
                    super().__init__()
                    # 載入圖片
                    self.raw_image = pygame.image.load('G3-'+path).convert_alpha()
                    # 縮小圖片
                    self.image = pygame.transform.scale(
                        self.raw_image, (width, height))
                    #  回傳位置
                    self.rect = self.image.get_rect()
                    #  定位
                    self.rect.topleft = (x_position, y_position)
                    self.width = width
                    self.height = height
                    self.window_width = window_width
                    self.window_height = window_height

            def print_sirting(academic_performance, romantic_relationship, interpersonal_relationship, money, text_surface_list):
                my_final_font = pygame.font.SysFont(None, 60)

                list_ = [romantic_relationship, money, academic_performance,
                         interpersonal_relationship]

                for i in range(len(list_)):
                    if list_[i] >= 0:
                        list_[i] = '+' + str(list_[i])
                    else:
                        list_[i] = str(list_[i])

                    text_surface_list.append(my_final_font.render(
                        list_[i], True, (0, 0, 0)))
                    # text_surface_list.append(my_space_font.render(
                    # ' ', True, (0, 0, 0)))

                return text_surface_list
            
            if t < FPS*3:  # 跑三秒後顯示最終分數
                score = random.randint(500, 1000) /10  # 分數為 50 至 100 到小數點後一位的數字
                score_surface = my_score_font.render('{}'.format(score), True, (0, 0, 0))
                window_surface.blit(score_surface, (WINDOW_WIDTH/2 - 75, 100))

                t += 1
            else:
                score_surface = my_score_font.render('{}'.format(score), True, (0, 0, 0))
                window_surface.blit(score_surface, (WINDOW_WIDTH/2 - 75, 100))
                # icons
                love = Line(60, 60, 200, 
                            140 + 70*1, WINDOW_WIDTH, WINDOW_HEIGHT, 'love.png')
                money = Line(60, 60, 200,
                            140+70*2, WINDOW_WIDTH, WINDOW_HEIGHT, 'money.png')
                study = Line(60, 60, 200,
                            140+70*3, WINDOW_WIDTH, WINDOW_HEIGHT, 'study.png')
                friend = Line(60, 60, 200,
                            140+70*4, WINDOW_WIDTH, WINDOW_HEIGHT, 'friend.png')
                item_list = [love, money, study, friend]
                group = pygame.sprite.Group()
                for item in item_list:
                    group.add(item)
                
                # 計算分數與顯示
                health = 0
                if score <= 60:
                    academic_performance = -30
                    romantic_relationship = -30
                    interpersonal_relationship = 10
                elif 60 < score <= 70:
                    academic_performance = -10
                    romantic_relationship = -20
                    interpersonal_relationship = 10
                elif 70 < score <= 80:
                    academic_performance = 0
                    romantic_relationship = 10
                    interpersonal_relationship = 10
                elif 80 < score <= 90:
                    academic_performance = 10
                    romantic_relationship = 10
                    interpersonal_relationship = 0
                else: # score > 90
                    academic_performance = 30
                    romantic_relationship = 0  # 學霸加成
                    interpersonal_relationship = 10
                
                if points < 12:
                    money = 30
                elif 12 <= points < 14:
                    money = -10
                elif 14 <= points < 16:
                    money = -20
                elif 16 <= points < 18:
                    money = -25
                else:  # points = 18
                    money = -30
                
                text_surface_list = []
                text_surface_list = print_sirting(
                                              academic_performance, romantic_relationship,
                                              interpersonal_relationship, money, text_surface_list)
                RESUME = Line(242, 34, 300,
                          500, WINDOW_WIDTH, WINDOW_HEIGHT, 'back_to_map.png')
                window_surface.blit(RESUME.image, RESUME.rect)
                for i in range(len(text_surface_list)):
                    window_surface.blit(
                        text_surface_list[i], (300, 220 + 70*i))  # text position

        elif page == 0:  # 遊戲說明畫面
        
            # RESUME button
            RESUME = Picture(400, 400, 'play.png', 0)
            RESUME.image = pygame.transform.scale(RESUME.raw_image, (117, 34))
            RESUME.width = 117
            RESUME.height = 34


            # cursor
            if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            
            # 渲染物件
            background_raw = pygame.image.load(
                'G3-background2.jpg')
            background = pygame.transform.scale(
                background_raw, (WINDOW_WIDTH, WINDOW_HEIGHT))
            background.convert()
            window_surface.blit(background, (0, 0))

            intro_raw = pygame.image.load('G3-intro1.png')
            intro = pygame.transform.smoothscale(
                intro_raw, (WINDOW_WIDTH, WINDOW_HEIGHT))
            window_surface.blit(intro, (0, 0))            
            window_surface.blit(RESUME.image, RESUME.rect)

        pygame.display.update()
        # 控制遊戲迴圈迭代速率
        main_clock.tick(FPS)
        

if __name__ == '__main__':    
    game3()