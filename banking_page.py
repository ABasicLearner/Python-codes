
from tkinter import *
import os
from PIL import ImageTk, Image

#main screen
master = Tk()
master.title("State Bank of India")

#import image
img = Image.open("image.jpg")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#labels
Label(master, text = "Custom Banking Beta", font = ('Calibri, 15')).grid(row = 0, sticky = N, pady = 10)