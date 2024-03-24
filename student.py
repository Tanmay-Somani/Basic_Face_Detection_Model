from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x710+0+0")
        self.root.title("Student")
        BgImg = Image.open(r"bg.jpg")
        BgImg = BgImg.resize((1530, 710), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(BgImg)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        title_label = Label(self.root, text="Student Database", font=("Times New Roman", 35, "bold"), bg="#ddddd6", fg="#fc7e3c")
        title_label.pack(pady=5)  

        # Creating a frame
        main_frame = Frame(self.root, bd=2, bg="#e8baa2")
        main_frame.place(x=45,y=80, width=1450, height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=5,bg="#e8baa1",fg="#0c82d2",relief=RIDGE,text="Student Details", font=("Times New Roman",16,"bold")) 
        Left_frame.place(x=10,y=10,width=700,height=580)

        #left front label frame

        #left front label frames
        lbl_name = LabelFrame(Left_frame,text="Course Details" ,bd=2,bg="#e8baa1",fg="#0c82d2",relief=RIDGE,font=("Times New Roman", 15, "bold"))
        lbl_name.place(x=10,y=10,width=670,height=90)

        lbl_name2 = LabelFrame(Left_frame, text="Student Details",bd=2,bg="#e8baa1",fg="#0c82d2", relief=RIDGE,font=("Times New Roman", 15, "bold"))
        lbl_name2.place(x=10,y=105,width=670,height=400)

        #label 1 name for department

        department_label = Label(lbl_name, text="Department", bg="#e8baa1", fg="#0c82d2", font=("Times New Roman", 15, "bold"))
        department_label.grid(row=0, column=0,padx=10,sticky=W)

        #combo box for course
        department_combo=ttk.Combobox(lbl_name, text="Department",width=17,height=4, font=("Times New Roman", 12, "bold"))
        department_combo['values']=("Select Department","MTech(2 year)","BSc(3 year)","Mtech (5 year)","Phd")
        department_combo.current(0)
        department_combo.grid(row=0, column=1,padx=10,pady=4,sticky=W) 

        #combo box for year
        year_combo=ttk.Combobox(lbl_name, text="Year",width=17,height=4, font=("Times New Roman", 12, "bold"))
        year_combo['values']=("Select Year","2021","2022","2023","2024","2025")
        year_combo.current(0)
        year_combo.grid(row=0, column=2,padx=10,pady=4,sticky=W) 

        #combo box for semester
        semester_combo=ttk.Combobox(lbl_name, text="Semester",width=17,height=4, font=("Times New Roman", 12, "bold"))
        semester_combo['values']=("Select Semester","1","2","3","4","5","6","7","8","9","10")
        semester_combo.current(0)
        semester_combo.grid(row=0, column=3,padx=10,pady=4,sticky=W) 

        #Student Info DataDB Form for course

        StudentID_label=Label(lbl_name2, text="Student ID", bg="#e8baa1", fg="#0c82bf", font=("Times New Roman", 15, "bold"))
        StudentID_label.grid(row=0, column=0,padx=10,pady=4,sticky=W)
        StudentID_label_entry=ttk.Entry(lbl_name2, text="Student ID", font=("Times New Roman", 15, "bold"), width=30)
        StudentID_label_entry.grid(row=0, column=2,padx=10,pady=4,sticky=W)

        #Student name DataDB Form for course

        Student_name=Label(lbl_name2, text="Student name", bg="#e8baa1", fg="#0c82bf", font=("Times New Roman", 15, "bold"))
        Student_name.grid(row=1, column=0,padx=10,pady=4,sticky=W)
        Student_name_entry=ttk.Entry(lbl_name2, text="Student name", font=("Times New Roman", 15, "bold"), width=30)
        Student_name_entry.grid(row=1, column=2,padx=10,pady=4,sticky=W)

        #Email DataDB Form for course

        Email=Label(lbl_name2, text="Email ID", bg="#e8baa1", fg="#0c82bf", font=("Times New Roman", 15, "bold"))
        Email.grid(row=2, column=0,padx=10,pady=4,sticky=W)
        Email_entry=ttk.Entry(lbl_name2, text="Email ID", font=("Times New Roman", 15, "bold"), width=30)
        Email_entry.grid(row=2, column=2,padx=10,pady=4,sticky=W)

        #Gender DataDB Form for course

        Gender=Label(lbl_name2, text="Gender", bg="#e8baa1", fg="#0c82bf", font=("Times New Roman", 15, "bold"))
        Gender.grid(row=3, column=0,padx=10,pady=4,sticky=W)
        Gender_entry=ttk.Entry(lbl_name2, text="Gender", font=("Times New Roman", 15, "bold"), width=30)
        Gender_entry.grid(row=3, column=2,padx=10,pady=4,sticky=W)

        #DOB Form for course

        DOB=Label(lbl_name2, text="DOB", bg="#e8baa1", fg="#0c82bf", font=("Times New Roman", 15, "bold"))
        DOB.grid(row=4, column=0,padx=10,pady=4,sticky=W)
        DOB_entry=ttk.Entry(lbl_name2, text="DOB", font=("Times New Roman", 15, "bold"), width=30)
        DOB_entry.grid(row=4, column=2,padx=10,pady=4,sticky=W)

        #Phone no. Form for course

        Phoneno=Label(lbl_name2, text="Phone no.", bg="#e8baa1", fg="#0c82bf", font=("Times New Roman", 15, "bold"))
        Phoneno.grid(row=5, column=0,padx=10,pady=4,sticky=W)
        Phoneno_entry=ttk.Entry(lbl_name2, text="Phone no.", font=("Times New Roman", 15, "bold"), width=30)
        Phoneno_entry.grid(row=5, column=2,padx=10,pady=4,sticky=W)

        #Address Form for course

        Address=Label(lbl_name2, text="Address", bg="#e8baa1", fg="#0c82bf", font=("Times New Roman", 15, "bold"))
        Address.grid(row=6, column=0,padx=10,pady=4,sticky=W)
        Address_entry=ttk.Entry(lbl_name2, text="Address", font=("Times New Roman", 15, "bold"), width=30)
        Address_entry.grid(row=6, column=2,padx=10,pady=4,sticky=W)

        #Radio button 1

        Radiobutton1=ttk.Radiobutton(lbl_name2, text="Take a Photo Sample",value="Yes")
        Radiobutton1.grid(row=7, column=1,padx=10,pady=4,sticky=W)

        Radiobutton2=ttk.Radiobutton(lbl_name2, text="No Photo Sample",value="No")
        Radiobutton2.grid(row=7, column=2,padx=10,pady=4,sticky=W)

        #frame of the button

        btnFrame=Frame(lbl_name2,bd=4,relief=RIDGE,bg="#e8baa2")
        btnFrame.place(x=50,y=296,width=566,height=70)

        #save the data button
        save_btn=Button(btnFrame,text="Save Data",width=10,fg="#e8baa1",bg="#0c82bf",font=("Times New Roman",14,"bold"))
        save_btn.grid(row=0,column=0,padx=10,pady=10)
        
        #update the data button
        update=Button(btnFrame,text="Update Data",width=10,fg="#e8baa1",bg="#0c82bf",font=("Times New Roman",14,"bold"))
        update.grid(row=0,column=1,padx=10,pady=10)

        #delete the data button
        delete_btn=Button(btnFrame,text="Delete Data",width=10,fg="#e8baa1",bg="#0c82bf",font=("Times New Roman",14,"bold"))
        delete_btn.grid(row=0,column=2,padx=10,pady=10)

        #reset the data button
        Reset_btn=Button(btnFrame,text="Reset",width=10,fg="#e8baa1",bg="#0c82bf",font=("Times New Roman",14,"bold"))
        Reset_btn.grid(row=0,column=3,padx=10,pady=10)

# 
        # 
        # 
        #Right label frame

        Right_frame=LabelFrame(main_frame,bd=5,bg="#e8baa1",fg="#0c82d2",relief=RIDGE,text="Student Details", font=("Times New Roman",16,"bold"))
        Right_frame.place(x=730,y=10,width=700,height=580)

        #search system in the right label frame

        lbl_name3 = LabelFrame(Right_frame,text="Search System" ,bd=2,bg="#e8baa1",fg="#0c82d2",relief=RIDGE,font=("Times New Roman", 15, "bold"))
        lbl_name3.place(x=10,y=10,width=670,height=80)

        Search_frame=Label(lbl_name3, text="Search By:", bg="#e8baa1", fg="#0c82bf", font=("Times New Roman", 15, "bold"))
        Search_frame.grid(row=0, column=0,padx=10,pady=4,sticky=W)

        Seach_combobox = ttk.Combobox(lbl_name3, values=['Select',"Name",'Roll_no',"Phone_No"],font=("times new roman",13,"bold"))
        Seach_combobox.grid(row=0, column=1, padx=10, pady=4, sticky=W)
        Seach_combobox.current(0)

        Space_srch=ttk.Entry(lbl_name3, text="Search", font=("Times New Roman", 12, "bold"), width=15)
        Space_srch.grid(row=0, column=2,padx=10,pady=4,sticky=W)

        Srch_btn=Button(lbl_name3,text="Search",width=6,fg="#e8baa1",bg="#0c82bf",font=("Times New Roman",12,"bold"))
        Srch_btn.grid(row=0,column=3,padx=10,pady=10)

        Showall_btn=Button(lbl_name3,text="Show all",width=6,fg="#e8baa1",bg="#0c82bf",font=("Times New Roman",12,"bold"))
        Showall_btn.grid(row=0,column=4,padx=10,pady=10)

        #table in the right label frame

        lbl_name4 = LabelFrame(Right_frame,text="Record Display" ,bd=2,bg="#e8baa1",fg="#0c82d2",relief=RIDGE,font=("Times New Roman", 15, "bold"))
        lbl_name4.place(x=10,y=90,width=670,height=415)

        scroll_x_lbl4=ttk.Scrollbar(lbl_name4,orient=HORIZONTAL)
        scroll_y_lbl4=ttk.Scrollbar(lbl_name4,orient=VERTICAL)

        self.student_Table = ttk.Treeview(lbl_name4,column=("id","name","email","gender","contact","dob","address","photo"),xscrollcommand=scroll_x_lbl4.set,yscrollcommand=scroll_y_lbl4.set)
        
        scroll_x_lbl4.pack(side=BOTTOM,fill=X)
        scroll_y_lbl4.pack(side=RIGHT,fill=Y)
        scroll_x_lbl4.config(command=self.student_Table.xview)
        scroll_y_lbl4.config(command=self.student_Table.yview)

        self.student_Table.heading("id",text="St_ID")
        self.student_Table.heading("name",text="Name")
        self.student_Table.heading("name",text="Name")
        self.student_Table.heading("email",text="Email")
        self.student_Table.heading("gender",text="Gender")
        self.student_Table.heading("contact",text="Contact")
        self.student_Table.heading("dob",text="DOB")
        self.student_Table.heading("address",text="Address")
        self.student_Table.heading("photo",text="Photo")

        self.student_Table.column("id",width=50)  # id is a short string
        self.student_Table.column("name",width=150)  # name can be longer
        self.student_Table.column("email",width=200)  # email can be longer
        self.student_Table.column("gender",width=50)  # gender is a short string
        self.student_Table.column("contact",width=70)  # contact is a number
        self.student_Table.column("dob",width=60)  # dob is a date
        self.student_Table.column("address",width=200)  # address can be longer
        self.student_Table.column("photo",width=50)  # photo is an image, we don't need to display it
        self.student_Table["show"]="headings"

        self.student_Table.pack(fill=BOTH,expand=1)
        



def see_docs(): # edit this for the documentation
    pass 

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    menubar = Menu(root)
    menu_f = Menu(menubar, title='File', tearoff=0) 
    menu_i = Menu(menubar, title="Interfaces", tearoff=0)
    menu_h = Menu(menubar, title="Help", tearoff=0)

    menubar.add_cascade(label="File", menu=menu_f)
    menu_f.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Help", menu=menu_h)
    menu_h.add_command(label="Docs", command=see_docs)
    menubar.add_cascade(label="Inferface",menu=menu_i)
    menu_i.add_command(label="Student Database")
    root.config(menu=menubar)
    root.mainloop()
