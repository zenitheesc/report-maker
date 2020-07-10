from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as tkFont

# CLASSES ----------------------------------------------------------------------------------------------------------

# Sets all Window configuration
class WindowConfig:
    def __init__(self, master, width, height):

        # Window configuration 
        self.zenith_logo_render = PhotoImage(file='c:/Users/Operador/Downloads/USP/ZENITH/REPORT MAKER/Códigos/IMAGES/LogoZ.png')

        self.master = master
        self.width = width
        self.height = height

        x, y = self.center(master)
        self.master.geometry(f"{self.width}x{self.height}" + f"+{x}+{y}")
        self.master.title("Report Maker")
        self.master.iconphoto(False, self.zenith_logo_render)
        self.master.config(bg="black")

    def center(self, master):
        master.update_idletasks()
        x = (master.winfo_screenwidth() // 2) - (self.width // 2)
        y = (master.winfo_screenheight() // 2) - (self.height // 2) - 30
        return x, y

# Define a button design
class StandardButton:
    def __init__ (self, frame, text, command):
        fontStyle = tkFont.Font(
                        family="Helvetica", 
                        size=10, 
                        weight="bold")

        self.standardButton = Button(frame, 
                                text=text, 
                                bg="black", 
                                fg="white", 
                                width=8, 
                                padx=5, 
                                font=fontStyle,
                                command= command)

    def grid (self, row, column, padx, pady, *args, **kwargs):
        sticky = kwargs.get('sticky', None)
        self.standardButton.grid (row=row, column=column, padx=padx, pady=pady, sticky=sticky)

# Sets the title's entry
class Title:
    def __init__ (self, master, fontStyle, name_title, row):
        self.master = master

        TitleLabel = Label( self.master,
                            text= name_title,
                            bg="black",
                            fg="white",
                            font=fontStyle)
        self.TitleEntry = Entry (self.master,
                                 width = 133)   

        TitleLabel.grid(row=row,
                        column=0,
                        padx=12)
        self.TitleEntry.grid(
                        row=row,
                        column=1,
                        pady=5)

    # Returns the content of the Entry
    def get_title (self):
        title = self.TitleEntry.get()
        return title

# Sets the Text Area to get the report content
class TextConteiner:

    # Configure the Text Area attached to its scrollbar
    def __init__ (self, conteiner, master):

        self.TextArea = Text(conteiner, 
                        width=98, 
                        height=8)
        ScrollBar = Scrollbar(
                        conteiner, 
                        orient=VERTICAL)

        ScrollBar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=ScrollBar.set)
        ScrolledText(master)

        ScrollBar.grid(
                    row=0, 
                    column=1, 
                    sticky=W)
        self.TextArea.grid(
                    row=0, 
                    column=0, 
                    sticky=E) 
    
    # Returns the content of the Text Area
    def get_text (self):
        text = self.TextArea.get("1.0", END)
        return text

# ------------------------------------------------------------------------------------------------------------------
# FUNCTIONS --------------------------------------------------------------------------------------------------------

def switch_frame(actualFrame, nextFrame):
    if actualFrame is not None:
        actualFrame.destroy()
    actualFrame = nextFrame
    actualFrame.pack (fill=BOTH)