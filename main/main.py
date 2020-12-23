import sys, math
import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT
import webbrowser
import random
from random import randint
import time
import os

# 設定視窗尺寸
win_width, win_height = 600, 600
clock = pygame.time.Clock()

pygame.init()
# 設定字型
font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 28)
font3 = pygame.font.Font(None, 20)
font4 = pygame.font.Font(None, 40)
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("My Life in NTU")  # 設定視窗標題

def initial():  # 遊戲初始畫面
    # 設定畫布並插入背景圖片
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_blue.jpg")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入遊戲標題與開始鍵
    imageTitle = pygame.image.load("my life in ntu.png")
    imageTitle = pygame.transform.scale(imageTitle,(400,200))
    imageStart = pygame.image.load("start.png")
    imageTitle.convert()
    imageStart.convert()
    pos_Title = [100, 100]
    pos_Start = [190, 450]
    bg.blit(imageTitle, pos_Title)
    bg.blit(imageStart, pos_Start)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # 點選並進入遊戲說明
                if pos_Start[0] < pygame.mouse.get_pos()[0] < pos_Start[0]+150\
                  and pos_Start[1] < pygame.mouse.get_pos()[1] < pos_Start[1]+100:
                    intro()  # 進入遊戲說明

def intro():  # 遊戲說明畫面
    # 設定畫布並插入背景圖片
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_blue.jpg")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入老師、對話框、繼續圖片
    imageMessage = pygame.image.load("start_msg.png")
    imageMessage = pygame.transform.smoothscale(imageMessage,(500, 500))
    imageTeacher = pygame.image.load("teacher.png")
    imageTeacher = pygame.transform.scale(imageTeacher,(230, 230))
    imageNext = pygame.image.load("next_witharrow.png")
    imageNext = pygame.transform.scale(imageNext, (100,30))
    imageTeacher.convert()
    imageMessage.convert()
    imageNext.convert()
    pos_Teacher, pos_Message, pos_Next = [50,370],[50,0], [420,450]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageTeacher,pos_Teacher)
    bg.blit(imageNext, pos_Next)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # 點選並進入角色選擇畫面
                if pos_Next[0] < pygame.mouse.get_pos()[0] < pos_Next[0]+100\
                  and pos_Next[1] < pygame.mouse.get_pos()[1] < pos_Next[1]+30:
                    point = {"Love": 60, "Money":60, "Health":60, "Study":60, "Friend":60}
                    grade = 1
                    stage1(point, grade)    

# def rolechoose():  # 角色選擇畫面
#     # 設定畫布並插入背景畫面
#     bg = pygame.Surface((win_width, win_height))
#     bg.convert()
#     imageBG = pygame.image.load("bg_blue.jpg")
#     imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
#     imageBG.convert()
#     bg.blit(imageBG, (0,0))

#     # 插入 姓名、性別、Play圖片
#     imageName = pygame.image.load("name.png")
#     imageName = pygame.transform.scale(imageName, (120,35))
#     textGender = font2.render("Gender:", True, (0,0,0))
#     imageNMale = pygame.image.load("male_grey.png")  # 灰底(未選擇)
#     imageNMale = pygame.transform.scale(imageNMale, (120,35))
#     imageNFemale = pygame.image.load("female_grey.png")  # 灰底(未選擇)
#     imageNFemale = pygame.transform.scale(imageNFemale, (120,35))
#     imagePlay = pygame.image.load("play.png")
#     imagePlay = pygame.transform.scale(imagePlay, (120,35))
#     imageMale = pygame.image.load("male.png")  # 藍底(選擇)
#     imageMale = pygame.transform.scale(imageMale, (120,35))
#     imageFemale = pygame.image.load("female.png")  # 藍底(選擇)
#     imageFemale = pygame.transform.scale(imageFemale, (120,35))
#     imageName.convert()
#     imageNMale.convert()
#     imageNFemale.convert()
#     imagePlay.convert()
#     imageMale.convert()
#     imageFemale.convert()
#     pos_Name, pos_Gender, pos_NMale, pos_NFemale, pos_Play = [80, 150],[100, 250],[220, 250], [380, 250], [250, 340]
#     bg.blit(imageName, pos_Name)
#     bg.blit(textGender, pos_Gender)
#     bg.blit(imageNMale, pos_NMale)
#     bg.blit(imageNFemale, pos_NFemale)
#     bg.blit(imagePlay, pos_Play)
    
