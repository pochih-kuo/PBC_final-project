import sys
import pygame as pg
import tkinter as tk
import webbrowser
# 設定視窗尺寸
win_width, win_height = 600, 600
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
    pos_Title = [180, 150]
    pos_Start = [180, 300]
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
    imageMessage = pg.image.load("start_msg.png")
    imageMessage = pg.transform.smoothscale(imageMessage,(500, 500))
    imageTeacher = pg.image.load("teacher.png")
    imageTeacher = pg.transform.scale(imageTeacher,(230, 230))
    imageNext = pg.image.load("next.png")
    imageNext = pg.transform.scale(imageNext, (120,35))
    imageTeacher.convert()
    imageMessage.convert()
    imageNext.convert()
    pos_Teacher, pos_Message, pos_Next = [50,370],[50,0], [300,470]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageTeacher,pos_Teacher)
    bg.blit(imageNext, pos_Next)

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
    pos_Name, pos_Gender, pos_NMale, pos_NFemale, pos_Play = [80, 150],[100, 250],[220, 250], [380, 250], [250, 340]
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
                    pos_Male = [220, 250]
                    bg.blit(imageMale, pos_Male)
                    bg.blit(imageNFemale, pos_NFemale)  # 灰底Female覆蓋
                elif pos_NFemale[0] < pg.mouse.get_pos()[0] < pos_NFemale[0]+100\
                  and pos_NFemale[1] < pg.mouse.get_pos()[1] < pos_NFemale[1]+50:
                # 選擇女性
                    gender = "Female"
                    pos_Female = [380, 250]
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
    imageBG = pg.image.load("bg_lake.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))    
    
    # 插入圖片、對話框、繼續圖片
    imageMessage = pg.image.load("lake_bubble.png")
    imageMessage = pg.transform.smoothscale(imageMessage,(550,270))
    imageJump = pg.image.load("jump.png")
    imageJump = pg.transform.smoothscale(imageJump,(200,80))
    imageNojump = pg.image.load("nojump.png")
    imageNojump = pg.transform.smoothscale(imageNojump,(200,80))
    imageMessage.convert()
    imageJump.convert()
    imageNojump.convert()
    pos_Message, pos_Jump, pos_Nojump = [20,250], [80,310], [310,310]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageJump, pos_Jump)
    bg.blit(imageNojump, pos_Nojump)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Nojump[0] < pg.mouse.get_pos()[0] < pos_Nojump[0]+200\
                  and pos_Nojump[1] < pg.mouse.get_pos()[1] < pos_Nojump[1]+80:
                    # 回到各年級畫面
                    if grade == 1:
                        stage1(gender, point, grade)
                    elif grade == 2:
                        stage2(gender, point, grade)
                    elif grade == 3:
                        stage3(gender, point, grade)
                    elif grade == 4:
                        stage4(gender, point, grade)
                
                if pos_Jump[0] < pg.mouse.get_pos()[0] < pos_Jump[0]+200\
                  and pos_Jump[1] < pg.mouse.get_pos()[1] < pos_Jump[1]+80:
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
    imageBG = pg.image.load("bg_main.png")
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
    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [50, 320],[50,370],[50,420],[50,470],[50,520]
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
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [110,330], [110,380], [110,430],[110,480],[110,530]
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    # 插入關卡、未完成任務及已完成任務
    imageCoco = pg.image.load("coco.png")
    imageCoco = pg.transform.scale(imageCoco, (200,450))
    imageLib = pg.image.load("library.png")
    imageLib = pg.transform.scale(imageLib, (190,190))
    imageDorm = pg.image.load("dorm.png")
    imageDorm = pg.transform.scale(imageDorm, (170,170))
    imageLab = pg.image.load("laboratory.png")
    imageLab = pg.transform.scale(imageLab, (170,170))
    imageLake = pg.image.load("lake.png")
    imageLake = pg.transform.scale(imageLake, (170,170))
    imageAlert = pg.image.load("alert.png")

    pos_Lib, pos_Coco, pos_Dorm, pos_Lab, pos_Lake = [200,10],[200,90],[410,330],[410,130],[10,100]
    pos_Alert1 = [310,470]
    bg.blit(imageLib, pos_Lib)
    bg.blit(imageCoco, pos_Coco)
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
                if pos_Coco[0] < pg.mouse.get_pos()[0] < pos_Coco[0]+200\
                  and pos_Coco[1]+100 < pg.mouse.get_pos()[1] < pos_Coco[1]+450:
                # 進入大一遊戲畫面
                    grade += 1
                    stage2(gender, point, grade)
                
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+170\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+170:
                # 進入醉月湖畫面
                    lake(gender, point, grade)

