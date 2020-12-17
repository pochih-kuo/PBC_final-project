import sys
import pygame as pg
import tkinter as tk

# 設定視窗尺寸
win_width, win_height = 600, 800
clock = pg.time.Clock()

pg.init()
font1 = pg.font.Font(None, 50)
font2 = pg.font.Font(None, 28)
font3 = pg.font.Font(None, 20)
screen = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("My Life in NTU")

def initial():  # 遊戲初始畫面
    # 設定畫布
    bg = pg.Surface((win_width, win_height))
    bg.convert()

    # 插入背景圖片
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入遊戲標題與開始鍵
    textTitle = font1.render("My Life in NTU", True, (0,0,0), (255,255,255))
    imageStart = pg.image.load("start.png")
    pos_Title = [180, 250]
    pos_Start = [180, 400]
    bg.blit(textTitle, pos_Title)
    bg.blit(imageStart, pos_Start)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Start[0] < pg.mouse.get_pos()[0] < pos_Start[0]+150\
                  and pos_Start[1] < pg.mouse.get_pos()[1] < pos_Start[1]+100:
                    intro()  # 進入遊戲說明

def intro():  # 遊戲說明畫面
    # 設定畫布
    bg = pg.Surface((win_width, win_height))
    bg.convert()

    # 插入背景圖片
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    imageTeacher = pg.image.load("teacher.jpg")
    imageTeacher = pg.transform.scale(imageTeacher,(300,300))
    imageMessage = pg.image.load("message.png")
    imageMessage = pg.transform.scale(imageMessage,(450,350))
    imageNext = pg.image.load("next.png")
    imageNext = pg.transform.scale(imageNext, (120,35))
    
    pos_Teacher, pos_Message, pos_Next = [50,450],[100,70], [450,730]
    bg.blit(imageTeacher,pos_Teacher)
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageNext, pos_Next)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Next[0] < pg.mouse.get_pos()[0] < pos_Next[0]+150\
                  and pos_Next[1] < pg.mouse.get_pos()[1] < pos_Next[1]+100:
                    rolechoose()  # 進入遊戲說明    

def rolechoose():  # 角色選擇畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()

    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    imageName = pg.image.load("name.png")
    imageName = pg.transform.scale(imageName, (120,35))
    textGender = font2.render("Gender:", True, (0,0,0), (255,255,255))
    imageNMale = pg.image.load("male_grey.png")
    imageNMale = pg.transform.scale(imageNMale, (120,35))
    imageNFemale = pg.image.load("female_grey.png")
    imageNFemale = pg.transform.scale(imageNFemale, (120,35))
    imagePlay = pg.image.load("play.png")
    imagePlay = pg.transform.scale(imagePlay, (120,35))
    imageMale = pg.image.load("male.png")
    imageMale = pg.transform.scale(imageMale, (120,35))
    imageFemale = pg.image.load("female.png")
    imageFemale = pg.transform.scale(imageFemale, (120,35))

    imageName.convert()
    imageNMale.convert()
    imageNFemale.convert()
    imagePlay.convert()
    imageMale.convert()
    imageFemale.convert()

    pos_Name, pos_Gender, pos_NMale, pos_NFemale, pos_Play = [80, 270],[100, 370],[220,370], [380,370], [250, 460]

    bg.blit(imageName, pos_Name)
    bg.blit(textGender, pos_Gender)
    bg.blit(imageNMale, pos_NMale)
    bg.blit(imageNFemale, pos_NFemale)
    bg.blit(imagePlay, pos_Play)
    
    screen.blit(bg,(0,0))
    pg.display.update()
    gender = ""

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_NMale[0] < pg.mouse.get_pos()[0] < pos_NMale[0]+100\
                  and pos_NMale[1] < pg.mouse.get_pos()[1] < pos_NMale[1]+50:
                    gender = "Male"
                    pos_Male = [220,370]
                    bg.blit(imageMale, pos_Male)
                    bg.blit(imageNFemale, pos_NFemale)
                elif pos_NFemale[0] < pg.mouse.get_pos()[0] < pos_NFemale[0]+100\
                  and pos_NFemale[1] < pg.mouse.get_pos()[1] < pos_NFemale[1]+50:
                    gender = "Female"
                    pos_Female = [380,370]
                    bg.blit(imageFemale, pos_Female)
                    bg.blit(imageNMale, pos_NMale)
                
                screen.blit(bg, (0,0))
                pg.display.update()
            
                if pos_Play[0] < pg.mouse.get_pos()[0] < pos_Play[0]+100\
                  and pos_Play[1] < pg.mouse.get_pos()[1] < pos_Play[1]+50:
                    if gender != "":
                        point = {"Love": 60, "Money":60, "Health":60, "Study":60, "Friend":60}
                        grade = 1
                        stage1(gender, point, grade)

