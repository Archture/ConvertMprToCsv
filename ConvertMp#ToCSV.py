# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:01:12 2020

@author: Zhijun ZHEN
"""

# To convert mp# file to numpy narray
import numpy as np
import os
from tkinter import *
import tkinter.filedialog

def Process():
    Path = tkinter.filedialog.askopenfilename(title = "Select mp# file", filetypes = (("mp# files", "*.mp#"),("All Files","*.*")))

    File = np.fromfile(Path)
    # Read header data
    with open(Path.rstrip('#') + 'r') as f:
        for line in f.readlines():
            if line[:5] == 'Size=':
                Size = line[5:].split(' ')
                Column = int(Size[1])
                Row = int(Size[0])
    
    File.shape = Row, Column
    np.savetxt(Path.rstrip('mp#') + 'csv', File, fmt="%.18f")
    if Path != '' and os.path.isfile(Path.rstrip('mp#') + 'csv'):
        lb.config(text = "Success, in the same folder please find the csv file with the same name, you can now close this windows or process another file.");
    else:
        lb.config(text = "Failture");                    
root = Tk()

lb = Label(root,text = 'Convert mp# file to csv file')
lb.pack()
btn = Button(root,text="Select MP# file",command=Process)
btn.pack()
root.mainloop()
# Read raw data
