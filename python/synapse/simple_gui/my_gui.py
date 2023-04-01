import tkinter as tk
from circle import *

class myGui:
    def __init__(self, master):
        # passes tk.Tk() from main and creates master
        # creates title and size of window
        self.master = master

        # creates title and size of window
        self.master.title("simple GUI.")
        self.master.geometry("1600x900")

        self.canvas = tk.Canvas(self.master, width=1600, height=900, bg="beige")

        self.canvas.pack()

        # using Circle class, initialise new circle called 'c1'
        c1 = Circle(self.canvas, 800, 100, 5, "lightyellow")
        r1 = self.drawRect(780, 95, 10, 10, "red")
        
        c2 = Circle(self.canvas, 900, 300, 20, "lightblue")

        


        self.master.mainloop()

    def animate(self, shape):
        self.canvas.move(shape, 0, 100)
        
        
    def drawRect(self, x, y, width, height, colour):
        x1 = x
        y1 = y
        x2 = x + width
        y2 = y + height

        self.canvas.create_rectangle(x1, y1, x2, y2, fill=colour)
