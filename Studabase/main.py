# STUDABASE: The Student Database (Stoo-da-base)
# Santosh Khadka        skhadka.code@gmail.com
# Reynaldo Ferrari      reynaldoferrari@my.unt.edu
# Duncan Campbell       duncancampbell@my.unt.edu
# Gregory Tillotson     gregorytillotson@my.unt.edu
# 
# This is a GUI style student database organization software called STUDABASE. STUDABASE will allow users take data from a 
# csv file (or MySQL database) and translate it into a GUI system. This program will let users easily sort by fields such as student-ID, 
# first and last name, email, department, major, and expected graduation date. The user would also be able to search, 
# add/remove students, and restrict the displayed data through various filters.  
#
# Uses the Python programming language with MySQL as the database. Tkinter library used create the GUI system.

## GUI Tkinter grid file.
from tkinter import *
# pip install pillow (<- in terminal if not already installed)
from PIL import Image, ImageTk

import tkinterGrid # Where the GUI is setup


# Main function
def main():
    tkinterGrid.mainWindow()

# Call main function
main()
