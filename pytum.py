"""
PyTum Game
from EPR-Job No.5
"""
#import nadda
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"



from tkinter import *
import tkinter as Tkinter
root = Tk()
root.title('PAvvsH TUM')
w = 550
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def pressed(i):
    return i
    if start.zerozero.get() == 1:
        start.b.config(bg="red")
    elif zerozero.get() == 0:
        b.config(bg="lightgrey")
def start():
    but_list = []
    #win = Tkinter.Tk()
    dc_value = {}
    count1 = 1
    count2 = 1
    hure = 1
    for i in range(1,8):
        for j in range (1,8):
            #i = str(count1) + str(count2)
            b = Checkbutton(root, height=2, width=3, command=lambda i=str(count1)+str(count2):
            print(pressed(i))).grid(row=i,column=j)
            dc_value.update({str(count1) + str(count2):hure})
            hure += 1
            count2 += 1
            but_list.append(b)

        count2 = 1
        count1 += 1
    print(dc_value)
start()
mainloop()