#     # 顯示畫布
#     screen.blit(bg,(0,0))
#     pygame.display.update()
#     gender = ""  # 記錄角色性別

#     while True:
#         for event in pygame.event.get():   
#             if event.type == pygame.QUIT:  # 關閉程式
#                 pygame.quit()
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if pos_NMale[0] < pygame.mouse.get_pos()[0] < pos_NMale[0]+100\
#                   and pos_NMale[1] < pygame.mouse.get_pos()[1] < pos_NMale[1]+50:
#                 # 選擇男性
#                     gender = "Male"
#                     pos_Male = [220, 250]
#                     bg.blit(imageMale, pos_Male)
#                     bg.blit(imageNFemale, pos_NFemale)  # 灰底Female覆蓋
#                 elif pos_NFemale[0] < pygame.mouse.get_pos()[0] < pos_NFemale[0]+100\
#                   and pos_NFemale[1] < pygame.mouse.get_pos()[1] < pos_NFemale[1]+50:
#                 # 選擇女性
#                     gender = "Female"
#                     pos_Female = [380, 250]
#                     bg.blit(imageFemale, pos_Female)
#                     bg.blit(imageNMale, pos_NMale)   # 灰底Male覆蓋
                
#                 screen.blit(bg, (0,0))
#                 pygame.display.update()
            
#                 if pos_Play[0] < pygame.mouse.get_pos()[0] < pos_Play[0]+100\
#                   and pos_Play[1] < pygame.mouse.get_pos()[1] < pos_Play[1]+50:
#                     if gender != "":  # 進入大一畫面
#                     # 記錄初始化分數、年級
#                         point = {"Love": 60, "Money":60, "Health":60, "Study":60, "Friend":60}
#                         grade = 1
#                         stage1(gender, point, grade)

def lake(point, grade):  # 醉月湖畫面
    # 設定畫布並插入背景畫面
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_lake.jpg")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))    
    
    # 插入圖片、對話框、繼續圖片
    imageMessage = pygame.image.load("lake_bubble.png")
    imageMessage = pygame.transform.smoothscale(imageMessage,(550,200))
    imageJump = pygame.image.load("jump.png")
    imageJump = pygame.transform.smoothscale(imageJump,(200,60))
    imageNojump = pygame.image.load("nojump.png")
    imageNojump = pygame.transform.smoothscale(imageNojump,(200,60))
    imageMessage.convert()
    imageJump.convert()
    imageNojump.convert()
    pos_Message, pos_Jump, pos_Nojump = [20,370],  [310,420], [80,420]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageJump, pos_Jump)
    bg.blit(imageNojump, pos_Nojump)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos_Nojump[0] < pygame.mouse.get_pos()[0] < pos_Nojump[0]+200\
                  and pos_Nojump[1] < pygame.mouse.get_pos()[1] < pos_Nojump[1]+80:
                    # 回到各年級畫面
                    if grade == 1:
                        stage1(point, grade)
                    elif grade == 2:
                        stage2(point, grade)
                    elif grade == 3:
                        stage3(point, grade)
                    elif grade == 4:
                        stage4(point, grade)
                
                if pos_Jump[0] < pygame.mouse.get_pos()[0] < pos_Jump[0]+200\
                  and pos_Jump[1] < pygame.mouse.get_pos()[1] < pos_Jump[1]+80:
                    # 扣分、開啟網頁
                    point["Health"] -= 10
                    if point["Health"] <= 0:
                        point["Health"] = 0
                    webbrowser.open("https://scc_osa.ntu.edu.tw")
                    
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

                    # 回到各年級畫面
                    if grade == 1:
                        stage1(point, grade)
                    elif grade == 2:
                        stage2(point, grade)
                    elif grade == 3:
                        stage3(point, grade)
                    elif grade == 4:
                        stage4(point, grade)