def lake(gender, point, grade):
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_orange.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))    
                    
    imageHelp = pg.image.load("help.png")
    imageMessage = pg.image.load("message.png")
    imageMessage = pg.transform.scale(imageMessage,(450,350))
    imageNext = pg.image.load("next.png")
    imageNext = pg.transform.scale(imageNext, (120,35))
    
    pos_Help, pos_Message, pos_Next = [50,450],[100,70], [450,730]
    bg.blit(imageHelp,pos_Help)
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageNext, pos_Next)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:  # 回到主畫面
                if pos_Next[0] < pg.mouse.get_pos()[0] < pos_Next[0]+150\
                  and pos_Next[1] < pg.mouse.get_pos()[1] < pos_Next[1]+100:
                    if grade == 1:
                        stage1(gender, point, grade)
                    elif grade == 2:
                        stage2(gender, point, grade)
                    elif grade == 3:
                        stage3(gender, point, grade)
                    elif grade == 4:
                        stage4(gender, point, grade)

def stage1(gender, point, grade):  # 主畫面1
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 能力值
    imageLove = pg.image.load("love.png")
    imageLove = pg.transform.scale(imageLove, (40,40))
    imageMoney = pg.image.load("money.png")
    imageMoney = pg.transform.scale(imageMoney, (40,40))
    imageHealth = pg.image.load("Health.png")
    imageHealth = pg.transform.scale(imageHealth, (40,40))
    imageStudy = pg.image.load("study.png")
    imageStudy = pg.transform.scale(imageStudy, (40,40))
    imageFriend = pg.image.load("friend.png")
    imageFriend = pg.transform.scale(imageFriend, (40,40))
    imageLove.convert()
    imageMoney.convert()
    imageHealth.convert()
    imageStudy.convert()
    imageFriend.convert()

    score_Love = font2.render(str(point["Love"]), True, (0,0,0), (255,255,255))
    score_Money = font2.render(str(point["Money"]), True, (0,0,0), (255,255,255))
    score_Health = font2.render(str(point["Health"]), True, (0,0,0), (255,255,255))
    score_Study = font2.render(str(point["Study"]), True, (0,0,0), (255,255,255))
    score_Friend = font2.render(str(point["Friend"]), True, (0,0,0), (255,255,255))    

    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [20, 540],[20,590],[20,640],[20,690],[20,740]
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [80,540], [80,590], [80,640],[80,690],[80,740]
    bg.blit(imageLove, pos_Love)
    bg.blit(imageMoney, pos_Money)
    bg.blit(imageHealth, pos_Health)
    bg.blit(imageStudy, pos_Study)
    bg.blit(imageFriend, pos_Friend)
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    imageCoco = pg.image.load("coco.png")
    imageCoco = pg.transform.scale(imageCoco, (150,150))
    imageLib = pg.image.load("library.png")
    imageLib = pg.transform.scale(imageLib, (150,150))
    imageDorm = pg.image.load("dorm.png")
    imageDorm = pg.transform.scale(imageDorm, (150,150))
    imageLab = pg.image.load("laboratory.png")
    imageLab = pg.transform.scale(imageLab, (150,150))
    imageLake = pg.image.load("lake.png")
    imageLake = pg.transform.scale(imageLake, (150,150))
    imageAlert = pg.image.load("alert.png")

    pos_Coco, pos_Lib, pos_Dorm, pos_Lab, pos_Lake = [200,400],[200,50],[400,500],[400,200],[30,250]
    pos_Alert1 = [270,500]
    bg.blit(imageCoco, pos_Coco)
    bg.blit(imageLib, pos_Lib)
    bg.blit(imageDorm, pos_Dorm)
    bg.blit(imageLab, pos_Lab)
    bg.blit(imageLake, pos_Lake)
    bg.blit(imageAlert, pos_Alert1)

    screen.blit(bg,(0,0))
    pg.display.update()
    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Coco[0] < pg.mouse.get_pos()[0] < pos_Coco[0]+150\
                  and pos_Coco[1] < pg.mouse.get_pos()[1] < pos_Coco[1]+150:
                    grade += 1
                    stage2(gender, point, grade)
                
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+150\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+150:
                    lake(gender, point, grade)

