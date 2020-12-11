from PIL import Image
from tkinter import filedialog
import tkinter.messagebox




from tkinter import *


class Image_Size:
    def __init__(self,root):
        self.root=root
        self.root.title("Image resize")
        self.root.geometry("300x300")
        self.root.iconbitmap("logo478.ico")
        self.root.resizable(0,0)




        def Dimensions():
            try:
                from PIL import Image
            except ImportError as e:
                print(e)
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("png","*.png"),("jpg","*.jpg"),("all files","*.*")))
            if len(file_path)!=0:
                image=Image.open(file_path)
                width,height=image.size
                lab_width_answer.config(text=width)
                lab_height_answer.config(text=height)
            else:
                tkinter.messagebox.showerror("Error","No file is selected")


            





        def clear():
            lab_width_answer.config(text="")
            lab_height_answer.config(text="")



#=========================frame=======================#
        
        mainframe=Frame(self.root,width=300,height=300,relief="ridge",bd=3,bg="black")
        mainframe.place(x=0,y=0)

        but_browse=Button(mainframe,width=18,text="Browse",font=('times new roman',14),cursor="hand2",command=Dimensions)
        but_browse.place(x=50,y=10)

        but_clear=Button(mainframe,width=18,text="Clear",font=('times new roman',14),cursor="hand2",command=clear)
        but_clear.place(x=50,y=80)

        lab_width=Label(mainframe,text="width :",font=('times new roman',15),bg="black",fg="white")
        lab_width.place(x=70,y=150)

        lab_width_answer=Label(mainframe,text="",font=('times new roman',15),bg="black",fg="white")
        lab_width_answer.place(x=170,y=150)

        lab_height=Label(mainframe,text="height :",font=('times new roman',15),bg="black",fg="white")
        lab_height.place(x=70,y=200)

        lab_height_answer=Label(mainframe,text="",font=('times new roman',15),bg="black",fg="white")
        lab_height_answer.place(x=170,y=200)






if __name__ == "__main__":
    root=Tk()
    Image_Size(root)
    root.mainloop()