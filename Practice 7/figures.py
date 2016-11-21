from Tkinter import *
import math
import random

def Tree(w, x0, y0, l, an):
    ind = 1;    
    if (l > ind ):
        x1 = x0 - (l * math.cos(an / 57.29578))
        y1 = y0 - (l* math.sin(an / 57.29578))       
        w.create_line(x0, y0, x1, y1, fill = 'green')    
        Tree(w, x1, y1, l / 1.3, an - 57)
        Tree(w, x1, y1, l / 1.3, an + 57)
    return

def Sun(w, x0, y0, l, an):  
    if(l > 0):  
        coseno = math.cos(an / 57.29578)
        seno = math.sin(an/57.29578)
        x1 = x0 - (l * coseno)
        y1 = y0 - (l * seno)
        w.create_line(x0, y0, x1, y1, fill='#f39f18')    
        l -= 3
        an += 37
        Sun(w, x0, y0, l, an)
    return  

def Mountain(w, x0, y0, l, an, ind):
    X = [0, 0]
    if ind > 0:
        Straight(w, x0, y0, l, an, X)
        Mountain(w, X[0], X[1], l / 1.2, an + 6, ind - 1)
        Mountain(w, X[0], X[1], l / 1.55, an + 172, ind - 1)
        Mountain(w, X[0], X[1], l / 1.8, an + 186, ind - 1)

def Straight(w, x0, y0, l, an, X):
    X[0] = x0 - (l * math.cos(an / 57.29578))
    X[1] = y0 - (l * math.sin(an / 57.29578))
    w.create_line(x0, y0, X[0], X[1], fill = '#bfb552') 
 
    return

def Cloud(w, x0, y0, l, an, ind):  
    if (ind > 0):
        coseno = math.cos(an / 57.29578)
        seno = math.sin(an / 57.29578)
        x1 = x0- (l * coseno)
        y1 = y0 - (l * seno)        
        w.create_line(x0, y0, x1, y1, fill = '#3ed6ef')    
        Cloud(w, x0, y0, l / 1.25, an + 30, ind - 1)
        Cloud(w, x1, y1, l / 1.3, an + 50, ind - 1)
        Cloud(w, x1, y1, l / 1.4, an + 100, ind - 1)
    return   

master = Tk()

xmax=800
ymax=800

w = Canvas(master, width=xmax, height=ymax)
w.pack()

Mountain(w, 140,250,83,-31,11)
Mountain(w, 340,250,83,-31,11)
Mountain(w, 540,250,83,-31,11)
Mountain(w, 740,250,83,-31,11)

for i in xrange(100, 800, 100):
    Cloud(w, i, 100, 22, 150, 7)

for i in xrange(100, 800, 100):
    Cloud(w, i - 50, 150, 22, 150, 7)


Sun(w, 400, 50, 200, 25)

for y in xrange(400, 800, 40):
    for i in xrange(15):
        if (y / 40) % 2 == 0:
            Tree(w, 10 + i * 60, y, 10, 90)
        else:
            Tree(w, 10 + i * 60 - 30, y, 10, 90)

mainloop()