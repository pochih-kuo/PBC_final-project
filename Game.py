import tkinter as tk
import tkinter.font as tkFont

class basedesk():
    def __init__(self, master):
        self.game = master
        self.game.config(background='white')
        self.game.title('My Life in NTU')
        self.game.geometry('800x600')
        
        initface(self.game)    

class initface():  # 遊戲初始畫面
    def __init__(self,master):
        self.master = master
        self.master.config()
        self.initface = tk.Frame(self.master,)
        self.initface.pack()
        
        f1 = tkFont.Font(size = 48)  # 遊戲標題
        self.enterName = tk.Label(self.initface, text='My Life in NTU', font=f1)
        self.enterName.grid(column=0, row=0, ipadx=5, pady=100, sticky=tk.W+tk.N)
        
        f2 = tkFont.Font(size = 24)  # 開始遊戲按鈕
        self.begin_btn = tk.Button(self.initface,text='開始遊戲',font=f2, command=self.change)
        self.begin_btn.grid(column=0, row=1, ipadx=5, pady=50)

    def change(self,):  # 切換至使用者角色選擇畫面
        self.initface.destroy()
        face1(self.master)      

class face1():  # 使用者角色選擇畫面
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.face1 = tk.Frame(self.master,)
        self.face1.pack()
        
        f1 = tkFont.Font(size=20)
        # 輸入使用者姓名
        self.enterName = tk.Label(self.face1, text = "請輸入名字：", font=f1)
        self.txtName = tk.Text(self.face1, height = 2, width = 20)
        self.enterSex = tk.Label(self.face1, text = "性別：", font=f1)
        # 選擇性別
        self.btnMale = tk.Button(self.face1, text='MALE', font=f1, command=self.clickBtnMale)
        self.btnFemale = tk.Button(self.face1, text='FEMALE', font=f1, command=self.clickBtnFemale)
        # 輸入完成
        self.btn_enter = tk.Button(self.face1,text='確認', font=f1, command=self.login)

        self.enterName.grid(column=0, row=0, ipadx=5, pady=100)
        self.txtName.grid(column=1, row=0, ipadx=5, pady=100, columnspan = 2)
        self.enterSex.grid(column=0, row=1, ipadx=5, pady=10)
        self.btnMale.grid(column=1, row=1, ipadx=5, pady=10)
        self.btnFemale.grid(column=2, row=1, ipadx=5, pady=10)
        self.btn_enter.grid(column=0, row=2, ipadx=5, pady=10, columnspan = 3)

    def clickBtnMale(self):  # 確認角色性別
        self.sex = '' 
        self.sex = 'Male'
        return self.sex

    def clickBtnFemale(self):  # 確認角色性別
        self.sex = ''
        self.sex = 'Female'
        return self.sex

    def login(self):  # 切換至遊戲主畫面
        self.face1.destroy()
        main(self.master)

class main():  # 遊戲主畫面
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.main = tk.Frame(self.master,)
        self.main.pack()
        
        f1 = tkFont.Font(size=10)
        f2 = tkFont.Font(size=14)

        capability = {'love':20, 'health':20, 'wealth':20, 'academic':20, 'interpersonal':20}
        # 顯示能力與數值
        self.enterLove = tk.Label(self.main, text = '愛情', font=f1)
        self.enterHeal = tk.Label(self.main, text = '健康', font=f1)
        self.enterWeal = tk.Label(self.main, text = '財富', font=f1)
        self.enterAcad = tk.Label(self.main, text = '學業', font=f1)
        self.enterInter = tk.Label(self.main, text = '人際關係', font=f1)
        self.valLove = tk.Label(self.main, text = str(capability['love']), font=f2)
        self.valHeal = tk.Label(self.main, text = str(capability['health']), font=f2)
        self.valWeal = tk.Label(self.main, text = str(capability['wealth']), font=f2)
        self.valAcad = tk.Label(self.main, text = str(capability['academic']), font=f2)
        self.valInter =tk.Label(self.main, text = str(capability['interpersonal']), font=f2)

        self.enterLove.grid(column=0, row=0, sticky=tk.W+tk.N)
        self.enterHeal.grid(column=0, row=1, sticky=tk.W+tk.N)
        self.enterWeal.grid(column=0, row=2, sticky=tk.W+tk.N)
        self.enterAcad.grid(column=0, row=3, sticky=tk.W+tk.N)
        self.enterInter.grid(column=0, row=4, sticky=tk.W+tk.N)
        self.valLove.grid(column=1, row=0, sticky=tk.W+tk.N)
        self.valHeal.grid(column=1, row=1, sticky=tk.W+tk.N)
        self.valWeal.grid(column=1, row=2, sticky=tk.W+tk.N)
        self.valAcad.grid(column=1, row=3, sticky=tk.W+tk.N)
        self.valInter.grid(column=1, row=4, sticky=tk.W+tk.N)

if __name__ == '__main__':    
    game = tk.Tk()
    basedesk(game)
    game.mainloop()

