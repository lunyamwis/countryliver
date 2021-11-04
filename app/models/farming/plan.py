
from pathlib import Path
import os,sys
import turtle
import tkinter as tk
# set directory
currentdir = Path('__file__').resolve().parent.parent.parent
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from graphics.shapes import draw_rectangle
from graphics.save_graphic import save_image
sys.path.pop(0)


root = tk.Tk()
canvas = tk.Canvas(root, width=2000, height=2000)
canvas.pack()
t = turtle.RawTurtle(canvas)
draw_rectangle(600,120)
save_image(root,"muthwani_farm","png")
from functools import reduce
reduce()