from tkinter import *
import tkinter as tk

import selectdirectory_func

def load_gui(self):

    self.btn_printdirectory = tk.Button(self.master, width=12, height=2, text='Select Directory', command=lambda: selectdirectory_func.select_directory(self))
    self.btn_printdirectory.grid(row=0, column=0, padx=(18,0), pady=(18,0), sticky=N+W)
    self.txt_directory = tk.Entry(self.master, text='')
    self.txt_directory.grid(row=0, column=1, columnspan=2, padx=(20,18), pady=(22,0), sticky=NSEW)