def stage1(point, grade):  # 大一畫面
    # 設定畫布並插入背景畫面
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_main.png")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入能力值
    imageLove = pygame.image.load("love.png")
    imageLove = pygame.transform.scale(imageLove, (40,40))
    imageMoney = pygame.image.load("money.png")
    imageMoney = pygame.transform.scale(imageMoney, (40,40))
    imageHealth = pygame.image.load("Health.png")
    imageHealth = pygame.transform.scale(imageHealth, (40,40))
    imageStudy = pygame.image.load("study.png")
    imageStudy = pygame.transform.scale(imageStudy, (40,40))
    imageFriend = pygame.image.load("friend.png")
    imageFriend = pygame.transform.scale(imageFriend, (40,40))
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
    imageCoco = pygame.image.load("coco.png")
    imageCoco = pygame.transform.scale(imageCoco, (200,450))
    imageLib = pygame.image.load("library.png")
    imageLib = pygame.transform.scale(imageLib, (190,190))
    imageDorm = pygame.image.load("dorm.png")
    imageDorm = pygame.transform.scale(imageDorm, (170,170))
    imageLab = pygame.image.load("laboratory.png")
    imageLab = pygame.transform.scale(imageLab, (170,170))
    imageLake = pygame.image.load("lake.png")
    imageLake = pygame.transform.scale(imageLake, (170,170))
    imageAlert = pygame.image.load("alert.png")

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
    pygame.display.update()

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
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos_Coco[0] < pygame.mouse.get_pos()[0] < pos_Coco[0]+200\
                  and pos_Coco[1]+100 < pygame.mouse.get_pos()[1] < pos_Coco[1]+450:
                # 進入大一遊戲畫面
                    grade += 1
                    
                    # adj_Love, adj_Money, adj_Health, adj_Study, adj_Friend = game1_start()
                    # print(adj_Love, adj_Money, adj_Health, adj_Study, adj_Friend)
                    # point["Love"] += adj_Love
                    # point["Money"] += adj_Money
                    # point["Health"] += adj_Health
                    # point["Study"] += adj_Study
                    # point["Friend"] += adj_Friend

                    # # 計算是否失敗
                    # point_list = list(point.items())
                    # point_list.sort(key=lambda x:x[1], reverse=True)
                    # sum_zero_point = 0
                    # for pairs in point_list:
                    #     pairs_list = list(pairs)
                    #     if pairs_list[1] == 0:
                    #         sum_zero_point += 1
                    # if sum_zero_point >= 3:
                    #     gameover()
                    
                    stage2(point, grade)
                
                elif pos_Lake[0] < pygame.mouse.get_pos()[0] < pos_Lake[0]+170\
                  and pos_Lake[1] < pygame.mouse.get_pos()[1] < pos_Lake[1]+170:
                # 進入醉月湖畫面
                    lake(point, grade)

