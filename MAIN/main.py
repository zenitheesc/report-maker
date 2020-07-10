from tkinter import *

from widgets import WindowConfig
from initialize import Initialize

def initialize(root):
    initializeFrame = Frame(root, bg="Black")
    gif = Initialize(initializeFrame, root)
    
    initializeFrame.pack(fill=BOTH)

if __name__ == "__main__":
    root = Tk()
    config = WindowConfig(root, 1000, 680)
    initialize(root)
    root.mainloop()