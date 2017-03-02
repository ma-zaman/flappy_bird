from Tkinter import *
import pygame
import random
import tkMessageBox
pygame.mixer.init()

pygame.mixer.music.set_volume(0.3)

son1 = pygame.mixer.Sound("point.wav")
son1.set_volume(0.5)

son2 = pygame.mixer.Sound("flap.wav")
son2.set_volume(0.5)

son3 = pygame.mixer.Sound("crash.wav")
son3.set_volume(0.5)

def reset():
    global PosX,PosY,Posx,Posy,Pion,Wallup,Walldown,start,n,test,score,Label1,Posx1,speed,Up,Up1,Bec,Eye,Iris,test1,Aile,Line,Eyebr
    start.destroy()
    Up = 0
    Up1 = 0
    speed = 10
    score = 0
    n = 0
    test1 = 0
    PosX = 250
    PosY = 250

    Posx = 600
    Posy = random.randint(100,400)

    Posx1 = -100


    Label1 = Label(Mafenetre, text = 'Score : %s'%score)
    Label1.pack(in_=top,side = BOTTOM)

    Pion = Canevas.create_oval(PosX-25,PosY-25,PosX+25,PosY+25,width=2,outline='black',fill='firebrick')
    Aile = Canevas.create_rectangle(PosX-25,PosY+17.5,PosX,PosY+30,width=2,outline='black',fill='Brown')

    Bec = Canevas.create_rectangle(PosX+15,PosY,PosX+40,PosY+15,width=2,outline='black',fill='Gold')
    Line = Canevas.create_line(PosX+17.5,PosY+7.5,PosX+40,PosY+7.5,width=1,fill='black')

    Eyebr = Canevas.create_rectangle(PosX-22,PosY-18,PosX-3,PosY-25,width=2,outline='black',fill='Brown')
    Eye = Canevas.create_oval(PosX-20,PosY-15,PosX-5,PosY,outline='black',fill='white')
    Iris = Canevas.create_oval(PosX-15,PosY-10,PosX-5,PosY,outline='black',fill='black')

    Wallup = Canevas.create_rectangle(Posx-50,0,Posx+50,Posy-50,width=2,outline='black',fill='Saddle Brown')
    Walldown = Canevas.create_rectangle(Posx-50,Posy+50,Posx+50,490,width=2,outline='black',fill='Saddle Brown')

    if test == 0:
        main()
        test += 1

def GameOver():
    global n,Up,Up1
    Up = 0
    Up1 = 0
    n=1
    rep = tkMessageBox.askyesno('GAME OVER','Do you want to restart the game ?')
    if rep == True:
        if Posx1 > -100:
            Canevas.delete(Wallup1)
            Canevas.delete(Walldown1)
        Canevas.delete(Pion)
        Canevas.delete(Aile)
        Canevas.delete(Bec)
        Canevas.delete(Line)
        Canevas.delete(Eye)
        Canevas.delete(Eyebr)
        Canevas.delete(Iris)
        Canevas.delete(Wallup)
        Canevas.delete(Walldown)
        Label1.destroy()
        reset()

    else:
        Mafenetre.quit()

def Clic(event):
    global PosY,test1,Aile,son2
    PosY -= 25
    Canevas.coords(Pion,PosX-25,PosY-25,PosX+25,PosY+25)
    if test1 == 0:
        Canevas.delete(Aile)
        Aile = Canevas.create_rectangle(PosX-25,PosY+17.5,PosX,PosY+5,width=2,outline='black',fill='Indian Red')
        test1 = 1
    else:
        Canevas.delete(Aile)
        Aile = Canevas.create_rectangle(PosX-25,PosY+17.5,PosX,PosY+30,width=2,outline='black',fill='Brown')
        test1 = 0

    son2.play()

def Press(event):
    global Up,test,Up1
    Up = 5
    Up1 = 2
    up()
    son2.play()

def Press1(event):
    global Up,test,Up1
    Up = -5
    Up1 = 2
    up()

def Release(event):
    global Up,Up1
    Up = 0
    Up1 = 0

