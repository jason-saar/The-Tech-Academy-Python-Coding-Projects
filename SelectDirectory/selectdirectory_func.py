from tkinter import *
from tkinter import filedialog
import tkinter as tk


import selectdirectory_main
import selectdirectory_gui

def select_directory(self):
    var = filedialog.askdirectory()
    self.txt_directory.insert(0, var)


    
