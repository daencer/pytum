import tkinter as tk
import random
from tkinter import messagebox

class PahTum():
    tiles_clicked = []
    tiles_undo = {}

    # Funtion to block a random number of tiles.
    def tiles_blocker(self,event):
        block_list = [5, 7, 9, 11, 13]
        amount = random.choice(block_list)
        print(event.widget)
        event.widget.config(state=tk.DISABLED)

    # Funtion to change color on click and only change it when its not already taken!
    def clicked(self, event):
        self.tiles_blocker(event)
        if event.widget not in self.tiles_clicked:
            if self.tic %2 == 0:
                self.tic += 1
                event.widget.config(bg="darkgreen")
                self.tiles_clicked.append(event.widget)
            else:
                self.tic += 1
                event.widget.config(bg="blue4")
                self.tiles_clicked.append(event.widget)
        else:
            messagebox.showinfo("ALERT!!!1!11","Tile already take!")
        print(self.tiles_clicked)

    def __init__(self,root,tic=0):
        self.root = root
        self.tic = tic
        self.root.title("Spiel:PavvgnTum")  # Title
        self.root['bg']="black"
        self.dic_canvas = {
              "11": "Canvas11", "12":"Canvas12", "13":"Canvas13", "14":"Canvas14", "15":"Canvas15", "16":"Canvas16", "17":"Canvas17"
            , "21": "Canvas21", "22":"Canvas22", "23":"Canvas23", "24":"Canvas24", "25":"Canvas25", "26":"Canvas26", "27":"Canvas27"
            , "31": "Canvas31", "32":"Canvas32", "33":"Canvas33", "34":"Canvas34", "35":"Canvas35", "36":"Canvas36", "37":"Canvas37"
            , "41": "Canvas41", "42":"Canvas42", "43":"Canvas43", "44":"Canvas44", "45":"Canvas45", "46":"Canvas46", "47":"Canvas47"
            , "51": "Canvas51", "52":"Canvas52", "53":"Canvas53", "54":"Canvas54", "55":"Canvas55", "56":"Canvas56", "57":"Canvas57"
            , "61": "Canvas61", "62":"Canvas62", "63":"Canvas63", "64":"Canvas64", "65":"Canvas65", "66":"Canvas66", "67":"Canvas67"
            , "71": "Canvas71", "72":"Canvas72", "73":"Canvas73", "74":"Canvas74", "75":"Canvas75", "76":"Canvas76", "77":"Canvas77"
        }

        #w = 600
        # h = 400
        # ws = root.winfo_screenwidth()
        # hs = root.winfo_screenheight()
        # x = (ws / 2) - (w / 2)
        # y = (hs / 2) - (h / 2)
        # root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        for i in range(1, 8):
            for j in range(1, 8):
                v = tk.IntVar()
                self.dic_ind = str(i)+str(j)
                self.name = tk.Canvas(root, width=50,height=50, bg="black",relief=tk.SUNKEN,bd=7)# Canvas size
                #self.name.create_rectangle(50,50,2,2, fill="green")
                self.name.bind("<Button>",self.clicked) # funtion that will be triggered by <Button>
                self.name.grid(row=i, column=j, ipadx=5, ipady=5)

    def undo(self):
        tiles_clicked[-1]
    def tiles_blocker(self,event):
        block_list = [5, 7, 9, 11, 13]
        amount = random.choice(block_list)
        print(event.widget)