def up():
    global PosY,Up,Posx,Posx1,Up1,Aile,test1
    PosY -= Up
    Posx -= Up1
    Posx1 -= Up1
    if test1 == 0:
        Canevas.delete(Aile)
        Aile = Canevas.create_rectangle(PosX-25,PosY+17.5,PosX,PosY+5,width=2,outline='black',fill='Indian Red')
        test1 = 1
    else:
        Canevas.delete(Aile)
        Aile = Canevas.create_rectangle(PosX-25,PosY+17.5,PosX,PosY+30,width=2,outline='black',fill='Brown')
        test1 = 0
    Canevas.coords(Pion,PosX-25,PosY-25,PosX+25,PosY+25)
    if Up != 0:
        Mafenetre.after(15,up)

def wall():
    global Posx,Posy,Wallup,Walldown,Posx1,Posy1,Wallup1,Walldown1,Aile
    Posx1 = Posx
    Posy1 = Posy
    Wallup1 = Canevas.create_rectangle(Posx1-50,0,Posx1+50,Posy1-50,width=2,outline='black',fill='Saddle Brown')
    Walldown1 = Canevas.create_rectangle(Posx1-50,Posy1+50,Posx1+50,490,width=2,outline='black',fill='Saddle Brown')
    Canevas.delete(Wallup)
    Canevas.delete(Walldown)

    Posx = 600
    Posy = random.randint(100,400)
    Wallup = Canevas.create_rectangle(Posx-50,0,Posx+50,Posy-50,width=2,outline='black',fill='Saddle Brown')
    Walldown = Canevas.create_rectangle(Posx-50,Posy+50,Posx+50,490,width=2,outline='black',fill='Saddle Brown')

def main():
    global PosY,Posx,n,score,Label1,speed,Posx1,Posy1,Aile,Line
    PosY += 1
    Posx -= 1
    if PosY+25 >= 490:
        son3.play()
        GameOver()

    if (Posx+50 >= PosX+40 >= Posx-50) or (Posx+50 >= PosX-25 >= Posx-50):
        if (Posy+50 <= PosY+25 >= Posy-50) or (Posy+50 >= PosY-25 <= Posy-50):
            son3.play()
            GameOver()

    if Posx+50 <= PosX-25:
        score += 1
        son1.play()
        Label1.destroy()
        Label1 = Label(Mafenetre, text = 'Score : %s'%score)
        Label1.pack(in_=top,side = BOTTOM)
        wall()

    if n == 0:
        if Posx1 > -100:
            Posx1 -= 1
            Canevas.coords(Wallup1,Posx1-50,0,Posx1+50,Posy1-50)
            Canevas.coords(Walldown1,Posx1-50,Posy1+50,Posx1+50,490)
        if test1 == 0:
            Canevas.coords(Aile,PosX-25,PosY+17.5,PosX,PosY+30)
        else:
            Canevas.coords(Aile,PosX-25,PosY+17.5,PosX,PosY+5)
        Canevas.coords(Pion,PosX-25,PosY-25,PosX+25,PosY+25)
        Canevas.coords(Bec,PosX+15,PosY,PosX+40,PosY+15)
        Canevas.coords(Line,PosX+17.5,PosY+7.5,PosX+40,PosY+7.5)
        Canevas.coords(Eye,PosX-20,PosY-15,PosX-5,PosY)
        Canevas.coords(Eyebr,PosX-22,PosY-18,PosX-3,PosY-25)
        Canevas.coords(Iris,PosX-15,PosY-10,PosX-5,PosY)
        Canevas.coords(Wallup,Posx-50,0,Posx+50,Posy-50)
        Canevas.coords(Walldown,Posx-50,Posy+50,Posx+50,490)
        Mafenetre.after(15,main)

Mafenetre = Tk()
Mafenetre.title('Pion')

test = 0

Largeur = 500
Hauteur = 500
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg = 'Royal Blue')

top = Frame(Mafenetre)
top.pack(side=TOP)

Canevas.focus_set()

Canevas.create_rectangle(-10,510,510,490,outline='black',fill='Forest Green')

Canevas.bind('<Button-1>',Clic)
Canevas.bind('<Button-2>',Press1)
Canevas.bind('<ButtonRelease-2>',Release)
Canevas.bind('<Button-3>',Press)
Canevas.bind('<ButtonRelease-3>',Release)
Canevas.pack(padx =5, pady =5)

start = Button(Mafenetre, text ='START', command = reset)
start.pack(side=LEFT,padx=5,pady=5)
Button(Mafenetre, text ='Quitter', command = Mafenetre.quit).pack(side=RIGHT,padx=5,pady=5)

Mafenetre.mainloop()
