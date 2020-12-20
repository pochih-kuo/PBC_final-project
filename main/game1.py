# 可以把整個 code 複製貼上, 並用五個參數接這個function (return in line 27)
def game1_start():
    import sys, math
    import pygame
    from random import randint
    import time
    
    FPS = 60
    PLAYER_SPEED_X = 5
    space = pygame.image.load('G1-background.png')
    game = Game()
    game.game_intro()
    if game.collision_check == True:
        romantic_relationship = 60
        money = 30
        health = 30
        academic_performance = 60
        interpersonal_relationship = 40
    
    else:
        romantic_relationship = 60
        money = 60
        health = 60
        academic_performance = 60
        interpersonal_relationship = 60
    
    return romantic_relationship, money, health, academic_performance,interpersonal_relationship
    
    
    class Student:
        def __init__(self, game):
            self.game = game
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
		self.game.gameDisplay.blit(self.studentImg, (self.pos_x, self.pos_y))

    class Stone:
        def __init__(self, game):
            self.game = game
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
            self.game.gameDisplay.blit(self.stoneImg, (self.pos_x, self.pos_y))

    class Game:
        def __init__(self):
            '''
            pygame.init()        
            self.gameDisplay = pygame.display.set_mode((600, 600))
            pygame.display.set_caption('Dodge people on Palm Avenue!')
            '''
            self.clock = pygame.time.Clock()
            self.last_spawn_stone = pygame.time.get_ticks()    # 獲取時間(毫秒)
            self.stones = []
            self.student = Student(self)       
#----------------------------------------
        def game_intro(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                self.gameDisplay.fill((255, 255, 255))
                self.draw_text("Dodge people on Palm Avenue!",40, (0, 0, 0), 300, 200)    # draw_text
                self.draw_text("Operations guide : Use ↑ ↓ ← → on your keyboard",20, (0, 0, 0), 300, 250)
                self.draw_text("                   to dodge people in 30 seconds",20, (0, 0, 0), 300, 300)
                self.button("Start", 250, 250, 100, 50,(200, 0, 0), (255, 0, 0), action=self.new)    # button    # new
                pygame.display.update()
                self.clock.tick(30)
#-----------------------------------------
        def new(self):
            self.stones = []
            self.student = Student(self)
            while True:
                if pygame.time.get_ticks() > 30000:    # 30秒
                    self.draw_text("You AG!", 50, (255, 255, 255), 300, 300)
                    final = 0
                    pygame.display.update()
                    time.sleep(2)
                    self.draw()
                    pygame.display.update()
                    time.sleep(1)
                    self.draw_text("academic_performance = 60", 20, (255, 255, 255), 300, 300)
                    self.draw_text("romantic_relationship = 60", 20, (255, 255, 255), 300, 275)
                    self.draw_text("interpersonal_relationship = 40", 20, (255, 255, 255), 300, 250)
                    self.draw_text("health = 40", 20, (255, 255, 255), 300, 225)
                    self.draw_text("money = 30", 20, (255, 255, 255), 300, 200)
                    pygame.display.update()
                    ######印出減分
                    time.sleep(5)
                    pygame.quit()
                    quit()
                    time.sleep(1)
                    return romantic_relationship, money, health, academic_performance, interpersonal_relationship
                    pygame.quit()
                    quit()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                self.update()    # update
                self.draw()    # draw          
                self.clock.tick(60)
#----------------------------------------   
        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_spawn_stone >= 800:
                self.stones.append(Stone(self))
                self.last_spawn_stone = now
            
            self.student.update()    # 更新學生
        
            for stone in self.stones:
                stone.update()    # 更新石頭
                if stone.pos_y >= 600:    # 如果石頭超出範圍，除掉
                    self.stones.remove(stone)

            for stone in self.stones:    # 每顆石頭檢查碰撞
                if self.collision_check(self.student, stone):    # collision_check
                    final = 1
                    self.draw_text("Lose!", 50, (255, 255, 255), 300, 300)
                    pygame.display.update()
                    time.sleep(2)
                    self.draw()
                    pygame.display.update()
                    time.sleep(1)
                    self.draw_text("academic_performance = 60", 20, (255, 255, 255), 300, 300)
                    self.draw_text("romantic_relationship = 60", 20, (255, 255, 255), 300, 275)
                    self.draw_text("interpersonal_relationship = 40", 20, (255, 255, 255), 300, 250)
                    self.draw_text("health = 40", 20, (255, 255, 255), 300, 225)
                    self.draw_text("money = 30", 20, (255, 255, 255), 300, 200)
                    pygame.display.update()
                    time.sleep(5)
                    pygame.quit()
                    quit()

#----------------------------------------
        def collision_check(self, obj_one, obj_two):
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
#----------------------------------------
        def draw(self):
            self.gameDisplay.fill((255, 255, 255))
            self.gameDisplay.blit(space, (0,0,600,600))    # 背景尺寸要改
            self.student.draw()
            for stone in self.stones:
                stone.draw()
            pygame.display.update()

#-----------------------------------------
        def button(self, text, posX, posY, width, height, inActiveColor, activeColor, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (mouse[0] > posX and mouse[0] < posX+width) and (mouse[1] > posY and mouse[1] < posY+height):
                pygame.draw.rect(self.gameDisplay, activeColor, (posX, posY, width, height))
                if click[0] == 1 and action != None:
                    action()
            else:
                pygame.draw.rect(self.gameDisplay, inActiveColor, (posX, posY, width, height))
            self.draw_text(text, 25, (255, 255, 255), posX+(width/2), posY+(height/2))
#----------------------------------------   
        def draw_text(self, text, size, color, x, y):
            font = pygame.font.SysFont('arial', size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            self.gameDisplay.blit(text_surface, text_rect)