from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x960+0+0")
        self.root.title("Student")
        BgImg = Image.open(r"bg.jpg")
        BgImg = BgImg.resize((1530, 960), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(BgImg)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        title_label = Label(self.root, text="Student Database", font=("Times New Roman", 35, "bold"), bg="#ddddd6", fg="#fc7e3c")
        title_label.pack(pady=5)  


def see_docs(): # edit this for the documentation
            pass 

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    menubar = Menu(root)
    menu_f = Menu(menubar, title='File', tearoff=0) 
    menu_i=Menu(menubar, title="Interfaces", tearoff=0)
    menu_h = Menu(menubar, title="Help", tearoff=0)

    menubar.add_cascade(label="File", menu=menu_f)
    menu_f.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Help", menu=menu_h)
    menu_h.add_command(label="Docs", command=see_docs())
    root.config(menu=menubar)

    root.mainloop()