def stage2(point, grade):  # 大二畫面
    # 設定畫布並插入背景畫面
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_main.png")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入能力值
    imageLove = pygame.image.load("love.png")
    imageLove = pygame.transform.scale(imageLove, (40,40))
    imageMoney = pygame.image.load("money.png")
    imageMoney = pygame.transform.scale(imageMoney, (40,40))
    imageHealth = pygame.image.load("Health.png")
    imageHealth = pygame.transform.scale(imageHealth, (40,40))
    imageStudy = pygame.image.load("study.png")
    imageStudy = pygame.transform.scale(imageStudy, (40,40))
    imageFriend = pygame.image.load("friend.png")
    imageFriend = pygame.transform.scale(imageFriend, (40,40))
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
    imageCoco = pygame.image.load("coco.png")
    imageCoco = pygame.transform.scale(imageCoco, (200,450))
    imageLib = pygame.image.load("library.png")
    imageLib = pygame.transform.scale(imageLib, (190,190))
    imageDorm = pygame.image.load("dorm.png")
    imageDorm = pygame.transform.scale(imageDorm, (170,170))
    imageLab = pygame.image.load("laboratory.png")
    imageLab = pygame.transform.scale(imageLab, (170,170))
    imageLake = pygame.image.load("lake.png")
    imageLake = pygame.transform.scale(imageLake, (170,170))
    imageAlert = pygame.image.load("alert.png")
    imageCheck = pygame.image.load("check.png")

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
    pygame.display.update()
    
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
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos_Lib[0] < pygame.mouse.get_pos()[0] < pos_Lib[0]+190\
                  and pos_Lib[1] < pygame.mouse.get_pos()[1] < pos_Lib[1]+190:
                # 進入大二遊戲畫面
                    grade += 1

                    adj_Love, adj_Money, adj_Health, adj_Study, adj_Friend = game2_start()
                    point["Love"] += adj_Love
                    point["Money"] += adj_Money
                    point["Health"] += adj_Health
                    point["Study"] += adj_Study
                    point["Friend"] += adj_Friend

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
                    stage3(point, grade)
                elif pos_Coco[0] < pygame.mouse.get_pos()[0] < pos_Coco[0]+200\
                  and pos_Coco[1]+100 < pygame.mouse.get_pos()[1] < pos_Coco[1]+450:
                # 進入skip畫面
                    skip(point, grade)
                elif pos_Lake[0] < pygame.mouse.get_pos()[0] < pos_Lake[0]+170\
                  and pos_Lake[1] < pygame.mouse.get_pos()[1] < pos_Lake[1]+170:
                # 進入醉月湖畫面
                    lake(point, grade)

def stage3(point, grade):  # 大三畫面
    # 設定畫布並插入背景畫面
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_main.png")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入能力值
    imageLove = pygame.image.load("love.png")
    imageLove = pygame.transform.scale(imageLove, (40,40))
    imageMoney = pygame.image.load("money.png")
    imageMoney = pygame.transform.scale(imageMoney, (40,40))
    imageHealth = pygame.image.load("Health.png")
    imageHealth = pygame.transform.scale(imageHealth, (40,40))
    imageStudy = pygame.image.load("study.png")
    imageStudy = pygame.transform.scale(imageStudy, (40,40))
    imageFriend = pygame.image.load("friend.png")
    imageFriend = pygame.transform.scale(imageFriend, (40,40))
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
    imageCoco = pygame.image.load("coco.png")
    imageCoco = pygame.transform.scale(imageCoco, (200,450))
    imageLib = pygame.image.load("library.png")
    imageLib = pygame.transform.scale(imageLib, (190,190))
    imageDorm = pygame.image.load("dorm.png")
    imageDorm = pygame.transform.scale(imageDorm, (170,170))
    imageLab = pygame.image.load("laboratory.png")
    imageLab = pygame.transform.scale(imageLab, (170,170))
    imageLake = pygame.image.load("lake.png")
    imageLake = pygame.transform.scale(imageLake, (170,170))
    imageAlert = pygame.image.load("alert.png")
    imageCheck = pygame.image.load("check.png")

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
    pygame.display.update()
    


    while True:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos_Dorm[0] < pygame.mouse.get_pos()[0] < pos_Dorm[0]+170\
                  and pos_Dorm[1] < pygame.mouse.get_pos()[1] < pos_Dorm[1]+170:
                # 進入大三遊戲畫面
                    grade += 1
                    adj_Love, adj_Money, adj_Health, adj_Study, adj_Friend = game3()
                    point["Love"] += adj_Love
                    point["Money"] += adj_Money
                    point["Health"] += adj_Health
                    point["Study"] += adj_Study
                    point["Friend"] += adj_Friend

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

                    stage4(point, grade)
                elif pos_Coco[0] < pygame.mouse.get_pos()[0] < pos_Coco[0]+200\
                  and pos_Coco[1]+100 < pygame.mouse.get_pos()[1] < pos_Coco[1]+450:
                # 進入skip畫面
                    skip(point, grade)
                elif pos_Lib[0] < pygame.mouse.get_pos()[0] < pos_Lib[0]+190\
                  and pos_Lib[1] < pygame.mouse.get_pos()[1] < pos_Lib[1]+190:
                # 進入skip畫面
                    skip(point, grade)
                elif pos_Lake[0] < pygame.mouse.get_pos()[0] < pos_Lake[0]+170\
                  and pos_Lake[1] < pygame.mouse.get_pos()[1] < pos_Lake[1]+170:
                # 進入醉月湖畫面
                    lake(point, grade)

