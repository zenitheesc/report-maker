from tkinter import *
from PIL import Image, ImageTk, ImageSequence

class Initialize:
    def __init__(self, master):

        # Window configuration ---------------------------------------------------------------------------------------------------
        self.zenith_logo_render = PhotoImage(file='c:/Users/Operador/Downloads/USP/ZENITH/REPORT MAKER/Códigos/IMAGES/LogoZ.png')

        self.master = master
        self.master.geometry("1000x680")
        self.master.title("Report Maker")
        self.master.iconphoto(False, self.zenith_logo_render)
        self.master.config(bg="black")
        # ------------------------------------------------------------------------------------------------------------------------

        self.canvas = Canvas(master, width=1000, height=680)
        self.canvas.config(bg="black")
        self.canvas.pack()
        
        # Create a sequence of frames in a list that corresponds to the gif
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(r'c:/Users/Operador/Downloads/USP/ZENITH/REPORT MAKER/Códigos/IMAGES/initialize.gif'))]
        self.image = self.canvas.create_image(500, 340, anchor=CENTER, image=self.sequence[0])

        self.animate(1)

    def animate(self, count):
        if count == 60:
            # Here comes the First Window 
            pass
        else:
            # Sequence of images
            self.canvas.itemconfig(self.image, image=self.sequence[count])
            self.master.after(20, lambda: self.animate((count+1) % len(self.sequence)))
        

if __name__ == "__main__":
    root = Tk()
    gif = Initialize(root)
    root.mainloop()
