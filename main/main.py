import sys
import pygame as pg
import tkinter as tk
import webbrowser
# 設定視窗尺寸
win_width, win_height = 600, 800
clock = pg.time.Clock()

pg.init()
# 設定字型
font1 = pg.font.Font(None, 50)
font2 = pg.font.Font(None, 28)
font3 = pg.font.Font(None, 20)
font4 = pg.font.Font(None, 40)
screen = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("My Life in NTU")  # 設定視窗標題

def initial():  # 遊戲初始畫面
    # 設定畫布並插入背景圖片
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入遊戲標題與開始鍵
    textTitle = font1.render("My Life in NTU", True, (0,0,0))
    imageStart = pg.image.load("start.png")
    imageStart.convert()
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
            if event.type == pg.MOUSEBUTTONDOWN:  # 點選並進入遊戲說明
                if pos_Start[0] < pg.mouse.get_pos()[0] < pos_Start[0]+150\
                  and pos_Start[1] < pg.mouse.get_pos()[1] < pos_Start[1]+100:
                    intro()  # 進入遊戲說明

def intro():  # 遊戲說明畫面
    # 設定畫布並插入背景圖片
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入老師、對話框、繼續圖片
    imageTeacher = pg.image.load("teacher.jpg")
    imageTeacher = pg.transform.scale(imageTeacher,(300,300))
    imageMessage = pg.image.load("message.png")
    imageMessage = pg.transform.scale(imageMessage,(500,350))
    imageNext = pg.image.load("next.png")
    imageNext = pg.transform.scale(imageNext, (120,35))
    imageTeacher.convert()
    imageMessage.convert()
    imageNext.convert()
    pos_Teacher, pos_Message, pos_Next = [50,450],[70,70], [450,730]
    bg.blit(imageTeacher,pos_Teacher)
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageNext, pos_Next)

    # 插入文字
    textWelcome = font2.render("Welcome!", True, (0,71,125))
    textFreshman = font2.render("You are a freshman of NTU.", True, (0,71,125))
    textTime2journey = font2.render("It's time to have a memorable journey in NTU", True, (0,71,125))
    textHope = font2.render("Hope you enjoy 4-year life in university.", True, (0,71,125))
    pos_Welcome, pos_Freshman, pos_Time2journey, pos_Hope = [120, 140], [120, 180], [120, 220], [120,260]
    bg.blit(textWelcome, pos_Welcome)
    bg.blit(textFreshman, pos_Freshman)
    bg.blit(textTime2journey, pos_Time2journey)
    bg.blit(textHope, pos_Hope)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:  # 點選並進入角色選擇畫面
                if pos_Next[0] < pg.mouse.get_pos()[0] < pos_Next[0]+150\
                  and pos_Next[1] < pg.mouse.get_pos()[1] < pos_Next[1]+100:
                    rolechoose()  # 進入角色選擇畫面    

def rolechoose():  # 角色選擇畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入 姓名、性別、Play圖片
    imageName = pg.image.load("name.png")
    imageName = pg.transform.scale(imageName, (120,35))
    textGender = font2.render("Gender:", True, (0,0,0))
    imageNMale = pg.image.load("male_grey.png")  # 灰底(未選擇)
    imageNMale = pg.transform.scale(imageNMale, (120,35))
    imageNFemale = pg.image.load("female_grey.png")  # 灰底(未選擇)
    imageNFemale = pg.transform.scale(imageNFemale, (120,35))
    imagePlay = pg.image.load("play.png")
    imagePlay = pg.transform.scale(imagePlay, (120,35))
    imageMale = pg.image.load("male.png")  # 藍底(選擇)
    imageMale = pg.transform.scale(imageMale, (120,35))
    imageFemale = pg.image.load("female.png")  # 藍底(選擇)
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
    
    # 顯示畫布
    screen.blit(bg,(0,0))
    pg.display.update()
    gender = ""  # 記錄角色性別

    while True:
        for event in pg.event.get():   
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_NMale[0] < pg.mouse.get_pos()[0] < pos_NMale[0]+100\
                  and pos_NMale[1] < pg.mouse.get_pos()[1] < pos_NMale[1]+50:
                # 選擇男性
                    gender = "Male"
                    pos_Male = [220,370]
                    bg.blit(imageMale, pos_Male)
                    bg.blit(imageNFemale, pos_NFemale)  # 灰底Female覆蓋
                elif pos_NFemale[0] < pg.mouse.get_pos()[0] < pos_NFemale[0]+100\
                  and pos_NFemale[1] < pg.mouse.get_pos()[1] < pos_NFemale[1]+50:
                # 選擇女性
                    gender = "Female"
                    pos_Female = [380,370]
                    bg.blit(imageFemale, pos_Female)
                    bg.blit(imageNMale, pos_NMale)   # 灰底Male覆蓋
                
                screen.blit(bg, (0,0))
                pg.display.update()
            
                if pos_Play[0] < pg.mouse.get_pos()[0] < pos_Play[0]+100\
                  and pos_Play[1] < pg.mouse.get_pos()[1] < pos_Play[1]+50:
                    if gender != "":  # 進入大一畫面
                    # 記錄初始化分數、年級
                        point = {"Love": 60, "Money":60, "Health":60, "Study":60, "Friend":60}
                        grade = 1
                        stage1(gender, point, grade)