def stage4(point, grade):  # 大四畫面
    # 設定畫布並插入背景畫面
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_main.png")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    # 插入能力值
    imageLove = pygame.image.load("love.png")
    imageLove = pygame.transform.scale(imageLove, (40,40))
    imageMoney = pygame.image.load("money.png")
    imageMoney = pygame.transform.scale(imageMoney, (40,40))
    imageHealth = pygame.image.load("Health.png")
    imageHealth = pygame.transform.scale(imageHealth, (40,40))
    imageStudy = pygame.image.load("study.png")
    imageStudy = pygame.transform.scale(imageStudy, (40,40))
    imageFriend = pygame.image.load("friend.png")
    imageFriend = pygame.transform.scale(imageFriend, (40,40))
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
    imageCoco = pygame.image.load("coco.png")
    imageCoco = pygame.transform.scale(imageCoco, (200,450))
    imageLib = pygame.image.load("library.png")
    imageLib = pygame.transform.scale(imageLib, (190,190))
    imageDorm = pygame.image.load("dorm.png")
    imageDorm = pygame.transform.scale(imageDorm, (170,170))
    imageLab = pygame.image.load("laboratory.png")
    imageLab = pygame.transform.scale(imageLab, (170,170))
    imageLake = pygame.image.load("lake.png")
    imageLake = pygame.transform.scale(imageLake, (170,170))
    imageAlert = pygame.image.load("alert.png")
    imageCheck = pygame.image.load("check.png")

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
    pygame.display.update()

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
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos_Lab[0] < pygame.mouse.get_pos()[0] < pos_Lab[0]+170\
                  and pos_Lab[1] < pygame.mouse.get_pos()[1] < pos_Lab[1]+170:
                # 進入大四遊戲畫面
                    adj_Love, adj_Money, adj_Health, adj_Study, adj_Friend = game4_start()
                    point["Love"] += adj_Love
                    point["Money"] += adj_Money
                    point["Health"] += adj_Health
                    point["Study"] += adj_Study
                    point["Friend"] += adj_Friend

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

                    final(point)
                elif pos_Coco[0] < pygame.mouse.get_pos()[0] < pos_Coco[0]+200\
                  and pos_Coco[1]+100 < pygame.mouse.get_pos()[1] < pos_Coco[1]+450:
                # 進入skip畫面
                    skip(point, grade)
                elif pos_Lib[0] < pygame.mouse.get_pos()[0] < pos_Lib[0]+190\
                  and pos_Lib[1] < pygame.mouse.get_pos()[1] < pos_Lib[1]+190:
                # 進入skip畫面
                    skip(point, grade)
                elif pos_Dorm[0] < pygame.mouse.get_pos()[0] < pos_Dorm[0]+170\
                  and pos_Dorm[1] < pygame.mouse.get_pos()[1] < pos_Dorm[1]+170:
                # 進入skip畫面
                    skip(point, grade)
                elif pos_Lake[0] < pygame.mouse.get_pos()[0] < pos_Lake[0]+170\
                  and pos_Lake[1] < pygame.mouse.get_pos()[1] < pos_Lake[1]+170:
                # 進入醉月湖畫面
                    lake(point, grade)

