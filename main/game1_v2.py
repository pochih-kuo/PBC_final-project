def game1_start():
    FPS = 60
    PLAYER_SPEED_X = 5
    space = pygame.image.load('G1-background.png')
    pygame.init()
    
    
    
    
    health = pygame.image.load("G1-health.png")
    money = pygame.image.load("G1-money.png")
    friend = pygame.image.load("G1-friend.png")
#--------------------------------------------------------------------------------------------------------
    window_surface = pygame.display.set_mode((600, 600))
    WINDOW_WIDTH=600
    WINDOW_HEIGHT=600

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

#---------------------------------------------------------------------------------------------------------
    class Student:
        def __init__(self):
            # self.game = game
            self.pos_x = (600 *0.45)
            self.pos_y = (600 * 0.8)
            self.direction_x = 0
            self.speed_x = 15
            self.studentImg = pygame.image.load('G1-student.png').convert_alpha()
            self.rect = self.studentImg.get_rect()
            self.rect.topleft = (self.pos_x, self.pos_y)    # 左上角
        
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.direction_x = -1
            elif keys[pygame.K_RIGHT]:
                    self.direction_x = 1 
            else:
                self.direction_x = 0
            self.pos_x += self.direction_x * self.speed_x
            if self.pos_x <= 0:
                self.pos_x = 0
            elif self.pos_x + 29 >= 600:    # 加上student的寬度
                self.pos_x = 571
                
            self.rect.topleft = (self.pos_x, self.pos_y)
                
        def draw(self):
            gameDisplay.blit(self.studentImg, (self.pos_x, self.pos_y))

    class Stone:
        def __init__(self):
            # self.game = game
            self.pos_x = randint(0, 565)
            self.pos_y = -50
            self.speed_y = randint(5, 20)
            self.stoneImg = pygame.image.load('G1-stone.png').convert_alpha()
            self.rect = self.stoneImg.get_rect()
            self.rect.topleft = (self.pos_x, self.pos_y)
        
        def update(self):
            self.pos_y += self.speed_y
            self.rect.topleft = (self.pos_x, self.pos_y)
        
        def draw(self):
            gameDisplay.blit(self.stoneImg, (self.pos_x, self.pos_y))

    def collision_check(obj_one, obj_two):
        pos_one = obj_one.rect.topleft
        pos_two = obj_two.rect.topleft
        width_one = obj_one.rect.width
        height_one = obj_one.rect.height
        width_two = obj_two.rect.width
        height_two = obj_two.rect.height
        
        if (pos_two[1] < pos_one[1] and pos_two[1] + height_two >= pos_one[1]) or \
            (pos_two[1] >= pos_one[1] and pos_two[1] + height_two <= pos_one[1] + height_one) or \
            (pos_two[1] <= pos_one[1] + height_one and pos_two[1] + height_two > pos_one[1] + height_one):
            if (pos_two[0] < pos_one[0] and pos_two[0] + width_two >= pos_one[0]) or \
                (pos_two[0] >= pos_one[0] and pos_two[0] + width_two <= pos_one[0] + width_one) or \
                (pos_two[0] <= pos_one[0] + width_one and pos_two[0] + width_two > pos_one[0] + width_one):
                return True
                
        return False

    def draw_text(text, size, color, x, y):
        font = pygame.font.SysFont('SourceHanSansTC-Bold.otf', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        gameDisplay.blit(text_surface, text_rect)

    gameDisplay = pygame.display.set_mode((600, 600))
    #pygame.display.set_caption('Dodge people on Palm Avenue!')
    clock = pygame.time.Clock()
    last_spawn_stone = pygame.time.get_ticks()    # 獲取時間(毫秒)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill((0, 0, 0))
#-----------------------------------------------------------------------------------------------
        RESUME = Line(157, 34, 350,400, 600, 600, 'G2-resume.png')
            # cursor
        if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
            and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)       

        background_raw = pygame.image.load('G2-intro1.png')
        background = pygame.transform.scale(background_raw, (600, 600))
        background.convert()
        window_surface.blit(background, (0, 0))
        window_surface.blit(RESUME.image, RESUME.rect)
        

        # button("Start", 250, 350, 100, 50,(200, 0, 0), (255, 0, 0))    # button    # new

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
            and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
            if click[0] == 1:
                
                #new()
                stones = []

                student = Student()

                while True:
                    if pygame.time.get_ticks() > 25000:    #25秒
                        draw_text("You AG!", 80, (255, 255, 255), 300, 300)
                        final = 0
                        pygame.display.update()
                        time.sleep(1)
                        gameDisplay.fill((255, 255, 255))
                        gameDisplay.blit(space, (0,0,600,600)) 
                        pygame.display.update()
                        time.sleep(1)
                        gameDisplay.blit(health, (60,60,50,70))
                        gameDisplay.blit(friend, (60,140,50,140))
                        draw_text("+20", 60, (0,0,0),160,100)
                        draw_text("+20", 60, (0,0,0),160,170)
                        #draw_text("academic_performance = 60", 20, (255, 255, 255), 300, 300)
                        #draw_text("romantic_relationship = 60", 20, (255, 255, 255), 300, 275)
                        #draw_text("interpersonal_relationship = 60", 20, (255, 255, 255), 300, 250)
                        #draw_text("health = 60", 20, (255, 255, 255), 300, 225)
                        #draw_text("wealth = 60", 20, (255, 255, 255), 300, 200)
                        pygame.display.update()
                        ######印出減分
                        time.sleep(5)
                        romantic_relationship = 0
                        money = 0
                        health_value = +20
                        academic_performance = 0
                        interpersonal_relationship = +20
                        return romantic_relationship, money, health_value, academic_performance,interpersonal_relationship
                        
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    #update()
                    now = pygame.time.get_ticks()
                    if now - last_spawn_stone >= 800:
                        stones.append(Stone())
                        last_spawn_stone = now
                        
                    student.update()    # 更新學生
                    
                    for stone in stones:
                        stone.update()    # 更新石頭
                        if stone.pos_y >= 600:    # 如果石頭超出範圍，除掉
                            stones.remove(stone)

                    for stone in stones:    # 每顆石頭檢查碰撞
                        if collision_check(student, stone):    # collision_check
                            final = 1
                            draw_text("Lose!", 80, (255, 255, 255), 300, 300)
                            pygame.display.update()
                            time.sleep(1)
                            gameDisplay.fill((255, 255, 255))
                            gameDisplay.blit(space, (0,0,600,600)) 
                            pygame.display.update()
                            time.sleep(1)
                            gameDisplay.blit(health, (60,60,50,70))
                            gameDisplay.blit(money, (60,140,50,140))
                            gameDisplay.blit(friend, (60,210,50,210))
                            draw_text("-30", 60, (0,0,0),160,100)
                            draw_text("-30", 60, (0,0,0),160,170)
                            draw_text("-20", 60, (0,0,0),160,240)
                            #draw_text("academic_performance = 60", 20, (255, 255, 255), 300, 300)
                            #draw_text("romantic_relationship = 60", 20, (255, 255, 255), 300, 275)
                            #draw_text("interpersonal_relationship = 40", 20, (255, 255, 255), 300, 250)
                            #draw_text("health = 30", 20, (255, 255, 255), 300, 225)
                            #draw_text("wealth = 30", 20, (255, 255, 255), 300, 200)
                            
                            pygame.display.update()
                            time.sleep(5)
                            romantic_relationship = 0
                            money = -30
                            health_value = -30
                            academic_performance = 0
                            interpersonal_relationship = -20

                            return romantic_relationship, money, health_value, academic_performance,interpersonal_relationship

                    
                    #draw()
                    gameDisplay.fill((255, 255, 255))
                    gameDisplay.blit(space, (0,0,600,600))
                    student.draw()
                    for stone in stones:
                        stone.draw()
                    pygame.display.update()
                    clock.tick(60)

        else:
            pass

        pygame.display.update()
        clock.tick(30)