def lake(gender, point, grade):  # 醉月湖畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_orange.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))    
    
    # 插入圖片、對話框、繼續圖片
    imagePark = pg.image.load("park.png")
    imageMessage = pg.image.load("message.png")
    imageMessage = pg.transform.scale(imageMessage,(450,350))
    imageResume = pg.image.load("resume.png")
    imageResume = pg.transform.scale(imageResume, (120,35))
    textJump = font4.render("Jump", True, (0,0,0))
    imagePark.convert()
    imageMessage.convert()
    imageResume.convert()
    pos_Park, pos_Message, pos_Resume, pos_Jump = [50,450],[100,70], [450,680], [450, 630]
    bg.blit(imagePark,pos_Park)
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageResume, pos_Resume)
    bg.blit(textJump, pos_Jump)

    # 插入文字
    textWow = font4.render("Wow!", True, (0,0,0))
    textGoodplace = font4.render("Such a wonderful place.", True, (0,0,0))
    textWhat2do = font2.render("What will you do?", True, (0,0,0))
    pos_Wow, pos_Goodplace, pos_What2do = [150, 150], [150, 200], [300, 270]
    bg.blit(textWow, pos_Wow)
    bg.blit(textGoodplace, pos_Goodplace)
    bg.blit(textWhat2do, pos_What2do)
    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Resume[0] < pg.mouse.get_pos()[0] < pos_Resume[0]+150\
                  and pos_Resume[1] < pg.mouse.get_pos()[1] < pos_Resume[1]+100:
                    # 回到各年級畫面
                    if grade == 1:
                        stage1(gender, point, grade)
                    elif grade == 2:
                        stage2(gender, point, grade)
                    elif grade == 3:
                        stage3(gender, point, grade)
                    elif grade == 4:
                        stage4(gender, point, grade)
                
                if pos_Jump[0] < pg.mouse.get_pos()[0] < pos_Jump[0]+100\
                  and pos_Jump[1] < pg.mouse.get_pos()[1] < pos_Jump[1]+100:
                    # 扣分、開啟網頁
                    point["Health"] -= 10
                    if point["Health"] <= 0:
                        point["Health"] = 0
                    webbrowser.open("https://scc_osa.ntu.edu.tw")
                    
                    # 回到各年級畫面
                    if grade == 1:
                        stage1(gender, point, grade)
                    elif grade == 2:
                        stage2(gender, point, grade)
                    elif grade == 3:
                        stage3(gender, point, grade)
                    elif grade == 4:
                        stage4(gender, point, grade)

def stage1(gender, point, grade):  # 大一畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入能力值
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
    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [40, 540],[40,590],[40,640],[40,690],[40,740]
    bg.blit(imageLove, pos_Love)
    bg.blit(imageMoney, pos_Money)
    bg.blit(imageHealth, pos_Health)
    bg.blit(imageStudy, pos_Study)
    bg.blit(imageFriend, pos_Friend)
    
    # 插入能力值分數
    score_Love = font4.render(str(point["Love"]), True, (0,0,0))
    score_Money = font4.render(str(point["Money"]), True, (0,0,0))
    score_Health = font4.render(str(point["Health"]), True, (0,0,0))
    score_Study = font4.render(str(point["Study"]), True, (0,0,0))
    score_Friend = font4.render(str(point["Friend"]), True, (0,0,0))    
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [100,550], [100,600], [100,650],[100,700],[100,750]
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    # 插入關卡、未完成任務及已完成任務
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

    # 顯示畫布
    screen.blit(bg,(0,0))
    pg.display.update()

    # 計算是否失敗
    point_list = list(point.items())
    point_list.sort(key=lambda x:x[1], reverse=True)
    sum_zero_point = 0
    for pairs in point_list:
        pairs_list = list(pairs)
        if pairs_list[1] == 0:
            sum_zero_point += 1
    if sum_zero_point >= 3:
        gameover()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Coco[0] < pg.mouse.get_pos()[0] < pos_Coco[0]+150\
                  and pos_Coco[1] < pg.mouse.get_pos()[1] < pos_Coco[1]+150:
                # 進入大一遊戲畫面
                    grade += 1
                    stage2(gender, point, grade)
                
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+150\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+150:
                # 進入醉月湖畫面
                    lake(gender, point, grade)