def stage2(gender, point, grade):  # 大二畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_main.png")
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
    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [50, 320],[50,370],[50,420],[50,470],[50,520]
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
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [110,330], [110,380], [110,430],[110,480],[110,530]
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    # 插入關卡、未完成任務及已完成任務
    imageCoco = pg.image.load("coco.png")
    imageCoco = pg.transform.scale(imageCoco, (200,450))
    imageLib = pg.image.load("library.png")
    imageLib = pg.transform.scale(imageLib, (190,190))
    imageDorm = pg.image.load("dorm.png")
    imageDorm = pg.transform.scale(imageDorm, (170,170))
    imageLab = pg.image.load("laboratory.png")
    imageLab = pg.transform.scale(imageLab, (170,170))
    imageLake = pg.image.load("lake.png")
    imageLake = pg.transform.scale(imageLake, (170,170))
    imageAlert = pg.image.load("alert.png")
    imageCheck = pg.image.load("check.png")

    pos_Lib, pos_Coco, pos_Dorm, pos_Lab, pos_Lake = [200,10],[200,90],[410,330],[410,130],[10,100]
    pos_Alert2, pos_Check1 = [310, 120], [310,470]

    bg.blit(imageLib, pos_Lib)
    bg.blit(imageCoco, pos_Coco)
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
                if pos_Lib[0] < pg.mouse.get_pos()[0] < pos_Lib[0]+190\
                  and pos_Lib[1] < pg.mouse.get_pos()[1] < pos_Lib[1]+190:
                # 進入大二遊戲畫面
                    grade += 1
                    stage3(gender, point, grade)
                elif pos_Coco[0] < pg.mouse.get_pos()[0] < pos_Coco[0]+200\
                  and pos_Coco[1]+100 < pg.mouse.get_pos()[1] < pos_Coco[1]+450:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+170\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+170:
                # 進入醉月湖畫面
                    lake(gender, point, grade)

def stage3(gender, point, grade):  # 大三畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_main.png")
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
    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [50, 320],[50,370],[50,420],[50,470],[50,520]
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
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [110,330], [110,380], [110,430],[110,480],[110,530]
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    # 插入關卡、未完成任務及已完成任務
    imageCoco = pg.image.load("coco.png")
    imageCoco = pg.transform.scale(imageCoco, (200,450))
    imageLib = pg.image.load("library.png")
    imageLib = pg.transform.scale(imageLib, (190,190))
    imageDorm = pg.image.load("dorm.png")
    imageDorm = pg.transform.scale(imageDorm, (170,170))
    imageLab = pg.image.load("laboratory.png")
    imageLab = pg.transform.scale(imageLab, (170,170))
    imageLake = pg.image.load("lake.png")
    imageLake = pg.transform.scale(imageLake, (170,170))
    imageAlert = pg.image.load("alert.png")
    imageCheck = pg.image.load("check.png")

    pos_Lib, pos_Coco, pos_Dorm, pos_Lab, pos_Lake = [200,10],[200,90],[410,330],[410,130],[10,100]
    pos_Alert3, pos_Check1, pos_Check2 = [490,440], [310, 120], [310,470]
    bg.blit(imageLib, pos_Lib)
    bg.blit(imageCoco, pos_Coco)
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
                if pos_Dorm[0] < pg.mouse.get_pos()[0] < pos_Dorm[0]+170\
                  and pos_Dorm[1] < pg.mouse.get_pos()[1] < pos_Dorm[1]+170:
                # 進入大三遊戲畫面
                    grade += 1
                    stage4(gender, point, grade)
                elif pos_Coco[0] < pg.mouse.get_pos()[0] < pos_Coco[0]+200\
                  and pos_Coco[1]+100 < pg.mouse.get_pos()[1] < pos_Coco[1]+450:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lib[0] < pg.mouse.get_pos()[0] < pos_Lib[0]+190\
                  and pos_Lib[1] < pg.mouse.get_pos()[1] < pos_Lib[1]+190:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+170\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+170:
                # 進入醉月湖畫面
                    lake(gender, point, grade)

