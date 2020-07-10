from tkinter import *
from PIL import Image, ImageTk, ImageSequence

from widgets import switch_frame
from widgets import WindowConfig
from window1 import Window1

class Initialize:
    def __init__(self, master, root):
        self.master = master
        self.root = root

        self.canvas = Canvas(master, width=1000, height=680)
        self.canvas.config(bg="black")
        self.canvas.pack()
        
        # Create a sequence of frames in a list that corresponds to the gif
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(r'c:/Users/Operador/Downloads/USP/ZENITH/REPORT MAKER/Códigos/IMAGES/initialize.gif'))]
        self.image = self.canvas.create_image (500, 340,anchor=CENTER, image=self.sequence[0])
        self.animate(1)

    def animate(self, count):
        if count == 70:
            self.initialize_to_window1()
        else:
            # Sequence of images
            self.canvas.itemconfig(self.image, image=self.sequence[count])
            self.master.after(20, lambda: self.animate((count+1) % len(self.sequence)))

    def initialize_to_window1(self):
        window1Frame = Frame(self.root, bg="Black")
        switch_frame(self.master, window1Frame)
        window1 = Window1(window1Frame, self.root)