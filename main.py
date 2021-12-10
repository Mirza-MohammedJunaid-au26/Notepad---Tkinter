from os import read
from tkinter import *
from tkinter.font import BOLD
from tkinter import filedialog 

class GUI:

    def __init__(self):
        
        # FRAME
        gui = Tk()

        gui.title("Notepad")

        gui.geometry("800x700")

        self.text = Text(gui,wrap=WORD,bg="#b8ffd5",font=("Ubuntu",14),pady=3,padx=3)
        self.text.pack(expand=TRUE,fill=BOTH)

        # Menu
        mymenu = Menu(gui,bg="#73ffb4",fg="black")
        File = Menu()
        Edit = Menu()

        File.add_command(label="New",accelerator="CTRL + N",command=self.new_file)
        File.add_command(label="Open File",accelerator="CTRL + O",command=self.open_file)
        File.add_command(label="Save",accelerator="CTRL + S",command=self.save_file)
        File.add_command(label="Save As",accelerator="CTRL + A",command=self.save_as)
        File.add_command(label="Print",accelerator="CTRL + P",command=self.print)
        
        Edit.add_command(label="Cut",accelerator="CTRL + X",command=self.cut)
        Edit.add_command(label="Copy",accelerator="CTRL + C",command=self.copy)
        Edit.add_command(label="Paste",accelerator="CTRL + v",command=self.paste)
       
        mymenu.add_cascade(label="File",menu=File,font=("Ubuntu",14,BOLD))
        mymenu.add_cascade(label="Edit",menu=Edit,font=("Ubuntu",14,BOLD))
        gui.config(menu = mymenu)

        # GUI Object
        gui.mainloop()


    # New File
    def new_file(self):
        self.text.delete(1.0,END)
    
    # Open File
    def open_file(self):
        file_name = filedialog.askopenfile(mode = "r")
        data = file_name.read()
        self.text.delete(1.0,END)
        self.text.insert(1.0,data)
    
    # Save File
    def save_file(self):
        default_name = "Untitled.txt"
        data = self.text.get(1.0,END)
        f = open(default_name,'w')
        f.write(data)
    
    # Save As
    def save_as(self):
        f = filedialog.asksaveasfile(mode = "w",defaultextension=".txt")
        data = self.text.get(1.0,END)
    
    # Print
    def print(self):
        data = self.text.get(1.0,END)
        print_gui = Tk()
        print_gui.title("Print")
        print_gui.geometry("1000x1000")
        print_gui_area = Text(print_gui,wrap=WORD,font=("Ubuntu",14),pady=70,padx=70)
        print_gui_area.pack(expand=TRUE,fill=BOTH)
        print_gui_area.insert(INSERT,data)
        
    # Copy
    def copy(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())

    # Paste
    def paste(self):
        self.text.insert(INSERT,self.text.clipboard_get())
    
    # cut
    def cut(self):
        self.copy()
        self.text.delete('sel.first','sel.last')

obj = GUI()