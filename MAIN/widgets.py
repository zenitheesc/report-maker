from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.package import Package
import shutil
import datetime
import os
import re

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as tkFont

# CLASSES ----------------------------------------------------------------------------------------------------------

# Sets all Window configuration
class WindowConfig:
    def __init__(self, master, width, height):

        self.zenithLogoRender = PhotoImage (file=os.path.join(os.path.dirname(__file__), "DEPENDENCES/IMAGES/LogoZ.png"))

        self.master = master
        self.width = width
        self.height = height

        x, y = self.center(master)
        self.master.geometry(f"{self.width}x{self.height}" + f"+{x}+{y}")
        self.master.title("Report Maker")
        self.master.iconphoto(False, self.zenithLogoRender)
        self.master.config(bg="black")

    def center(self, master):
        master.update_idletasks()
        x = (master.winfo_screenwidth() // 2) - (self.width // 2)
        y = (master.winfo_screenheight() // 2) - (self.height // 2) - 30
        return x, y

# Define a button design
class StandardButton:
    def __init__ (self, frame, text, command):
        self.standardButton = Button(frame, 
                                text=text, 
                                bg="black", 
                                fg="white", 
                                width=8, 
                                padx=5, 
                                font=FontStyle.get(),
                                command= command)

    def grid (self, row, column, padx, pady, *args, **kwargs):
        sticky = kwargs.get('sticky', None)
        self.standardButton.grid (row=row, column=column, padx=padx, pady=pady, sticky=sticky)

# Sets the title's entry
class Title:
    def __init__ (self, master, name_title, row):
        self.master = master

        TitleLabel      = Label(self.master, text= name_title, bg="black", fg="white", font=FontStyle.get())
        self.TitleEntry = Entry (self.master, width = 133)   

        TitleLabel.grid      (row=row, column=0, padx=12)
        self.TitleEntry.grid (row=row, column=1, pady=5)

    # Returns the content of the Entry
    def get_title (self):
        title = self.TitleEntry.get()
        return title

# Sets the Text Area to get the report content
class TextConteiner:

    # Configure the Text Area attached to its scrollbar
    def __init__ (self, conteiner, master):

        self.TextArea = Text(conteiner, width=112, height=7, font="Calibri 11")
        ScrollBar     = Scrollbar(conteiner, orient=VERTICAL)

        ScrollBar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=ScrollBar.set)
        ScrolledText(master)

        ScrollBar.grid     (row=0, column=1, sticky=W)
        self.TextArea.grid (row=0, column=0, sticky=E) 
    
    # Returns the content of the Text Area
    def get_text (self):
        text = self.TextArea.get("1.0", END)
        return text

# Define a font pattern
class FontStyle:
    def __init__ (self):
        pass
    def get():
        return tkFont.Font(family="Helvetica", size=10, weight="bold")

# ------------------------------------------------------------------------------------------------------------------
# FUNCTIONS --------------------------------------------------------------------------------------------------------

def switch_frame(actualFrame, nextFrame):
    if actualFrame is not None:
        actualFrame.destroy()
    actualFrame = nextFrame
    actualFrame.pack (fill=BOTH)

def PyLaTex_generator(title, section1, section1Title, section2, section2Title, section3, section3Title, path, includeImages):

    now = datetime.datetime.now()

    filepath = (path + r"/OUTPUT")
    if (os.path.isdir(filepath) == False):
        os.makedirs(filepath)

    dependencesPath = (path + r"/DEPENDENCES")
    if (os.path.isdir(dependencesPath) == False):
            os.makedirs(dependencesPath)

    doc = Document(filepath)
    doc.documentclass = Command(
            'documentclass',
            options=['brazilian', '12pt', 'oneside', 'a4paper'],
            arguments=['article'],
        )

    doc.preamble.append(NoEscape(r'\input{DEPENDENCES/preamble.tex}'))
    doc.preamble.append(Command('titulo', {title}))
    doc.preamble.append(NoEscape(r'\data{\today}'))
    doc.append(NoEscape(r'\setFaixa'))
    doc.append(NoEscape(r'\geraTitulo'))
    doc.append(NoEscape(r'\section{'+ section1Title + '}'))
    doc.append(section1)
    doc.append(NoEscape(r'\section{'+ section2Title + '}'))
    doc.append(section2)
    doc.append(NoEscape(r'\section{'+ section3Title + '}'))
    doc.append(section3)
    if (includeImages == True):
        doc.append(NoEscape(r'\section{Dados}'))
        c = 1
        imageComand = ""

        imagesPath = path + r"/IMAGES"
        for image in os.listdir(imagesPath):
            if os.path.isfile(os.path.join(imagesPath, image)):
                splittedGraphName = re.split("_", image[:-4])
                caption = f"Gráfico {splittedGraphName[1]} versus {splittedGraphName[3]}"
                if c == 4:
                    imageComand = imageComand + r"    \subfloat[" + caption + r"]{\includegraphics[width = 1.5in]{" + r"IMAGES/" + image + r"}}\\" + "\n"
                    c = 1
                else: 
                    imageComand = imageComand + r"    \subfloat[" + caption + r"]{\includegraphics[width = 1.5in]{" + r"IMAGES/" + image + r"}} &" + "\n"
                    c = c + 1

        doc.append(NoEscape(r"""
    \begin{figure}[htb]
    \centering
        \begin{tabular}{cccc}
    """
        + "\n" + imageComand +
        r"""
        \end{tabular}
        \caption{Gráficos}    
    \end{figure}
        """))

    filename=(r"zenith_report_{dia}-{mes}-{ano}".format(dia=now.day, mes=now.month, ano=now.year))
    doc.generate_tex(r"{filepath}/{filename}".format(filepath=filepath, filename=filename))
    
    # Copying dependence files
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "DEPENDENCES/preamble.tex"), dependencesPath)
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "DEPENDENCES/IMAGES/LogoZ.png"), dependencesPath)
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "DEPENDENCES/IMAGES/zenith-faixa.png"), dependencesPath)

    #creating the zipfile
    make_archive(filename, path, path + "/" + filename + ".zip")

def make_archive(name, source, destination):
    base = os.path.basename(destination)
    format = base.split('.')[1]
    archiveFrom = os.path.dirname(source)
    archiveTo = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archiveFrom, archiveTo)
    shutil.move('%s.%s'%(name,format), destination)