def stage2(gender, point, grade):  # 主畫面2
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 能力值
    imageLove = pg.image.load("love.png")
    imageLove = pg.transform.scale(imageLove, (40,40))
    imageMoney = pg.image.load("money.png")
    imageMoney = pg.transform.scale(imageMoney, (40,40))
    imageHealth = pg.image.load("Health.png")
    imageHealth = pg.transform.scale(imageHealth, (40,40))
    imageStudy = pg.image.load("study.png")
    imageStudy = pg.transform.scale(imageStudy, (40,40))
    imageFriend = pg.image.load("friend.png")
    imageFriend = pg.transform.scale(imageFriend, (40,40))
    imageLove.convert()
    imageMoney.convert()
    imageHealth.convert()
    imageStudy.convert()
    imageFriend.convert()

    score_Love = font2.render(str(point["Love"]), True, (0,0,0), (255,255,255))
    score_Money = font2.render(str(point["Money"]), True, (0,0,0), (255,255,255))
    score_Health = font2.render(str(point["Health"]), True, (0,0,0), (255,255,255))
    score_Study = font2.render(str(point["Study"]), True, (0,0,0), (255,255,255))
    score_Friend = font2.render(str(point["Friend"]), True, (0,0,0), (255,255,255))    

    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [20, 540],[20,590],[20,640],[20,690],[20,740]
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [80,540], [80,590], [80,640],[80,690],[80,740]
    bg.blit(imageLove, pos_Love)
    bg.blit(imageMoney, pos_Money)
    bg.blit(imageHealth, pos_Health)
    bg.blit(imageStudy, pos_Study)
    bg.blit(imageFriend, pos_Friend)
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    imageCoco = pg.image.load("coco.png")
    imageCoco = pg.transform.scale(imageCoco, (150,150))
    imageLib = pg.image.load("library.png")
    imageLib = pg.transform.scale(imageLib, (150,150))
    imageDorm = pg.image.load("dorm.png")
    imageDorm = pg.transform.scale(imageDorm, (150,150))
    imageLab = pg.image.load("laboratory.png")
    imageLab = pg.transform.scale(imageLab, (150,150))
    imageLake = pg.image.load("lake.png")
    imageLake = pg.transform.scale(imageLake, (150,150))
    imageAlert = pg.image.load("alert.png")
    imageCheck = pg.image.load("check.png")

    pos_Coco, pos_Lib, pos_Dorm, pos_Lab, pos_Lake = [200,400],[200,50],[400,500],[400,200],[30,250]
    pos_Alert2, pos_Check1 = [270, 150], [270,500]
    bg.blit(imageCoco, pos_Coco)
    bg.blit(imageLib, pos_Lib)
    bg.blit(imageDorm, pos_Dorm)
    bg.blit(imageLab, pos_Lab)
    bg.blit(imageLake, pos_Lake)
    bg.blit(imageAlert, pos_Alert2)
    bg.blit(imageCheck, pos_Check1)

    screen.blit(bg,(0,0))
    pg.display.update()
    
    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Lib[0] < pg.mouse.get_pos()[0] < pos_Lib[0]+150\
                  and pos_Lib[1] < pg.mouse.get_pos()[1] < pos_Lib[1]+150:
                    grade += 1
                    stage3(gender, point, grade)
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+150\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+150:
                    lake(gender, point, grade)

