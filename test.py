from tkinter import *
from tkinter import messagebox
import time
import random
from winsound import *
class SnakeLadder:
    def __init__(self,canvas):
        self.canvas=canvas      
        startbtn=Button(tk,image=startbtnphoto,command=Startgame,borderwidth=2)
        self.startbtn=startbtn
        exitbtn=Button(tk,image=exitbtnphoto,borderwidth=2,command=aexit)
        self.exitbtn=exitbtn
        howto=Button(tk,image=howtoplay,borderwidth=2)
        self.howto=howto
    def create_btn(self):#สร้างปุ่มสร้างรูป
        self.startbtn.place(x=150,y=375)
        self.exitbtn.place(x=700,y=375)
        self.howto.place(x=430,y=375)
        self.canvas.create_image(0,800,anchor=SW,image=snack_id)
    def delete_btn(self):#ลบปุม start exit
        self.startbtn.destroy()
        self.exitbtn.destroy()
        self.howto.destroy()
class page2:
    def __init__(self,canvas):
        self.x1=150
        self.y1=670
        self.x2=160
        self.y2=680
      
        
        self.point=0
        
        self.point1=0
        self.canvas=canvas
        self.i=0
        homebtn=Button(tk,image=backbutton,command=homepage1,borderwidth=5)
        self.homebtn=homebtn
        global dicebutton
        dicebutton=Button(tk,image=dicephoto,command=Toy555)
        self.dicebutton=dicebutton
       
    def create_btn(self):
        self.homebtn.place(x=880,y=700)
        self.dicebutton.place(x=880,y=20)
        self.canvas.create_image(0,800,anchor=SW,image=startedphoto)
    def delete_btn(self):#ลบปุ่ม
        self.homebtn.destroy()
        self.dicebutton.destroy()
    
    def deletePhotab(self):
        number=random.choice(['1','2','3','4','5','6'])
        self.number=number
        self.number1=int(number)
        if self.number1==1:
             print(1)
             PlaySound('1.WAV', SND_FILENAME)   
        if self.number1==2:
             print(2)
             PlaySound('2.WAV', SND_FILENAME) 
        if self.number1==3:
             print(3)
             PlaySound('3.WAV', SND_FILENAME) 
        if self.number1==4:
             print(4)
             PlaySound('4.WAV', SND_FILENAME) 
        if self.number1==5:
             print(5)
             PlaySound('5.WAV', SND_FILENAME) 
        if self.number1==6:
             print(6)
             PlaySound('6.WAV', SND_FILENAME)
        self.image={'1':Photoone,'2':Phototwo,'3':Photothree,'4':Photofour,'5':Photofive,'6':Photosix,}
        self.i+=1
        if self.i%2 !=0:
            
            self.tab2=canvas.create_image(150,100,anchor=SW,image=Phototab1)
            self.showtoy=canvas.create_image(482,75,anchor=SW,image=self.image[self.number])
   
        else:
            
            canvas.delete(self.tab2)
            self.a=canvas.create_image(150,100,anchor=SW,image=Phototab)
            self.showtoy=canvas.create_image(482,75,anchor=SW,image=self.image[self.number])
        
    def move1(self):
      if self.point1<=41:
        for i in range(1,self.number1+1):
            self.point+=1
            Y1=0
            Y2=0
            if self.point<=6:#เเถว1
                for i in range(10):
                    if Y1>(-15):
                        canvas.move(self.walkking1,10,Y1)
                        tk.update()
                        time.sleep(0.05)
                        Y1+=-3
                    else:
                        canvas.move(self.walkking1,10,Y2)
                        tk.update()
                        time.sleep(0.05)
                        Y2+=3
                    self.x1+=10
            if 7<=self.point<=13 :#เเถว2
                if self.x1==750 and self.y1==670 :
                    for i in range(10):
                        canvas.move(self.walkking1,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y1-=10
                    
                    
                else:
                    for i in range(10):
                        if Y1>(-15):
                            canvas.move(self.walkking1,-10,Y1)
                            tk.update()
                            time.sleep(0.05)
                            Y1+=-3
                            
                        else:
                            canvas.move(self.walkking1,-10,Y2)
                            tk.update()
                            time.sleep(0.05)
                            Y2+=3
                        self.x1-=10
                    
            if 14<=self.point<=20 :#เเถว3
                if self.x1==150 and self.y1==660 :
                    for i in range(10):
                        canvas.move(self.walkking1,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y1-=10
                else:
                    for i in range(10):
                        if Y1>(-15):
                            canvas.move(self.walkking1,10,Y1)
                            tk.update()
                            time.sleep(0.05)
                            Y1+=-3
                            
                        else:
                            canvas.move(self.walkking1,10,Y2)
                            tk.update()
                            time.sleep(0.05)
                            Y2+=3
                        self.x1+=10
            if 21<=self.point<=27 :#เเถว4
                if self.x1==750 and self.y1==650 :
                    for i in range(10):
                        canvas.move(self.walkking1,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y1-=10
                else:
                    for i in range(10):
                        if Y1>(-15):
                            canvas.move(self.walkking1,-10,Y1)
                            tk.update()
                            time.sleep(0.05)
                            Y1+=-3
                            
                        else:
                            canvas.move(self.walkking1,-10,Y2)
                            tk.update()
                            time.sleep(0.05)
                            Y2+=3
                        self.x1-=10
            if 28<=self.point<=34 :#เเถว5
                if self.x1==150 and self.y1==640 :
                    for i in range(10):
                        canvas.move(self.walkking1,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y1-=10
                else:
                    for i in range(10):
                        if Y1>(-15):
                            canvas.move(self.walkking1,10,Y1)
                            tk.update()
                            time.sleep(0.05)
                            Y1+=-3
                            
                        else:
                            canvas.move(self.walkking1,10,Y2)
                            tk.update()
                            time.sleep(0.05)
                            Y2+=3
                        self.x1+=10
                    
            if 35<=self.point<=41 :#เเถว6
                if self.x1==750 and self.y1==630 :
                    for i in range(10):
                        canvas.move(self.walkking1,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y1-=10
                else:
                    
                        for i in range(10):
                            if Y1>(-15):
                                canvas.move(self.walkking1,-10,Y1)
                                tk.update()
                                time.sleep(0.05)
                                Y1+=-3
                            
                            else:
                                canvas.move(self.walkking1,-10,Y2)
                                tk.update()
                                time.sleep(0.05)
                                Y2+=3
                            self.x1-=10
            if self.point>=41:

                        play1win()
                        break
                        
        if  self.x1==450 and self.y1==670 :#ขึ้นบันได3
            for i in range(10):
                canvas.move(self.walkking1,-10,-10)
                tk.update()
                time.sleep(0.05)
            self.point+=8
            self.x1-=100
            self.y1-=10
        if self.x1==650 and self.y1==660:#ขึ้นบันได8
            for i in range(10):
                canvas.move(self.walkking1,0,-20)
                tk.update()
                time.sleep(0.05)
            self.point+=14
            self.y1-=20
        if self.x1==350 and self.y1==650: #ลงงู16
            for i in range(20):
                canvas.move(self.walkking1,-5,10)
                tk.update()
                time.sleep(0.05)
            self.point+=(-15)
            self.x1-=100
            self.y1+=20
        if self.x1==250 and self.y1==640: #ขึ้นบันได26
            for i in range(10):
                canvas.move(self.walkking1,10,-10)
                tk.update()
                time.sleep(0.05)
            self.point+=(4)
            self.x1+=100
            self.y1-=10
        if self.x1==450 and self.y1==630:#ลงงู31
            for i in range(30):
                canvas.move(self.walkking1,3,10)
                tk.update()
                time.sleep(0.05)
            self.point+=(-22)
            self.x1+=100
            self.y1+=30
        if  self.x1==550 and self.y1==630 :#ขึ้นบันได32
            for i in range(10):
                canvas.move(self.walkking1,-10,-10)
                tk.update()
                time.sleep(0.05)
            self.point+=6
            print(self.point)
            self.x1-=100
            self.y1-=10
        if self.x1==650 and self.y1==620:#ลงงู36
            for i in range(20):
                canvas.move(self.walkking1,5,10)
                tk.update()
                time.sleep(0.05)
            self.point+=(-15)
            self.x1+=100
            self.y1+=20
        if self.x1==250 and self.y1==620:#ลงงู40
            for i in range(30):
                canvas.move(self.walkking1,-3.2,10)
                tk.update()
                time.sleep(0.05)
            self.point+=(-26)
            self.x1-=100
            self.y1+=30
        createdicebutton()
    def move2(self):
      if self.point<=41:
        for i in range(1,self.number1+1):
            self.point1+=1
            Y11=0
            Y12=0
            if self.point1<=6:#เเถว1
                for i in range(10):
                    if Y11>(-15):
                        canvas.move(self.walkking2,10,Y11)
                        tk.update()
                        time.sleep(0.05)
                        Y11+=-3
                    else:
                        canvas.move(self.walkking2,10,Y12)
                        tk.update()
                        time.sleep(0.05)
                        Y12+=3
                    self.x2+=10
            if 7<=self.point1<=13 :#เเถว2
                if self.x2==760 and self.y2==680 :
                    for i in range(10):
                        canvas.move(self.walkking2,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y2-=10
                    
                    
                else:
                    for i in range(10):
                        if Y11>(-15):
                            canvas.move(self.walkking2,-10,Y11)
                            tk.update()
                            time.sleep(0.05)
                            Y11+=-3
                            
                        else:
                            canvas.move(self.walkking2,-10,Y12)
                            tk.update()
                            time.sleep(0.05)
                            Y12+=3
                        self.x2-=10
                    
            if 14<=self.point1<=20 :#เเถว3
                if self.x2==160 and self.y2==670 :
                    for i in range(10):
                        canvas.move(self.walkking2,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y2-=10
                else:
                    for i in range(10):
                        if Y11>(-15):
                            canvas.move(self.walkking2,10,Y11)
                            tk.update()
                            time.sleep(0.05)
                            Y11+=-3
                            
                        else:
                            canvas.move(self.walkking2,10,Y12)
                            tk.update()
                            time.sleep(0.05)
                            Y12+=3
                        self.x2+=10
            if 21<=self.point1<=27 :#เเถว4
                if self.x2==760 and self.y2==660 :
                    for i in range(10):
                        canvas.move(self.walkking2,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y2-=10
                else:
                    for i in range(10):
                        if Y11>(-15):
                            canvas.move(self.walkking2,-10,Y11)
                            tk.update()
                            time.sleep(0.05)
                            Y11+=-3
                            
                        else:
                            canvas.move(self.walkking2,-10,Y12)
                            tk.update()
                            time.sleep(0.05)
                            Y12+=3
                        self.x2-=10
            if 28<=self.point1<=34 :#เเถว5
                if self.x2==160 and self.y2==650 :
                    for i in range(10):
                        canvas.move(self.walkking2,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y2-=10
                else:
                    for i in range(10):
                        if Y11>(-15):
                            canvas.move(self.walkking2,10,Y11)
                            tk.update()
                            time.sleep(0.05)
                            Y11+=-3
                            
                        else:
                            canvas.move(self.walkking2,10,Y12)
                            tk.update()
                            time.sleep(0.05)
                            Y12+=3
                        self.x2+=10
                    
            if 35<=self.point1<=41 :#เเถว6
                if self.x2==760 and self.y2==640 :
                    for i in range(10):
                        canvas.move(self.walkking2,0,-10)
                        tk.update()
                        time.sleep(0.05)
                    self.y2-=10
                else:
                    
                        for i in range(10):
                            if Y11>(-15):
                                canvas.move(self.walkking2,-10,Y11)
                                tk.update()
                                time.sleep(0.05)
                                Y11+=-3
                            
                            else:
                                canvas.move(self.walkking2,-10,Y12)
                                tk.update()
                                time.sleep(0.05)
                                Y12+=3
                            self.x2-=10
            if self.point1>=41:
                        play2win()
                        break
                        
        if  self.x2==460 and self.y2==680 :#ขึ้นบันได3
            for i in range(10):
                canvas.move(self.walkking2,-10,-10)
                tk.update()
                time.sleep(0.05)
            self.point1+=8
            self.x2-=100
            self.y2-=10
        if self.x2==660 and self.y2==670:#ขึ้นบันได8
            for i in range(10):
                canvas.move(self.walkking2,0,-20)
                tk.update()
                time.sleep(0.05)
            self.point1+=14
            self.y2-=20
        if self.x2==360 and self.y2==660: #ลงงู16
            for i in range(20):
                canvas.move(self.walkking2,-5,10)
                tk.update()
                time.sleep(0.05)
            self.point1+=(-15)
            self.x2-=100
            self.y2+=20
        if self.x2==260 and self.y2==650: #ขึ้นบันได26
            for i in range(10):
                canvas.move(self.walkking2,10,-10)
                tk.update()
                time.sleep(0.05)
            self.point1+=(4)
            self.x2+=100
            self.y2-=10
        if self.x2==460 and self.y2==640:#ลงงู31
            for i in range(30):
                canvas.move(self.walkking2,3,10)
                tk.update()
                time.sleep(0.05)
            self.poin1t+=(-22)
            self.x2+=100
            self.y2+=30
        if  self.x2==560 and self.y2==640 :#ขึ้นบันได32
            for i in range(10):
                canvas.move(self.walkking2,-10,-10)
                tk.update()
                time.sleep(0.05)
            self.point1+=6
            
            self.x2-=100
            self.y2-=10
        if self.x2==660 and self.y2==630:#ลงงู36
            for i in range(20):
                canvas.move(self.walkking2,5,10)
                tk.update()
                time.sleep(0.05)
            self.point1+=(-15)
            self.x2+=100
            self.y2+=20
        if self.x2==260 and self.y2==630:#ลงงู40
            for i in range(30):
                canvas.move(self.walkking2,-3.2,10)
                tk.update()
                time.sleep(0.05)
            self.point1+=(-26)
            self.x2-=100
            self.y2+=30
        createdicebutton()
    def Play1(self):
        self.tab1=canvas.create_image(self.x1,100,anchor=SW,image=Phototab)
        walkking1=canvas.create_image(180,670,anchor=SW,image=Photowalk1)
        self.walkking1=walkking1
    def Play2(self):
        walkking2=canvas.create_image(160,680,anchor=SW,image=Photowalk2)
        self.walkking2=walkking2
    def create_photo(self):
        self.canvas.create_image(150,700,anchor=SW,image=Photogo)
        self.canvas.create_image(250,700,anchor=SW,image=Photo1)
        self.canvas.create_image(350,700,anchor=SW,image=Photo2)
        self.canvas.create_image(450,700,anchor=SW,image=Photo3)
        self.canvas.create_image(550,700,anchor=SW,image=Photo4)
        self.canvas.create_image(650,700,anchor=SW,image=Photo5)
        self.canvas.create_image(750,700,anchor=SW,image=Photo6)
        self.canvas.create_image(150,600,anchor=SW,image=Photo13)
        self.canvas.create_image(250,600,anchor=SW,image=Photo12)
        self.canvas.create_image(350,600,anchor=SW,image=Photo11)
        self.canvas.create_image(450,600,anchor=SW,image=Photo10)
        self.canvas.create_image(550,600,anchor=SW,image=Photo9)
        self.canvas.create_image(650,600,anchor=SW,image=Photo8)
        self.canvas.create_image(750,600,anchor=SW,image=Photo7)
        self.canvas.create_image(150,500,anchor=SW,image=Photo14)
        self.canvas.create_image(250,500,anchor=SW,image=Photo15)
        self.canvas.create_image(350,500,anchor=SW,image=Photo16)
        self.canvas.create_image(450,500,anchor=SW,image=Photo17)
        self.canvas.create_image(550,500,anchor=SW,image=Photo18)
        self.canvas.create_image(650,500,anchor=SW,image=Photo19)
        self.canvas.create_image(750,500,anchor=SW,image=Photo20)
        self.canvas.create_image(150,400,anchor=SW,image=Photo27)
        self.canvas.create_image(250,400,anchor=SW,image=Photo26)
        self.canvas.create_image(350,400,anchor=SW,image=Photo25)
        self.canvas.create_image(450,400,anchor=SW,image=Photo24)
        self.canvas.create_image(550,400,anchor=SW,image=Photo23)
        self.canvas.create_image(650,400,anchor=SW,image=Photo22)
        self.canvas.create_image(750,400,anchor=SW,image=Photo21)
        self.canvas.create_image(150,300,anchor=SW,image=Photo28)
        self.canvas.create_image(250,300,anchor=SW,image=Photo29)
        self.canvas.create_image(350,300,anchor=SW,image=Photo30)
        self.canvas.create_image(450,300,anchor=SW,image=Photo31)
        self.canvas.create_image(550,300,anchor=SW,image=Photo32)
        self.canvas.create_image(650,300,anchor=SW,image=Photo33)
        self.canvas.create_image(750,300,anchor=SW,image=Photo34)
        self.canvas.create_image(750,200,anchor=SW,image=Photo35)
        self.canvas.create_image(650,200,anchor=SW,image=Photo36)
        self.canvas.create_image(550,200,anchor=SW,image=Photo37)
        self.canvas.create_image(450,200,anchor=SW,image=Photo38)
        self.canvas.create_image(350,200,anchor=SW,image=Photo39)
        self.canvas.create_image(250,200,anchor=SW,image=Photo40)
        self.canvas.create_image(150,200,anchor=SW,image=Photowin)
        self.canvas.create_image(650,550,anchor=SW,image=Photoladder1)
        self.canvas.create_image(250,400,anchor=SW,image=Photoladder2)
        self.canvas.create_image(350,700,anchor=SW,image=Photoladder3)
        self.canvas.create_image(450,300,anchor=SW,image=Photoladder4)
        self.canvas.create_image(650,400,anchor=SW,image=Photosnake1)
        self.canvas.create_image(150,500,anchor=SW,image=Photosnake2)
        self.canvas.create_image(450,600,anchor=SW,image=Photosnake3)
        self.canvas.create_image(250,750,anchor=SW,image=Photosnake4)
def aexit():
    d=messagebox.askyesno(title='คำยืนยัน',message='คุณต้องการออกจากเกมส์หรือไม่')
    if d>0:
            tk.destroy()
def homepage():
        global home
        page_2.delete_btn()
        home=SnakeLadder(canvas)
        home.create_btn()
def homepage1():
    a=messagebox.askyesno(title='คำยืนยัน',message='คุณต้องการย้อนกลับหรือไม่')
    if a>0:
        global home
        page_2.delete_btn()
        home=SnakeLadder(canvas)
        home.create_btn()
        deletedice()
        
def Startgame():
    global page_2
    page_2=page2(canvas)
    page_2.create_btn()
    page_2.create_photo()
    home.delete_btn()
    page_2.Play1()
    page_2.Play2()
def Toy555():
    sound()
    global m
    m=m+1
    dicebutton.destroy()
    page_2.deletePhotab()
    if m%2 !=0:
            page_2.move1()
    else:
            page_2.move2()
def play1win():
    canvas.create_image(0,800,anchor=SW,image=Photo1win)
def play2win():
    canvas.create_image(0,800,anchor=SW,image=Photo2win)
def createdicebutton():
    
        global dicebutton
        dicebutton=Button(tk,image=dicephoto,command=Toy555)
        dicebutton.place(x=880,y=20)
        
def deletedice(): 
        print(1)
        dicebutton.destroy()
    
tk=Tk()
canvas=Canvas(tk,width=1000,height=800)
canvas.create_rectangle(0,0,1000,1000,fill='pink')
canvas.pack()

m=0
snack_id=PhotoImage(file='b1.png')
startbtnphoto=PhotoImage(file='startgame.png')
exitbtnphoto=PhotoImage(file='exit1.png')
howtoplay=PhotoImage(file='howtoplay1.png')
startedphoto=PhotoImage(file='dg.png')
backbutton=PhotoImage(file='back.png')
dicephoto=PhotoImage(file='dice.png')
Photogo=PhotoImage(file='go.png')
Photo1=PhotoImage(file='1.png')
Photo2=PhotoImage(file='2.png')
Photo3=PhotoImage(file='3.png')
Photo4=PhotoImage(file='4.png')
Photo5=PhotoImage(file='5.png')
Photo6=PhotoImage(file='6.png')
Photo7=PhotoImage(file='7.png')
Photo8=PhotoImage(file='8.png')
Photo9=PhotoImage(file='9.png')
Photo10=PhotoImage(file='10.png')
Photo11=PhotoImage(file='11.png')
Photo12=PhotoImage(file='12.png')
Photo13=PhotoImage(file='13.png')
Photo14=PhotoImage(file='14.png')
Photo15=PhotoImage(file='15.png')
Photo16=PhotoImage(file='16.png')
Photo17=PhotoImage(file='17.png')
Photo18=PhotoImage(file='18.png')
Photo19=PhotoImage(file='19.png')
Photo20=PhotoImage(file='20.png')
Photo21=PhotoImage(file='21.png')
Photo22=PhotoImage(file='22.png')
Photo23=PhotoImage(file='23.png')
Photo24=PhotoImage(file='24.png')
Photo25=PhotoImage(file='25.png')
Photo26=PhotoImage(file='26.png')
Photo27=PhotoImage(file='27.png')
Photo28=PhotoImage(file='28.png')
Photo29=PhotoImage(file='29.png')
Photo30=PhotoImage(file='30.png')
Photo31=PhotoImage(file='31.png')
Photo32=PhotoImage(file='32.png')
Photo33=PhotoImage(file='33.png')
Photo34=PhotoImage(file='34.png')
Photo35=PhotoImage(file='35.png')
Photo36=PhotoImage(file='36.png')
Photo37=PhotoImage(file='37.png')
Photo38=PhotoImage(file='38.png')
Photo39=PhotoImage(file='39.png')
Photo40=PhotoImage(file='40.png')
Photowin=PhotoImage(file='win.png')
Photoladder1=PhotoImage(file='ladder1.png')
Photoladder2=PhotoImage(file='ladder2.png')
Photoladder3=PhotoImage(file='ladder3.png')
Photoladder4=PhotoImage(file='ladder4.png')
Photosnake1=PhotoImage(file='snake1.png')
Photosnake2=PhotoImage(file='snake2.png')
Photosnake3=PhotoImage(file='snake3.png')
Photosnake4=PhotoImage(file='snake4.png')
Phototab=PhotoImage(file='tab.png')
Phototab1=PhotoImage(file='tab1.png')
Photowalk1=PhotoImage(file='walk1.png')
Photowalk2=PhotoImage(file='walk2.png')
Photoone=PhotoImage(file='toy1.png')
Phototwo=PhotoImage(file='toy2.png')
Photothree=PhotoImage(file='toy3.png')
Photofour=PhotoImage(file='toy4.png')
Photofive=PhotoImage(file='toy5.png')
Photosix=PhotoImage(file='toy6.png')
Photo1win=PhotoImage(file='play11win.png')
Photo2win=PhotoImage(file='play2win.png')
page_2=page2(canvas)
homepage()
while True:
    tk.update()

