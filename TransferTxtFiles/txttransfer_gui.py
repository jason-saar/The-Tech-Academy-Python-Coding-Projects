from tkinter import *
import tkinter as tk

import txttransfer_func

def load_gui(self):

    
    self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: txttransfer_func.select_source(self))
    self.btn_browse1.grid(row=0, column=0, padx=(18,0), pady=(45,0), sticky=N+W)
    self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: txttransfer_func.select_destination(self))
    self.btn_browse2.grid(row=1, column=0, padx=(18,0), pady=(12,0), sticky=N+W)
    self.btn_transfer = tk.Button(self.master, width=12, height=2, text='Transfer', command=lambda: txttransfer_func.transfer(self))
    self.btn_transfer.grid(row=2, column=0, padx=(18,0), pady=(12,0), sticky=N+W)
    
    self.txt_source = tk.Entry(self.master, text='')
    self.txt_source.grid(row=0, column=1, columnspan=4, padx=(30,18), pady=(45,0), sticky=NSEW)
    self.txt_destination = tk.Entry(self.master, text='')
    self.txt_destination.grid(row=1, column=1, columnspan=4, padx=(30,18), pady=(16,0), sticky=NSEW)
