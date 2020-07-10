from tkinter import *
import tkinter.font as tkFont

from widgets import Title, TextConteiner, StandardButton, FontStyle

# Represents all the second window
class Window2:
    def __init__ (self, master, root):

        # Zenith's logo render
        self.zenith_label_render = PhotoImage(file='c:/Users/Operador/Downloads/USP/ZENITH/REPORT MAKER/Códigos/IMAGES/zenith-faixa.png')

        # Window's customize
        self.master = master
        self.root = root

        # All widgets definition
        ButtonFinish = StandardButton(frame=self.master, text="Finish", command= self.PyLaTex_function)
        ZenithLabel = Label(self.master, 
                            image= self.zenith_label_render, 
                            highlightthickness=0, 
                            borderwidth=0)

        self.MainTitle =    Title (master, "Título" , 1)
        self.SectionName1 = Title (master, "Seção 1", 2)
        Conteiner1 = Frame(master)
        self.SectionText1 = TextConteiner(Conteiner1, master)

        self.SectionName2 = Title (master, "Seção 2", 4)
        Conteiner2 = Frame(master)
        self.SectionText2 = TextConteiner(Conteiner2, master)

        self.SectionName3 = Title (master, "Seção 3", 6)
        Conteiner3 = Frame(master)
        self.SectionText3 = TextConteiner(Conteiner3, master)

        ''' Sets a boolean variable to indicate the state of the CheckButton. From the beginning, the box is checked and val_checkbox returns 
        True. If the box is unchecked, val_checkbox returns False.'''

        self.val_checkbox = BooleanVar(value=True)
        self.CheckBox = Checkbutton(master, 
                                    text="Inserir Imagens",
                                    variable = self.val_checkbox,
                                    font = FontStyle.get(),
                                    bg= "Black",
                                    fg= "White",
                                    selectcolor="Black")

        # Positioning all widgets in the master root
        ZenithLabel.grid   (row=0, column=0, columnspan=2, padx=0, pady=0)
        Conteiner1.grid    (row=3, column=1, padx=10)
        Conteiner2.grid    (row=5, column=1)
        Conteiner3.grid    (row=7, column=1)
        ButtonFinish.grid  (row=8, column=1, sticky=E, padx=20, pady=10)
        self.CheckBox.grid (row=8, column=0, padx=20)

    # Function to generates a LaTex file with the written text
    def PyLaTex_function (self):
        maintitle = self.MainTitle.get_title()
        section1_title = self.SectionName1.get_title()
        section2_title = self.SectionName2.get_title()
        section3_title = self.SectionName3.get_title()

        section1_text = self.SectionText1.get_text()
        section2_text = self.SectionText2.get_text()
        section3_text = self.SectionText3.get_text()


        self.root.destroy()
        