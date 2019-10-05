from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3
import shutil
import os
import time


def select_source(self):
    var = filedialog.askdirectory()
    self.txt_source.insert(0, var)

def select_destination(self):
    var = filedialog.askdirectory()
    self.txt_destination.insert(0, var)

def create_db(self):
    conn = sqlite3.connect('db_textfiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_textfiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT, \
            col_lastmodified TEXT \
            );")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()    
    
def transfer(self):
    sDir = self.txt_source.get()
    dDir = self.txt_destination.get()
    dirs = os.listdir(sDir)

    create_db(self)
    for file in dirs:
        fName = file
        abPath = os.path.join(sDir, fName)
        if abPath.endswith('.txt'):
            mTime = os.path.getmtime(abPath)
            local_time = time.ctime(mTime)
            shutil.move(os.path.join(sDir,fName), os.path.join(dDir, fName))
            conn = sqlite3.connect('db_textfiles.db')
            with conn:
                cur = conn.cursor()
                cur.execute("""INSERT INTO tbl_textfiles (col_filename, col_lastmodified) VALUES (?, ?)""",(file, local_time))
            print(file, "Last modified:", local_time)