def stage3(gender, point, grade):  # 主畫面3
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 能力值
    imageLove = pg.image.load("love.png")
    imageLove = pg.transform.scale(imageLove, (40,40))
    imageMoney = pg.image.load("money.png")
    imageMoney = pg.transform.scale(imageMoney, (40,40))
    imageHealth = pg.image.load("Health.png")
    imageHealth = pg.transform.scale(imageHealth, (40,40))
    imageStudy = pg.image.load("study.png")
    imageStudy = pg.transform.scale(imageStudy, (40,40))
    imageFriend = pg.image.load("friend.png")
    imageFriend = pg.transform.scale(imageFriend, (40,40))
    imageLove.convert()
    imageMoney.convert()
    imageHealth.convert()
    imageStudy.convert()
    imageFriend.convert()

    score_Love = font2.render(str(point["Love"]), True, (0,0,0), (255,255,255))
    score_Money = font2.render(str(point["Money"]), True, (0,0,0), (255,255,255))
    score_Health = font2.render(str(point["Health"]), True, (0,0,0), (255,255,255))
    score_Study = font2.render(str(point["Study"]), True, (0,0,0), (255,255,255))
    score_Friend = font2.render(str(point["Friend"]), True, (0,0,0), (255,255,255))    

    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [20, 540],[20,590],[20,640],[20,690],[20,740]
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [80,540], [80,590], [80,640],[80,690],[80,740]
    bg.blit(imageLove, pos_Love)
    bg.blit(imageMoney, pos_Money)
    bg.blit(imageHealth, pos_Health)
    bg.blit(imageStudy, pos_Study)
    bg.blit(imageFriend, pos_Friend)
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    imageCoco = pg.image.load("coco.png")
    imageCoco = pg.transform.scale(imageCoco, (150,150))
    imageLib = pg.image.load("library.png")
    imageLib = pg.transform.scale(imageLib, (150,150))
    imageDorm = pg.image.load("dorm.png")
    imageDorm = pg.transform.scale(imageDorm, (150,150))
    imageLab = pg.image.load("laboratory.png")
    imageLab = pg.transform.scale(imageLab, (150,150))
    imageLake = pg.image.load("lake.png")
    imageLake = pg.transform.scale(imageLake, (150,150))
    imageAlert = pg.image.load("alert.png")
    imageCheck = pg.image.load("check.png")

    pos_Coco, pos_Lib, pos_Dorm, pos_Lab, pos_Lake = [200,400],[200,50],[400,500],[400,200],[30,250]
    pos_Alert3, pos_Check1, pos_Check2 = [470,600], [270, 150], [270,500]
    bg.blit(imageCoco, pos_Coco)
    bg.blit(imageLib, pos_Lib)
    bg.blit(imageDorm, pos_Dorm)
    bg.blit(imageLab, pos_Lab)
    bg.blit(imageLake, pos_Lake)
    bg.blit(imageAlert, pos_Alert3)
    bg.blit(imageCheck, pos_Check1)
    bg.blit(imageCheck, pos_Check2)

    screen.blit(bg,(0,0))
    pg.display.update()
    
    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Dorm[0] < pg.mouse.get_pos()[0] < pos_Dorm[0]+150\
                  and pos_Dorm[1] < pg.mouse.get_pos()[1] < pos_Dorm[1]+150:
                    grade += 1
                    stage4(gender, point, grade)
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+150\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+150:
                    lake(gender, point, grade)