def stage2(gender, point, grade):  # 大二畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入能力值圖片
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
    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [40, 540],[40,590],[40,640],[40,690],[40,740]
    bg.blit(imageLove, pos_Love)
    bg.blit(imageMoney, pos_Money)
    bg.blit(imageHealth, pos_Health)
    bg.blit(imageStudy, pos_Study)
    bg.blit(imageFriend, pos_Friend)

    # 插入能力值分數
    score_Love = font4.render(str(point["Love"]), True, (0,0,0))
    score_Money = font4.render(str(point["Money"]), True, (0,0,0))
    score_Health = font4.render(str(point["Health"]), True, (0,0,0))
    score_Study = font4.render(str(point["Study"]), True, (0,0,0))
    score_Friend = font4.render(str(point["Friend"]), True, (0,0,0))    
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [100,550], [100,600], [100,650],[100,700],[100,750]
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

    # 顯示畫布
    screen.blit(bg,(0,0))
    pg.display.update()
    
    # 計算是否失敗
    point_list = list(point.items())
    point_list.sort(key=lambda x:x[1], reverse=True)
    sum_zero_point = 0
    for pairs in point_list:
        pairs_list = list(pairs)
        if pairs_list[1] == 0:
            sum_zero_point += 1
    if sum_zero_point >= 3:
        gameover()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Lib[0] < pg.mouse.get_pos()[0] < pos_Lib[0]+150\
                  and pos_Lib[1] < pg.mouse.get_pos()[1] < pos_Lib[1]+150:
                # 進入大二遊戲畫面
                    grade += 1
                    stage3(gender, point, grade)
                elif pos_Coco[0] < pg.mouse.get_pos()[0] < pos_Coco[0]+150\
                  and pos_Coco[1] < pg.mouse.get_pos()[1] < pos_Coco[1]+150:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+150\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+150:
                # 進入醉月湖畫面
                    lake(gender, point, grade)

def stage3(gender, point, grade):  # 大三畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入能力值圖片
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
    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [40, 540],[40,590],[40,640],[40,690],[40,740]
    bg.blit(imageLove, pos_Love)
    bg.blit(imageMoney, pos_Money)
    bg.blit(imageHealth, pos_Health)
    bg.blit(imageStudy, pos_Study)
    bg.blit(imageFriend, pos_Friend)

    # 插入能力值分數
    score_Love = font4.render(str(point["Love"]), True, (0,0,0))
    score_Money = font4.render(str(point["Money"]), True, (0,0,0))
    score_Health = font4.render(str(point["Health"]), True, (0,0,0))
    score_Study = font4.render(str(point["Study"]), True, (0,0,0))
    score_Friend = font4.render(str(point["Friend"]), True, (0,0,0))    
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [100,550], [100,600], [100,650],[100,700],[100,750]
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    # 插入關卡、未完成任務及已完成任務
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

    # 顯示畫布
    screen.blit(bg,(0,0))
    pg.display.update()
    
    # 計算是否失敗
    point_list = list(point.items())
    point_list.sort(key=lambda x:x[1], reverse=True)
    sum_zero_point = 0
    for pairs in point_list:
        pairs_list = list(pairs)
        if pairs_list[1] == 0:
            sum_zero_point += 1
    if sum_zero_point >= 3:
        gameover()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Dorm[0] < pg.mouse.get_pos()[0] < pos_Dorm[0]+150\
                  and pos_Dorm[1] < pg.mouse.get_pos()[1] < pos_Dorm[1]+150:
                # 進入大三遊戲畫面
                    grade += 1
                    stage4(gender, point, grade)
                elif pos_Coco[0] < pg.mouse.get_pos()[0] < pos_Coco[0]+150\
                  and pos_Coco[1] < pg.mouse.get_pos()[1] < pos_Coco[1]+150:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lib[0] < pg.mouse.get_pos()[0] < pos_Lib[0]+150\
                  and pos_Lib[1] < pg.mouse.get_pos()[1] < pos_Lib[1]+150:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+150\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+150:
                # 進入醉月湖畫面
                    lake(gender, point, grade)

