from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os


class Face_reco_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x960+0+0")
        self.root.title("Attendance System")

        # Load and resize the background image
        BgImg = Image.open(r"bg.jpg")
        BgImg = BgImg.resize((1530, 960), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(BgImg)
        
        # Display the background image
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, relwidth=1, relheight=1) 
        
        # Create title label
        title_label = Label(self.root, text="Attendance System 1.4", font=("Times New Roman", 35, "bold"), bg="#ddddd6", fg="#fc7e3c")
        title_label.pack(pady=5)  

        # Create Exit button
        button1 = Button(root, text="Student Database", cursor="hand2", command=see_docs())
        button1.place(x=200, y=300, width=220, height=140)
    
        button2 = Button(root, text="Face Detection", cursor="hand2", command=see_docs())
        button2.place(x=200, y=600, width=220, height=140)

        button3 = Button(root, text="Attendance", cursor="hand2", command=see_docs())
        button3.place(x=600, y=300, width=220, height=140)

        button4 = Button(root, text="Train Data", cursor="hand2",command=see_docs())
        button4.place(x=600, y=600, width=220, height=140)

        button5=Button(root, text="Photos", cursor="hand2",command=see_docs())
        button5.place(x=1000, y=300, width=220, height=140)

        button6 = Button(root, text="Exit", cursor="crosshair", command=root.quit)
        button6.place(x=1000, y=600, width=220, height=140)

def see_docs(): # edit this for the documentation
            pass 

if __name__ == "__main__":
    root = Tk()
    obj = Face_reco_system(root)
    # Menu bar
    menubar = Menu(root)
    menu_f = Menu(menubar, title='File', tearoff=0) 
    menu_i=Menu(menubar, title="Interfaces", tearoff=0)
    menu_h = Menu(menubar, title="Help", tearoff=0)

    menubar.add_cascade(label="File", menu=menu_f)
    menu_f.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Help", menu=menu_h)
    menu_h.add_command(label="Docs", command=see_docs())
    menubar.add_cascade(label="Inferface",menu=menu_i)
    menu_i.add_command(label="Student Database")
    root.config(menu=menubar)

    root.mainloop()