def stage4(gender, point, grade):  # 主畫面3
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 能力值
    imageLove = pg.image.load("love.png")
    imageLove = pg.transform.scale(imageLove, (40,40))
    imageMoney = pg.image.load("money.png")
    imageMoney = pg.transform.scale(imageMoney, (40,40))
    imageHealth = pg.image.load("Health.png")
    imageHealth = pg.transform.scale(imageHealth, (40,40))
    imageStudy = pg.image.load("study.png")
    imageStudy = pg.transform.scale(imageStudy, (40,40))
    imageFriend = pg.image.load("friend.png")
    imageFriend = pg.transform.scale(imageFriend, (40,40))
    imageLove.convert()
    imageMoney.convert()
    imageHealth.convert()
    imageStudy.convert()
    imageFriend.convert()

    score_Love = font2.render(str(point["Love"]), True, (0,0,0), (255,255,255))
    score_Money = font2.render(str(point["Money"]), True, (0,0,0), (255,255,255))
    score_Health = font2.render(str(point["Health"]), True, (0,0,0), (255,255,255))
    score_Study = font2.render(str(point["Study"]), True, (0,0,0), (255,255,255))
    score_Friend = font2.render(str(point["Friend"]), True, (0,0,0), (255,255,255))    

    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [20, 540],[20,590],[20,640],[20,690],[20,740]
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [80,540], [80,590], [80,640],[80,690],[80,740]
    bg.blit(imageLove, pos_Love)
    bg.blit(imageMoney, pos_Money)
    bg.blit(imageHealth, pos_Health)
    bg.blit(imageStudy, pos_Study)
    bg.blit(imageFriend, pos_Friend)
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    imageCoco = pg.image.load("coco.png")
    imageCoco = pg.transform.scale(imageCoco, (150,150))
    imageLib = pg.image.load("library.png")
    imageLib = pg.transform.scale(imageLib, (150,150))
    imageDorm = pg.image.load("dorm.png")
    imageDorm = pg.transform.scale(imageDorm, (150,150))
    imageLab = pg.image.load("laboratory.png")
    imageLab = pg.transform.scale(imageLab, (150,150))
    imageLake = pg.image.load("lake.png")
    imageLake = pg.transform.scale(imageLake, (150,150))
    imageAlert = pg.image.load("alert.png")
    imageCheck = pg.image.load("check.png")

    pos_Coco, pos_Lib, pos_Dorm, pos_Lab, pos_Lake = [200,400],[200,50],[400,500],[400,200],[30,250]
    pos_Alert4, pos_Check1, pos_Check2, pos_Check3= [470,300], [470,600], [270, 150], [270,500]
    bg.blit(imageCoco, pos_Coco)
    bg.blit(imageLib, pos_Lib)
    bg.blit(imageDorm, pos_Dorm)
    bg.blit(imageLab, pos_Lab)
    bg.blit(imageLake, pos_Lake)
    bg.blit(imageAlert, pos_Alert4)
    bg.blit(imageCheck, pos_Check1)
    bg.blit(imageCheck, pos_Check2)
    bg.blit(imageCheck, pos_Check3)

    screen.blit(bg,(0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Lab[0] < pg.mouse.get_pos()[0] < pos_Lab[0]+150\
                  and pos_Lab[1] < pg.mouse.get_pos()[1] < pos_Lab[1]+150:
                    final(gender, point)
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+150\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+150:
                    lake(gender, point, grade)

def final(gender, point):
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_final.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))    
                    
    imageMessage = pg.image.load("message.png")
    imageMessage = pg.transform.scale(imageMessage,(250,200))
    
    pos_Message = [300,150]
    bg.blit(imageMessage, pos_Message)

    
    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

if __name__ == '__main__':    
    initial()