def skip(point, grade):  # 非該年級遊戲畫面
    # 設定畫布並插入背景畫面
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_blue.jpg")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    imageMessage = pygame.image.load("finished_msg.png")
    imageMessage = pygame.transform.smoothscale(imageMessage,(450,450))
    imageBack = pygame.image.load("back_witharrow.png")
    imageBack = pygame.transform.scale(imageBack, (100,30))
    imageMessage.convert()
    imageBack.convert()
    pos_Message, pos_Back = [70,40], [80,450]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageBack, pos_Back)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos_Back[0] < pygame.mouse.get_pos()[0] < pos_Back[0]+100\
                  and pos_Back[1] < pygame.mouse.get_pos()[1] < pos_Back[1]+30:
                    # 回到各年級畫面
                    if grade == 1:
                        stage1(point, grade)
                    elif grade == 2:
                        stage2(point, grade)
                    elif grade == 3:
                        stage3(point, grade)
                    elif grade == 4:
                        stage4(point, grade)

def final(point):  # 遊戲結束畫面
    # 設定畫布並插入背景畫面
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_blue.jpg")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    imageMessage = pygame.image.load("ending_bubble.png")
    imageMessage = pygame.transform.smoothscale(imageMessage,(500,250))
    imageFinish = pygame.image.load("finish.png")
    imageFinish = pygame.transform.scale(imageFinish,(130,40))
    imageRestart = pygame.image.load("restart.png")
    imageRestart = pygame.transform.scale(imageRestart,(150,40))
    imageMessage.convert()
    imageFinish.convert()
    imageRestart.convert()
    pos_Message, pos_Finish, pos_Restart = [50,50], [400,400], [400, 470]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageFinish, pos_Finish)
    bg.blit(imageRestart, pos_Restart)


    # 成績結算
    point_list = list(point.items())
    point_list.sort(key=lambda x:x[1], reverse=True)
    result = list(point_list[0])
    prize = ""
    if result[0] == "Health":
        prize = "Sunshine Boy"
    elif result[0] == "Love":
        prize = "Heartthrob"
    elif result[0] == "Friend":
        prize = "King of Friends"
    elif result[0] == "Money":
        prize = "Rich man"
    elif result[0] == "Study":
        prize = "knowledgeable Boy"
    
    # 顯示遊戲結果
    textPrize = font1.render(prize, True, (165,42,42))
    pos_Prize = [150, 150]
    bg.blit(textPrize, pos_Prize)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # 重新開始
                if pos_Restart[0] < pygame.mouse.get_pos()[0] < pos_Restart[0]+130\
                  and pos_Restart[1] < pygame.mouse.get_pos()[1] < pos_Restart[1]+40:
                    pygame.quit()
                    sys.exit()
                elif pos_Restart[0] < pygame.mouse.get_pos()[0] < pos_Restart[0]+150\
                  and pos_Restart[1] < pygame.mouse.get_pos()[1] < pos_Restart[1]+40:
                    initial()

