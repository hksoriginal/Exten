import os
import time
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


class broom:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Extension Groom")
        self.root.iconbitmap('icon.ico')

        bg_frame = Frame(root, bg="#333333", width=200, height=100)
        bg_frame.pack()



        def get_info():
            
                target = path_entry.get()
                ext=ext_entry.get()
                del_file(target,ext)
            

        def del_file(target, ext):
            status_box.insert("1.0","Please Wait...\n\n")
            time.sleep(2)
            s=time.time()
            for x in os.listdir(target):
                if x.endswith(ext):
                    os.unlink(target + '\\' + x)
                    time.sleep(0.3)
                    status_box.insert("1.0",f"\nDeleted : {x}\n")
            e = time.time()
            status_box.insert("1.0",f"\nProcess finished in {e-s}s\n")
            messagebox.showinfo("Finished",f"Process completed in {e-s} seconds")



        path_label = Label(bg_frame, text='Folder Path',
                           fg="white", bg="#333333")
        path_label.grid(row=0, column=0, padx=4, pady=4, sticky=W)
        path_entry = ttk.Entry(bg_frame, width=150, font=("Comic Sans", 10))
        path_entry.grid(row=0, column=1, padx=4, pady=4, sticky=W)

        ext_label = Label(bg_frame, text='Extension', fg="white", bg="#333333")
        ext_label.grid(row=1, column=0, padx=4, pady=4, sticky=W)
        ext_entry = ttk.Entry(bg_frame, width=20, font=("Comic Sans", 10))
        ext_entry.grid(row=1, column=1, padx=4, pady=4, sticky=W)

        btn = Button(bg_frame, text='Clean', width=20, bg="#12B568", fg="white",
                     relief=RIDGE, font=("Comic Sans", 12, "bold"), cursor="hand2",command=get_info)
        btn.grid(row=2, column=1, padx=4, pady=4, sticky=W)

        status_box = Text(root, font=("Comic Sans", 10),state="normal", fg="white", bg="#333333")
        status_box.place(x=0, y=120, height=500, width=800)

    


if __name__ == '__main__':
    root = Tk()
    obj = broom(root)

    root.resizable(False, False)
    root.mainloop()
