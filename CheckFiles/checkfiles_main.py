# Python Ver:   3.7.4
#
# Author:       Jason Saar
#
# Purpose:      Check files GUI demo drill
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
from tkinter import messagebox
import tkinter as tk

import checkfiles_gui

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(550, 195)
        self.master.maxsize(550, 195)
        self.master.columnconfigure(1, weight=1)

        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        arg = self.master

        checkfiles_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
