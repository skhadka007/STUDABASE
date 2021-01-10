from tkinter import *
import tkinter as tk
from tkinter import filedialog

import tkinterGrid

# Opens file opener dialog box
def getFilePath():
    # Sets variable name to chosen file
    tkinterGrid.root.filename = filedialog.askopenfilename(initialdir="~/DATA", title="Select a File", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    if tkinterGrid.root.filename is None: # When 'canceled' and no file opened
        return
    return(tkinterGrid.root.filename)