def gameover():  # 遊戲失敗畫面
    # 設定畫布並插入背景畫面
    bg = pygame.Surface((win_width, win_height))
    bg.convert()
    imageBG = pygame.image.load("bg_blue.jpg")
    imageBG = pygame.transform.scale(imageBG,(win_width, win_height))
    imageBG.convert()
    bg.blit(imageBG, (0,0))

    imageMessage = pygame.image.load("gameover.png")
    imageMessage = pygame.transform.smoothscale(imageMessage,(450,450))
    imageRestart = pygame.image.load("restart.png")
    imageRestart = pygame.transform.scale(imageRestart,(140,40))
    imageMessage.convert()
    imageRestart.convert()
    pos_Message, pos_Restart = [70,40], [220,450]
    bg.blit(imageMessage, pos_Message)
    bg.blit(imageRestart, pos_Restart)

    # 顯示畫布
    screen.blit(bg, (0,0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:  # 關閉程式
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # 重新開始
                if pos_Restart[0] < pygame.mouse.get_pos()[0] < pos_Restart[0]+120\
                  and pos_Restart[1] < pygame.mouse.get_pos()[1] < pos_Restart[1]+40:
                    initial()

def game1_start():
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
            # pygame.init()        
            self.gameDisplay = pygame.display.set_mode((600, 600))
            # pygame.display.set_caption('Dodge people on Palm Avenue!')
            
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
                    # pygame.quit()
                    # quit()
                    time.sleep(1)
                    return romantic_relationship, money, health, academic_performance, interpersonal_relationship
                    # pygame.quit()
                    # quit()
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
                    # pygame.quit()
                    # quit()
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
    


def game2_start():
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
    '''
    pygame.init()

    pygame.display.set_caption('Stop Procrastinating!')'''
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
        
            RESUME = Line(157, 34, 350,
                          400, WINDOW_WIDTH, WINDOW_HEIGHT, 'G2-resume.png')
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


def game3():
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
    
    '''
    pygame.init()
    
    # load window surface
    pygame.display.set_caption('Choose Wisely')
    '''
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    group = pygame.sprite.Group()

    ok = Picture(300-40, 480,'ok.png', 0)
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
                    romantic_relationship = 30
                    interpersonal_relationship = 10
                    money = 0
                elif 60 < score <= 70:
                    academic_performance = -10
                    romantic_relationship = 20
                    interpersonal_relationship = 10
                    money = 0
                elif 70 < score <= 80:
                    academic_performance = 0
                    romantic_relationship = 10
                    interpersonal_relationship = 10
                    money = 0
                elif 80 < score <= 90:
                    academic_performance = 10
                    romantic_relationship = -10
                    interpersonal_relationship = 0
                    money = 0
                else:
                    academic_performance = 30
                    romantic_relationship = 0  # 學霸加成
                    interpersonal_relationship = 10
                    money = 20
                
                text_surface_list = []
                text_surface_list = print_sirting(
                                              academic_performance, romantic_relationship,
                                              interpersonal_relationship, money, text_surface_list)
                RESUME = Line(157, 34, 400,
                          500, WINDOW_WIDTH, WINDOW_HEIGHT, 'resume.png')
                window_surface.blit(RESUME.image, RESUME.rect)
                for i in range(len(text_surface_list)):
                    window_surface.blit(
                        text_surface_list[i], (300, 220 + 70*i))  # text position

        elif page == 0:  # 遊戲說明畫面
            background_raw = pygame.image.load(
                'G3-background2.jpg')
            # 調整背景圖片大小
            background = pygame.transform.scale(
                background_raw, (WINDOW_WIDTH, WINDOW_HEIGHT))
            background.convert()
            window_surface.blit(background, (0, 0))
            
            # RESUME button
            RESUME = Picture(400, 500, 'start.png', 0)
            RESUME.image = pygame.transform.scale(RESUME.raw_image, (117, 34))
            RESUME.width = 117
            RESUME.height = 34
            window_surface.blit(RESUME.image, RESUME.rect)
            
            # introduction text
            my_intro_font = pygame.font.SysFont(None, 50)
            intro_text = my_intro_font.render(
                'this is the introduction.', True, (0, 0, 0))
            window_surface.blit(intro_text, (10, 10))
        
        pygame.display.update()
        # 控制遊戲迴圈迭代速率
        main_clock.tick(FPS)


def game4_start():
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    BOSSWIDTH = 100
    BOSSHEIGHT = 470
    COMPUTERWIDTH = 300
    COMPUTERHEIGHT = 320
    PHONEWIDTH = 50
    PHONEHEIGHT = 60
    FPS = 10
    boss_x_position = 5
    boss_y_position = 120
    computer_x_position = 150
    computer_y_position = 220
    phone_x_position = 500
    phone_y_position = 450
    show_probability1 = 60  # 每次顯示通知機率 (%)
    # show_probability2 = 30
    bosspath = os.path.abspath('G4-boss.gif')
    computerpath = os.path.abspath('G4-computer.gif')
    phonepath = os.path.abspath('G4-phone.gif')


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
            self.image = pygame.transform.scale(self.raw_image, (width, height))
            #  回傳位置
            self.rect = self.image.get_rect()
            #  定位
            self.rect.topleft = (x_position, y_position)
            self.width = width
            self.height = height
            self.window_width = window_width
            self.window_height = window_height
        
    '''
    pygame.init()
    # load window surface
    pygame.display.set_caption('Maximize Your Utility!')
    '''
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
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


    while True:

        if game_over_time == 0 and pygame.time.get_ticks()-start_ticks > 4000:  # 遊戲打開 {} 秒後結束
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
                    BossIsHere = True
                    PATH = bosspath
                    boss = Line(BOSSWIDTH, BOSSHEIGHT, boss_x_position, boss_y_position, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                    #老闆出現
                elif ran_number > show_probability1:
                    # hide (藏在右下)
                    PATH = bosspath
                    boss = Line(BOSSWIDTH, BOSSHEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, PATH)
                    BossIsHere = False

            if event.type == MOUSEBUTTONDOWN and game_over_time == 0 and BossIsHere is True:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在電腦上
                if computer.rect.topleft[0] < pygame.mouse.get_pos()[0] < computer.rect.topleft[0] + COMPUTERWIDTH \
                   and computer.rect.topleft[1] < pygame.mouse.get_pos()[1] < computer.rect.topleft[1] + COMPUTERHEIGHT:
                    # 算分
                    salary += 500
                else:
                    salary -= 500

                if salary <= 0:
                    salary = 0

            elif event.type == MOUSEBUTTONDOWN and game_over_time == 0 and BossIsHere is False:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在手機上
                if phone.rect.topleft[0] < pygame.mouse.get_pos()[0] < phone.rect.topleft[0] + PHONEWIDTH \
                   and phone.rect.topleft[1] < pygame.mouse.get_pos()[1] < phone.rect.topleft[1] + PHONEHEIGHT:
                   
                    # 算分
                    satisfaction += 500
                
                else:
                    satisfaction -= 500

                if satisfaction <= 0:
                    satisfaction = 0
                    
            # 遊戲結束之後按下 RESUME 之後的動作
            elif event.type == MOUSEBUTTONDOWN and game_over_time == 1:
                if RESUME.rect.topleft[0] < pygame.mouse.get_pos()[0] < RESUME.rect.topleft[0] + RESUME.width \
                        and RESUME.rect.topleft[1] < pygame.mouse.get_pos()[1] < RESUME.rect.topleft[1] + RESUME.height:
                    return romantic_relationship, wealth, health, academic_performance, 0

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

            text_surface_list = print_sirting(academic_performance, romantic_relationship, wealth, health, text_surface_list)
            love = Line(60, 60, 50, 50,
                       WINDOW_WIDTH, WINDOW_HEIGHT, 'love.png')
            money = Line(60, 60, 50, 50 + 70*1,
                        WINDOW_WIDTH, WINDOW_HEIGHT, 'money.png')
            health = Line(60, 60, 50,
                         50+70*2, WINDOW_WIDTH, WINDOW_HEIGHT, 'health.png')
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
                          500, WINDOW_WIDTH, WINDOW_HEIGHT, 'resume.png')
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
                          500, WINDOW_WIDTH, WINDOW_HEIGHT, 'resume.png')
            window_surface.blit(RESUME.image, RESUME.rect)
            intro_text = my_final_font.render(
                'this is the introduction.', True, (0, 0, 0))
            window_surface.blit(intro_text, (10, 10))

        pygame.display.update()
        # 控制遊戲迴圈迭代速率
        main_clock.tick(FPS)

if __name__ == '__main__':    
    # initial()
    gameover()