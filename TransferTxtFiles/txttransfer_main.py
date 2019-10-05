# Python Ver:   3.7.4
#
# Author:       Jason Saar
#
# Purpose:      C
#
# Tested OS:    Windows 10

from tkinter import *
from tkinter import filedialog
import tkinter as tk

import txttransfer_gui
import txttransfer_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(600, 200)
        self.master.maxsize(600, 200)
        self.master.columnconfigure(1, weight=1)

        self.master.title("Text File Transfer")
        self.master.configure(bg="#F0F0F0")

        arg = self.master

        txttransfer_gui.load_gui(self)
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
