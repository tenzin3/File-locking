from tkinter import *
import portalocker
import os
import time
import sqlite3
from threading import *
from multiprocessing import Process


def convertTuple(tup):
    str =  ''.join(tup)
    return str

filepath_temp=""
flag=0

def Unlock():
    time.sleep(1)
    file = open(filepath_temp, 'r+')
    portalocker.unlock(file)
    #os.startfile(filepath_temp)
    time.sleep(1)




def Window():
   window=Tk()
   password=StringVar()
   def getValues():
       conn = sqlite3.connect('info.db')
       c = conn.cursor()
       global filepath_temp
       c.execute("SELECT File_password FROM data_base WHERE File_path=:first",{'first':filepath_temp})
       temp_password = convertTuple(c.fetchone())
       print(temp_password)
       print(password.get())
       if temp_password==password.get():
           window.destroy()
           Unlock()
           global flag
           flag=1


   window.geometry("250x100")
   Label(window,text="Enter password").grid(row=1,column=0)
   Entry(window,show="*",textvariable=password).grid(row=1,column=1)
   Button(window,text="Login",command=getValues).grid(row=2,column=1)
   window.mainloop()


def MainProgram():
    print("in the main program")
    conn = sqlite3.connect('info.db')
    c = conn.cursor()
    c.execute("SELECT File_path FROM data_base")
    temp = c.fetchall()

    while flag==0:
        for t in temp:
            str_t = convertTuple(t)
            Current_Time = time.time()
            Accessed_Time = os.path.getatime(str_t)
            if Current_Time == Accessed_Time:
                file = open(str_t, 'r+')
                portalocker.lock(file, portalocker.LOCK_EX)
                global filepath_temp
                filepath_temp=str_t
                print(filepath_temp)
                Window()

MainProgram()