def stage4(gender, point, grade):  # 大四畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_main.png")
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
    pos_Love, pos_Money, pos_Health, pos_Study, pos_Friend = [50, 320],[50,370],[50,420],[50,470],[50,520]
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
    pos_scLove, pos_scMoney, pos_scHealth, pos_scStudy, pos_scFriend = [110,330], [110,380], [110,430],[110,480],[110,530]
    bg.blit(score_Love, pos_scLove)
    bg.blit(score_Money, pos_scMoney)
    bg.blit(score_Health, pos_scHealth)
    bg.blit(score_Study, pos_scStudy)
    bg.blit(score_Friend, pos_scFriend)

    # 插入關卡、未完成任務及已完成任務
    imageCoco = pg.image.load("coco.png")
    imageCoco = pg.transform.scale(imageCoco, (200,450))
    imageLib = pg.image.load("library.png")
    imageLib = pg.transform.scale(imageLib, (190,190))
    imageDorm = pg.image.load("dorm.png")
    imageDorm = pg.transform.scale(imageDorm, (170,170))
    imageLab = pg.image.load("laboratory.png")
    imageLab = pg.transform.scale(imageLab, (170,170))
    imageLake = pg.image.load("lake.png")
    imageLake = pg.transform.scale(imageLake, (170,170))
    imageAlert = pg.image.load("alert.png")
    imageCheck = pg.image.load("check.png")

    pos_Lib, pos_Coco, pos_Dorm, pos_Lab, pos_Lake = [200,10],[200,90],[410,330],[410,130],[10,100]
    pos_Alert4, pos_Check1, pos_Check2, pos_Check3= [490,240], [490,440], [310, 120], [310,470]
    bg.blit(imageLib, pos_Lib)
    bg.blit(imageCoco, pos_Coco)
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
                if pos_Lab[0] < pg.mouse.get_pos()[0] < pos_Lab[0]+170\
                  and pos_Lab[1] < pg.mouse.get_pos()[1] < pos_Lab[1]+170:
                # 進入大四遊戲畫面
                    final(gender, point)
                elif pos_Coco[0] < pg.mouse.get_pos()[0] < pos_Coco[0]+200\
                  and pos_Coco[1]+100 < pg.mouse.get_pos()[1] < pos_Coco[1]+450:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lib[0] < pg.mouse.get_pos()[0] < pos_Lib[0]+190\
                  and pos_Lib[1] < pg.mouse.get_pos()[1] < pos_Lib[1]+190:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Dorm[0] < pg.mouse.get_pos()[0] < pos_Dorm[0]+170\
                  and pos_Dorm[1] < pg.mouse.get_pos()[1] < pos_Dorm[1]+170:
                # 進入skip畫面
                    skip(gender, point, grade)
                elif pos_Lake[0] < pg.mouse.get_pos()[0] < pos_Lake[0]+170\
                  and pos_Lake[1] < pg.mouse.get_pos()[1] < pos_Lake[1]+170:
                # 進入醉月湖畫面
                    lake(gender, point, grade)

def skip(gender, point, grade):  # 非該年級遊戲畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    imageMessage = pg.image.load("finished_msg.png")
    imageMessage = pg.transform.smoothscale(imageMessage,(450,450))
    imageBack = pg.image.load("back_witharrow.png")
    imageBack = pg.transform.scale(imageBack, (120,40))
    imageMessage.convert()
    imageBack.convert()
    pos_Message, pos_Back = [70,70], [80,500]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageBack, pos_Back)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pos_Back[0] < pg.mouse.get_pos()[0] < pos_Back[0]+120\
                  and pos_Back[1] < pg.mouse.get_pos()[1] < pos_Back[1]+40:
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
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    imageMessage = pg.image.load("ending_bubble.png")
    imageMessage = pg.transform.smoothscale(imageMessage,(500,250))
    imageRestart = pg.image.load("restart.png")
    imageRestart = pg.transform.scale(imageRestart,(120,40))
    imageMessage.convert()
    imageRestart.convert()
    pos_Message, pos_Restart = [50,50], [250, 350]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageRestart, pos_Restart)


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
    textPrize = font1.render(prize, True, (165,42,42))
    pos_Prize = [150, 150]
    bg.blit(textPrize, pos_Prize)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:  # 重新開始
                if pos_Restart[0] < pg.mouse.get_pos()[0] < pos_Restart[0]+120\
                  and pos_Restart[1] < pg.mouse.get_pos()[1] < pos_Restart[1]+40:
                    initial()

def gameover():  # 遊戲失敗畫面
    # 設定畫布並插入背景畫面
    bg = pg.Surface((win_width, win_height))
    bg.convert()
    imageBG = pg.image.load("bg_blue.jpg")
    imageBG = pg.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    imageMessage = pg.image.load("expell_msg.png")
    imageMessage = pg.transform.smoothscale(imageMessage,(500,500))
    imageRestart = pg.image.load("restart.png")
    imageRestart = pg.transform.scale(imageRestart,(120,40))
    imageMessage.convert()
    imageRestart.convert()
    pos_Message, pos_Restart = [50,20], [250, 480]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageRestart, pos_Restart)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pg.display.update()

    while True:
        for event in pg.event.get():            
            if event.type == pg.QUIT:  # 關閉程式
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:  # 重新開始
                if pos_Restart[0] < pg.mouse.get_pos()[0] < pos_Restart[0]+120\
                  and pos_Restart[1] < pg.mouse.get_pos()[1] < pos_Restart[1]+40:
                    initial()

if __name__ == '__main__':    
    initial()
