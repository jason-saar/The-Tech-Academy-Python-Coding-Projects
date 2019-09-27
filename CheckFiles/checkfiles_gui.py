from tkinter import *
import tkinter as tk

def load_gui(self):

    
    self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...')
    self.btn_browse1.grid(row=0, column=0, padx=(18,0), pady=(45,0), sticky=N+W)
    self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...')
    self.btn_browse2.grid(row=1, column=0, padx=(18,0), pady=(12,0), sticky=N+W)
    self.btn_checkfiles = tk.Button(self.master, width=12, height=2, text='Check for files...')
    self.btn_checkfiles.grid(row=2, column=0, padx=(18,0), pady=(12,0), sticky=N+W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program')
    self.btn_close.grid(row=2, column=4, padx=(100,18), pady=(12,0), sticky=N+W)

    self.txt_textbox1 = tk.Entry(self.master, text='')
    self.txt_textbox1.grid(row=0, column=1, columnspan=4, padx=(30,18), pady=(45,0), sticky=NSEW)
    self.txt_textbox2 = tk.Entry(self.master, text='')
    self.txt_textbox2.grid(row=1, column=1, columnspan=4, padx=(30,18), pady=(16,0), sticky=NSEW)
                                    