def stage4(gender, point, grade):  # 大四畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入能力值圖片
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
    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [40, 540],[40,590],[40,640],[40,690],[40,740]
    imageLove.convert()
    imageMoney.convert()
    imageHealth.convert()
    imageStudy.convert()
    imageFriend.convert()
    bg.blit(imageLove, pos_Love)
    bg.blit(imageMoney, pos_Money)
    bg.blit(imageHealth, pos_Health)
    bg.blit(imageStudy, pos_Study)
    bg.blit(imageFriend, pos_Friend)

    # 插入能力值分數
    score_Love = font4.render(str(point["Love"]), True, (0,0,0))
    score_Money = font4.render(str(point["Money"]), True, (0,0,0))
    score_Health = font4.render(str(point["Health"]), True, (0,0,0))
    score_Study = font4.render(str(point["Study"]), True, (0,0,0))
    score_Friend = font4.render(str(point["Friend"]), True, (0,0,0))    
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [100,550], [100,600], [100,650],[100,700],[100,750]
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    # 插入關卡、未完成任務及已完成任務
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

    # 顯示畫布
    screen.blit(bg,(0,0))
    pg.display.update()

    # 計算是否失敗
    point_list = list(point.items())
    point_list.sort(key=lambda x:x[1], reverse=True)
    sum_zero_point = 0
    for pairs in point_list:
        pairs_list = list(pairs)
        if pairs_list[1] == 0:
            sum_zero_point += 1
    if sum_zero_point >= 3:
        gameover()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Lab[0] < pg.mouse.get_pos()[0] < pos_Lab[0]+150\
                  and pos_Lab[1] < pg.mouse.get_pos()[1] < pos_Lab[1]+150:
                # 進入大四遊戲畫面
                    final(gender, point)
                elif pos_Coco[0] < pg.mouse.get_pos()[0] < pos_Coco[0]+150\
                  and pos_Coco[1] < pg.mouse.get_pos()[1] < pos_Coco[1]+150:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lib[0] < pg.mouse.get_pos()[0] < pos_Lib[0]+150\
                  and pos_Lib[1] < pg.mouse.get_pos()[1] < pos_Lib[1]+150:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Dorm[0] < pg.mouse.get_pos()[0] < pos_Dorm[0]+150\
                  and pos_Dorm[1] < pg.mouse.get_pos()[1] < pos_Dorm[1]+150:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+150\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+150:
                # 進入醉月湖畫面
                    lake(gender, point, grade)

def skip(gender, point, grade):  # 非該年級遊戲畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_orange.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    imageResume = pg.image.load("resume.png")
    imageResume = pg.transform.scale(imageResume, (120,35))
    imageResume.convert()
    pos_Resume = [450,680]
    bg.blit(imageResume, pos_Resume)

    # 插入繼續文字
    textComplete = font1.render("You have completed the task.", True, (165,42,42))
    textMoveon = font1.render("Please Move on to another task!", True, (165,42,42))
    pos_Complete, pos_Moveon = [70, 250], [50, 350]
    bg.blit(textComplete, pos_Complete)
    bg.blit(textMoveon, pos_Moveon)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Resume[0] < pg.mouse.get_pos()[0] < pos_Resume[0]+150\
                  and pos_Resume[1] < pg.mouse.get_pos()[1] < pos_Resume[1]+100:
                    # 回到各年級畫面
                    if grade == 1:
                        stage1(gender, point, grade)
                    elif grade == 2:
                        stage2(gender, point, grade)
                    elif grade == 3:
                        stage3(gender, point, grade)
                    elif grade == 4:
                        stage4(gender, point, grade)

def final(gender, point):  # 遊戲結束畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_final.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))
    
    # 插入對話框                
    imageMessage = pg.image.load("message.png")
    imageMessage = pg.transform.scale(imageMessage,(300,200))
    pos_Message = [270,150]
    bg.blit(imageMessage, pos_Message)

    # 成績結算
    point_list = list(point.items())
    point_list.sort(key=lambda x:x[1], reverse=True)
    result = list(point_list[0])
    prize = ""
    if result[0] == "Health":
        prize = "Sunshine Boy" if gender == "Male" else "Sunshine Girl"
    elif result[0] == "Love":
        prize = "Heartthrob"
    elif result[0] == "Friend":
        prize = "King of Friends"
    elif result[0] == "Money":
        prize = "Rich man"
    elif result[0] == "Study":
        prize = "knowledgeable Boy" if gender == "Male" else "knowledgeable Girl"
    
    # 顯示遊戲結果
    textCongratulation = font2.render("Congratulations!", True, (0,0,0))
    textYouare = font2.render("You have been a", True, (0,0,0))
    textPrize = font4.render(prize, True, (165,42,42))
    pos_Contratulation = [300,180]
    pos_Youare = [300,210]
    pos_Prize = [300, 240]
    bg.blit(textCongratulation, pos_Contratulation)
    bg.blit(textYouare, pos_Youare)
    bg.blit(textPrize, pos_Prize)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

def gameover():  # 遊戲失敗畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_final.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入失敗文字
    textGameover = font1.render("Game over!", True, (165,42,42))
    textDropout = font1.render("You are dropped out of school.", True, (165,42,42))
    pos_Gameover, pos_Dropout = [220, 250], [50, 350]
    bg.blit(textGameover, pos_Gameover)
    bg.blit(textDropout, pos_Dropout)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

if __name__ == '__main__':    
    initial()
