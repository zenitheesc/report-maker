from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as tkFont

# Represents all the second window
class Window2:
    def __init__ (self, master):

        # Zenith's logo render
        self.zenith_logo_render = PhotoImage(file='c:/Users/Operador/Downloads/USP/ZENITH/REPORT MAKER/Códigos/IMAGES/LogoZ.png')
        self.zenith_label_render = PhotoImage(file='c:/Users/Operador/Downloads/USP/ZENITH/REPORT MAKER/Códigos/IMAGES/zenith-faixa.png')

        # Window's customize
        self.master = master
        self.master.geometry("1000x680")
        self.master.title("Report Maker")
        self.master.iconphoto(False, self.zenith_logo_render)
        self.master.config(bg="black")

        # Define text fontstyle
        fontStyle = tkFont.Font(
                        family="Helvetica", 
                        size=10, 
                        weight="bold")

        # All widgets definition
        ButtonFinish = Button(
                            self.master, 
                            text="Finish", 
                            bg="black", 
                            fg="white", 
                            width=7, 
                            padx=5, 
                            font=fontStyle,
                            command= self.PyLaTex_function)
        ZenithLabel = Label(self.master, 
                            image= self.zenith_label_render, 
                            highlightthickness=0, 
                            borderwidth=0)

        self.MainTitle = Title(master, fontStyle, "Título", 1)
        self.SectionName1 = Title(master, fontStyle, "Seção 1", 2)
        Conteiner1 = Frame(master)
        self.SectionText1 = TextConteiner(Conteiner1, master)

        self.SectionName2 = Title(master, fontStyle, "Seção 2", 4)
        Conteiner2 = Frame(master)
        self.SectionText2 = TextConteiner(Conteiner2, master)

        self.SectionName3 = Title(master, fontStyle, "Seção 3", 6)
        Conteiner3 = Frame(master)
        self.SectionText3 = TextConteiner(Conteiner3, master)

        ''' Sets a boolean variable to indicate the state of the CheckButton. From the beginning, the box is checked and val_checkbox returns 
        True. If the box is unchecked, val_checkbox returns False.'''

        self.val_checkbox = BooleanVar(value=True)
        self.CheckBox = Checkbutton( master, 
                                text="Inserir Imagens",
                                variable = self.val_checkbox,
                                font= fontStyle,
                                bg= "Black",
                                fg= "White",
                                selectcolor="Black")

        # Positioning all widgets in the master root
        ZenithLabel.grid(
                        row=0, 
                        column=0, 
                        columnspan=2, 
                        padx=0, 
                        pady=0)
        Conteiner1.grid(row=3,
                        column=1,
                        padx=10)
        Conteiner2.grid(row=5,
                        column=1)
        Conteiner3.grid(row=7,
                        column=1)
        ButtonFinish.grid(
                        row=8, 
                        column=1, 
                        sticky=E, 
                        padx=20,
                        pady=10)
        self.CheckBox.grid (row=8,
                            column=0,
                            padx=20)

    # Function to generates a LaTex file with the written text
    def PyLaTex_function (self):
        maintitle = self.MainTitle.get_title()
        section1_title = self.SectionName1.get_title()
        section2_title = self.SectionName2.get_title()
        section3_title = self.SectionName3.get_title()

        section1_text = self.SectionText1.get_text()
        section2_text = self.SectionText2.get_text()
        section3_text = self.SectionText3.get_text()
        

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
                                 width = 132)   

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
                        width=97, 
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

root = Tk()
window2 = Window2(root)
root.mainloop()