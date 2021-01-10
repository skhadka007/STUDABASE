# GUI Tkinter grid file.
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk # pip install pillow (<- in terminal if not already installed)

import tkinter as tk
import csv

# OTHER PYTHON FILES (OURS)
import menuFunctions
import openData
# import moreFunctions

import pyodbc
# pip install wheel, then pip install pandas
import pandas as pd

# Root needs to be created FIRST
root = tk.Tk()

searchText = "ERROR"

def filterOptions():
    global searchText
    
    # Label Frame
    filterOptionsFrame = tk.LabelFrame(root, text="Sort & Search", pady=5, padx=5)
    filterOptionsFrame.pack(side="top", padx=10, pady=10, fill="both", expand="no")
    # filterOptionsFrame.configure(bg="white")

    # Filter label and drop down menu
    # label
    filterLabel = tk.Label(filterOptionsFrame, text="Sort:")
    filterLabel.pack(side='left')
    # Option/Drop menu
    filters = [
        'Department',
        'GPA',
        'Graduation Year',
        'First Name Start',
        'Last Name Start'
    ]

    currentFilter = tk.StringVar()
    currentFilter.set(filters[0])

    filterMenu = tk.OptionMenu(filterOptionsFrame, currentFilter, *filters)
    filterMenu.pack(side='left', padx=5)
    filterMenu.config(bg="white", fg="black", width=17)  # filterMenu settings

    # Reset Filter button
    button_resetFilter = tk.Button(filterOptionsFrame, text="Reset Sort", bg="light sky blue")
    button_resetFilter.pack(side='left')
    
    # Search Text Box
    searchBox = Entry(filterOptionsFrame, borderwidth=2)   
    
    # Search entry box deletion
    def deleteSearch():
        searchBox.delete(0, END)
    
    # Clear Search Button
    button_clearSearch = tk.Button(filterOptionsFrame, text="CLEAR", bg="light sky blue", command=deleteSearch)
    button_clearSearch.pack(side='right', padx=2)
    # Search Button
    button_search = tk.Button(filterOptionsFrame, text="SEARCH", bg="khaki1", command=openResults)
    searchText = searchBox.get()
    button_search.pack(side='right', padx=2)
    # Search text box pack
    searchBox.pack(side='right', padx=5)
    
    # Search label
    searchLabel = tk.Label(filterOptionsFrame, text="Search:")
    searchLabel.pack(side='right')
    
#######################################################################################################
###############           DATA TABLE & RELATED FUNCTIONS        #######################################
#######################################################################################################
# Label Frame
dataTableFrame = tk.LabelFrame(root, text="Student Data", pady=2, padx=5, width=1300, height=1000)
    
dataScrollbarV = tk.Scrollbar(dataTableFrame, orient=VERTICAL)
dataScrollbarH = tk.Scrollbar(dataTableFrame, orient=HORIZONTAL)

dataListBox = Listbox(dataTableFrame, width=20, yscrollcommand=dataScrollbarV.set, selectmode=BROWSE, exportselection=0)
dataListBoxID = Listbox(dataTableFrame, width=3, yscrollcommand=dataScrollbarV.set, selectmode=BROWSE, exportselection=0)
dataListBoxEmail = Listbox(dataTableFrame, width=25, yscrollcommand=dataScrollbarV.set, selectmode=BROWSE, exportselection=0)
dataListBoxDepartment = Listbox(dataTableFrame, width=8, yscrollcommand=dataScrollbarV.set, selectmode=BROWSE, exportselection=0)
dataListBoxMajor = Listbox(dataTableFrame, width=15, yscrollcommand=dataScrollbarV.set, selectmode=BROWSE, exportselection=0)
dataListBoxDate = Listbox(dataTableFrame, width=8, yscrollcommand=dataScrollbarV.set, selectmode=BROWSE, exportselection=0)

def yview( *args):
    dataListBox.yview(*args)
    dataListBoxID.yview(*args)
    dataListBoxEmail.yview(*args)
    dataListBoxDepartment.yview(*args)
    dataListBoxMajor.yview(*args)
    dataListBoxDate.yview(*args)  
     
dataScrollbarV.config(command=yview)

  
#dataScrollbarV.config(command=lambda:[dataListBox.yview(), dataListBoxID.yview(), dataListBoxEmail.yview(), dataListBoxDepartment.yview(), dataListBoxMajor.yview(), dataListBoxDate.yview()])
#dataScrollbarH.config(command=dataListBox.xview)
#################################################################

## VARIABLES ##
filePathCurrent = ""
studentList = []

# Display listbox onto GUI
def dataTablePack():
    dataTableFrame.pack(anchor="n", padx=10, pady=1, fill="both", expand="yes")
    dataListBox.pack(side=LEFT, pady=10, fill="both", expand="yes")
    dataListBoxID.pack(side=LEFT, pady=10, fill="both", expand="yes")
    dataListBoxEmail.pack(side=LEFT, pady=10, fill="both", expand="yes")
    dataListBoxDepartment.pack(side=LEFT, pady=10, fill="both", expand="yes")
    dataListBoxMajor.pack(side=LEFT, pady=10, fill="both", expand="yes")
    dataListBoxDate.pack(side=LEFT, pady=10, fill="both", expand="yes")
    dataScrollbarV.pack(side=RIGHT, fill='y')

# Insert data from opened csv
def insertData():
    global filePathCurrent
    global studentList
    deleteAll()
    # Just so name is easier to use
    filePath = openData.getFilePath()
    filePathCurrent = filePath
    # Opens chosen file
    File = open(filePath)
    Reader = csv.reader(File)
    Data = list(Reader)
    # Removes first line of file - Row filled with the Column titles
    del(Data[0])
    
    for x in list(range(0, len(Data))):
        studentList.append(Data[x])
        #dataListBox.insert(END, Data[x])
        name = studentList[x][1] + ", " + studentList[x][0]
        #formattedText = ('{:<20}{:>15}{:>50}'.format(name, studentList[x][2], studentList[x][4]))
        #formattedText = (name + " " + studentList[x][2] + " " + studentList[x][3] + " " + studentList[x][4] + " " + studentList[x][5] + " " + studentList[x][6])
        dataListBox.insert(END, (name))
        dataListBoxID.insert(END, (studentList[x][2]))  
        dataListBoxEmail.insert(END, (studentList[x][3]))
        dataListBoxDepartment.insert(END, (studentList[x][4]))
        dataListBoxMajor.insert(END, (studentList[x][5]))
        dataListBoxDate.insert(END, (studentList[x][6]))

# For refreshing current open file    
def insertDataRefresh():
    global filePathCurrent
    global studentList
    deleteAll()
    # Opens chosen file
    File = open(filePathCurrent)
    Reader = csv.reader(File)
    Data = list(Reader)
    del(Data[0])    

    for x in list(range(0, len(Data))):
        studentList.append(Data[x])
        name = studentList[x][1] + ", " + studentList[x][0]        
        dataListBox.insert(END, (name))
        dataListBoxID.insert(END, (studentList[x][2]))  
        dataListBoxEmail.insert(END, (studentList[x][3]))
        dataListBoxDepartment.insert(END, (studentList[x][4]))
        dataListBoxMajor.insert(END, (studentList[x][5]))
        dataListBoxDate.insert(END, (studentList[x][6])) 
        

## CREEATES DATATABLE AFTER PICKING FILE
def dataTable():
    dataTablePack()
    insertData()

# Deletes ONE student      
def deleteOne():
    global studentList
    index = dataListBox.curselection()[0] 
    del studentList[index]
    dataListBox.delete(index) # ANCHOR
    dataListBoxID.delete(index)
    dataListBoxEmail.delete(index)
    dataListBoxDepartment.delete(index)
    dataListBoxMajor.delete(index)
    dataListBoxDate.delete(index)
    dataListBox.config(text='')

    
# Clears Table    
def deleteAll():
    dataListBox.delete(0, END)
    dataListBoxID.delete(0, END)
    dataListBoxEmail.delete(0, END)
    dataListBoxDepartment.delete(0, END)
    dataListBoxMajor.delete(0, END)
    dataListBoxDate.delete(0, END)
 
def select():
    dataListBox.config(text=dataListBox.get(ANCHOR))
    
def saveFile():
    global studentList
    csvWrite = filedialog.asksaveasfile(mode='w', defaultextension=".csv", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    if csvWrite is None: # When 'canceled' and no file saved
        return
#    with open(csvWrite, "wb") as f:
#        writer = csv.writer(f)
#        writer.writerows(a)
    text2save = str(dataListBox.get(0, END)) # starts from `1.0`, not `0.0`
    csvWrite.write(text2save)
    csvWrite.close()

def refreshTable():
    deleteAll()
    insertDataRefresh()
    
def updateStudent():
    global studentList
    '''
    First_Name
    Last_Name
    Student_ID
    Email
    Department
    Major
    Grad_Date
    '''
    # Gets location of current selection
    index = dataListBox.curselection()[0] 
    
    newWindow = Toplevel(root)
    newWindow.title("Update Student")
    newWindow.geometry("315x230")
    newWindow.iconbitmap('hat.ico')
    newWindow.resizable(width=False, height=False)     # Window size changeability

    #Create Text Boxes
    First_Name = Entry(newWindow, width = 30)
    First_Name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
    First_Name.insert(0, studentList[index][0])

    Last_Name = Entry(newWindow, width = 30)
    Last_Name.grid(row = 1, column = 1, padx = 20)
    Last_Name.insert(0, studentList[index][1])

    Student_ID = Entry(newWindow, width = 30)
    Student_ID.grid(row = 2, column = 1, padx = 20)
    Student_ID.insert(0, studentList[index][2])
    
    Email = Entry(newWindow, width = 30)
    Email.grid(row = 3, column = 1, padx = 20)
    Email.insert(0, studentList[index][3])
    
    Department = Entry(newWindow, width = 30)
    Department.grid(row = 4, column = 1, padx = 20)
    Department.insert(0, studentList[index][4])

    Major = Entry(newWindow, width = 30)
    Major.grid(row = 5, column = 1, padx = 20)
    Major.insert(0, studentList[index][5])

    Grad_Date = Entry(newWindow, width = 30)
    Grad_Date.grid(row = 6, column = 1, padx = 20)
    Grad_Date.insert(0, studentList[index][6])
    
    #Create Text Box Labels
    First_Name_Label = Label(newWindow, text = 'First Name')
    First_Name_Label.grid(row = 0, column = 0, pady = (10, 0))

    Last_Name_Label = Label(newWindow, text = 'Last Name')
    Last_Name_Label.grid(row = 1, column = 0)

    Student_ID_Label = Label(newWindow, text = 'Student ID')
    Student_ID_Label.grid(row = 2, column = 0)

    Email_Label = Label(newWindow, text = 'Email')
    Email_Label.grid(row = 3, column = 0)

    Department_Label = Label(newWindow, text = 'Department')
    Department_Label.grid(row = 4, column = 0)

    Major_Label = Label(newWindow, text = 'Major')
    Major_Label.grid(row = 5, column = 0)

    Grad_Date_Label = Label(newWindow, text = 'Grad Date')
    Grad_Date_Label.grid(row = 6, column = 0)
    
    goodUpdate_Label = Label(newWindow, text="* * *")
    goodUpdate_Label.grid(row = 8, columnspan=2)

    def retrieve_input(entryBox):
        input = entryBox.get()
        return input
    
    def goodUpdate():
        ## Update student
        # Get entered text
        studentList[index][0] = retrieve_input(First_Name)
        studentList[index][1] = retrieve_input(Last_Name)
        studentList[index][2] = retrieve_input(Student_ID)
        studentList[index][3] = retrieve_input(Email)
        studentList[index][4] = retrieve_input(Department)
        studentList[index][5] = retrieve_input(Major)
        studentList[index][6] = retrieve_input(Grad_Date) 
        name = studentList[index][1] + ", " + studentList[index][0]        
        
        dataListBox.insert(END, (name))
        dataListBoxID.insert(END, (studentList[index][2]))  
        dataListBoxEmail.insert(END, (studentList[index][3]))
        dataListBoxDepartment.insert(END, (studentList[index][4]))
        dataListBoxMajor.insert(END, (studentList[index][5]))
        dataListBoxDate.insert(END, (studentList[index][6])) 
        #name = studentList[index][1] + ", " + studentList[index][0]        
        #dataListBox.insert(END, Data[x])
        
        #formattedText = str(name + " " + studentList[index][2] + " " + studentList[index][3] + " " + studentList[index][4] + " " + studentList[index][5] + " " + studentList[index][6])  
        #dataListBox.insert(index, (formattedText))
        
        insertDataRefresh()
        goodUpdate_Label.config(text="Successfull Update!")
    
    #Create Update Button
    Update_button = Button(newWindow, text = 'Update Student', bg="goldenrod1", command=goodUpdate)
    Update_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
    

  # print(index)
    return None

        
def openResults():
    global studentList
    global searchText
    
    newWindow = Toplevel(root)
    newWindow.title("Search Results")
    newWindow.geometry("315x170")
    newWindow.iconbitmap('hat.ico')
    newWindow.resizable(width=False, height=False)     # Window size changeability

    #Create Text Boxes
    First_Name = Entry(newWindow, width = 30)
    First_Name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
    #First_Name.insert(0, studentList[x][0])

    Last_Name = Entry(newWindow, width = 30)
    Last_Name.grid(row = 1, column = 1, padx = 20)
    #Last_Name.insert(0, studentList[x][1])
    
    Student_ID = Entry(newWindow, width = 30)
    Student_ID.grid(row = 2, column = 1, padx = 20)
    #Student_ID.insert(0, studentList[x][2])
    
    Email = Entry(newWindow, width = 30)
    Email.grid(row = 3, column = 1, padx = 20)
    #Email.insert(0, studentList[x][3])
    
    Department = Entry(newWindow, width = 30)
    Department.grid(row = 4, column = 1, padx = 20)
    #Department.insert(0, studentList[x][4])
    
    Major = Entry(newWindow, width = 30)
    Major.grid(row = 5, column = 1, padx = 20)
    #Major.insert(0, studentList[x][5])
    
    Grad_Date = Entry(newWindow, width = 30)
    Grad_Date.grid(row = 6, column = 1, padx = 20)
    #Grad_Date.insert(0, studentList[x][6])
           
    #Create Text Box Labels
    First_Name_Label = Label(newWindow, text = 'First Name')
    First_Name_Label.grid(row = 0, column = 0, pady = (10, 0))
    
    Last_Name_Label = Label(newWindow, text = 'Last Name')
    Last_Name_Label.grid(row = 1, column = 0)
    
    Student_ID_Label = Label(newWindow, text = 'Student ID')
    Student_ID_Label.grid(row = 2, column = 0)
    
    Email_Label = Label(newWindow, text = 'Email')
    Email_Label.grid(row = 3, column = 0)
    
    Department_Label = Label(newWindow, text = 'Department')
    Department_Label.grid(row = 4, column = 0)

    Major_Label = Label(newWindow, text = 'Major')
    Major_Label.grid(row = 5, column = 0)

    Grad_Date_Label = Label(newWindow, text = 'Grad Date')
    Grad_Date_Label.grid(row = 6, column = 0)
    #index = dataListBox.get(0, END).index(searchText)
    #print(index)
    
    #if (index == "ERROR"):
    #    filterOptions().searchBox.insert(0, "STRING NOT FOUND")
    
    # Gets location of current selection
    #index = dataListBox.curselection()[0] 
    


    

def addStudent():
    global studentList
    '''
    First_Name
    Last_Name
    Student_ID
    Email
    Department
    Major
    Grad_Date
    '''

    newWindow = Toplevel(root)
    newWindow.title("Add Student")
    newWindow.geometry("365x230")
    newWindow.iconbitmap('hat.ico')
    newWindow.resizable(width=False, height=False)     # Window size changeability

    #Create Text Boxes
    First_Name = Entry(newWindow, width = 30)
    First_Name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
    First_Name.insert(0, "FIRSTNAME")

    Last_Name = Entry(newWindow, width = 30)
    Last_Name.grid(row = 1, column = 1, padx = 20)
    Last_Name.insert(0, "LASTNAME")

    Student_ID = Entry(newWindow, width = 30)
    Student_ID.grid(row = 2, column = 1, padx = 20)
    Student_ID.insert(0, "#####")

    Email = Entry(newWindow, width = 30)
    Email.grid(row = 3, column = 1, padx = 20)
    Email.insert(0, "example@school.edu")

    Department = Entry(newWindow, width = 30)
    Department.grid(row = 4, column = 1, padx = 20)
    Department.insert(0, "Business")

    Major = Entry(newWindow, width = 30)
    Major.grid(row = 5, column = 1, padx = 20)
    Major.insert(0, "Finance")

    Grad_Date = Entry(newWindow, width = 30)
    Grad_Date.grid(row = 6, column = 1, padx = 20)
    Grad_Date.insert(0, "##/##/20##")

    #Create Text Box Labels
    First_Name_Label = Label(newWindow, text = 'First Name')
    First_Name_Label.grid(row = 0, column = 0, pady = (10, 0))

    Last_Name_Label = Label(newWindow, text = 'Last Name')
    Last_Name_Label.grid(row = 1, column = 0)

    Student_ID_Label = Label(newWindow, text = 'Student ID')
    Student_ID_Label.grid(row = 2, column = 0)

    Email_Label = Label(newWindow, text = 'Email')
    Email_Label.grid(row = 3, column = 0)

    Department_Label = Label(newWindow, text = 'Department')
    Department_Label.grid(row = 4, column = 0)

    Major_Label = Label(newWindow, text = 'Major')
    Major_Label.grid(row = 5, column = 0)

    Grad_Date_Label = Label(newWindow, text = 'Grad Date')
    Grad_Date_Label.grid(row = 6, column = 0)

    goodAdd_Label = Label(newWindow, text="* * *")
    goodAdd_Label.grid(row = 8, columnspan=2)
    
    def retrieve_input(entryBox):
        input = entryBox.get()
        return input
    
    # Button disables after a successfull addition
    def goodAdd():
        global filePathCurrent
        global studentList

        ## Add student
        # Get entered text
        firstName = retrieve_input(First_Name)
        lastName = retrieve_input(Last_Name)
        studentid = retrieve_input(Student_ID)
        email_ = retrieve_input(Email)
        department_ = retrieve_input(Department)
        major_ = retrieve_input(Major)
        gradDate = retrieve_input(Grad_Date) 
        
        # Store into the table
        gatheredText = [firstName, lastName, studentid, email_, department_, major_, gradDate]
        studentList.append(gatheredText)
        
        name = lastName + ", " + firstName
        
        dataListBox.insert(END, (name))
        dataListBoxID.insert(END, (studentid))  
        dataListBoxEmail.insert(END, (email_))
        dataListBoxDepartment.insert(END, (department_))
        dataListBoxMajor.insert(END, (major_))
        dataListBoxDate.insert(END, (gradDate))         
#        formattedText = (lastName + ", " + firstName + " " + studentid + " " + email_ + " " + department_ + " " + major_ + " " + gradDate) 
#        dataListBox.insert(END, (formattedText))
          
        # Confirmation & disbale button
        goodAdd_Label.config(text="Successfull Add!")
        Add_button.config(state=DISABLED)     

    # Create Add Button
    Add_button = Button(newWindow, text = 'Add Student to Database', bg="SeaGreen1", command=goodAdd)
    Add_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
    
  # print(index)
    return None    
    
"""
    # for r in range (rows):
    #     for c in range (cols):
    canvas = tk.Canvas(dataTableFrame, bg="white", width=700, height=500)
    canvas.pack(fill="both", expand="yes")
    
    canvas2 = tk.Canvas(canvas, width=700, height=500)
    canvas2.pack(side="left")
    
    labelData = tk.Label(canvas2, text=(df.to_string()), bg="white")
    labelData.grid(row=rows, column=cols) 
    scrollbar = tk.Scrollbar(canvas, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
"""
#######################################################################################################
#######################################################################################################

def bottomButtons():
    # Label Frame
    bottomButtonsFrame = tk.LabelFrame(
        root, text="Database Options", pady=5, padx=5)
    bottomButtonsFrame.pack(side="bottom", padx=10, pady=10, fill="x", expand="no")

    # Buttons
    button_refresh = tk.Button(bottomButtonsFrame, text="Refresh Table", bg="light sky blue", command=refreshTable)
    button_refresh.pack(side='left', padx=5)

    button_save = tk.Button(bottomButtonsFrame, text="Save Current Database", bg="pale green", command=saveFile)
    button_save.pack(side='left', padx=5)
    
    #button_emailStudent = tk.Button(bottomButtonsFrame, text="Email Student(s)", bg="CadetBlue1")
    #button_emailStudent.pack(side='left', padx=5)

    button_add = tk.Button(bottomButtonsFrame, text="Add Student", bg="SeaGreen1", command=addStudent)
    button_add.pack(side='right', padx=5)

    button_update = tk.Button(bottomButtonsFrame, text="Update Student", bg="goldenrod1", command=updateStudent)  # DarkSeaGreen1
    button_update.pack(side='right', padx=5)

    button_delete = tk.Button(bottomButtonsFrame, text="Delete Student", bg="IndianRed1", command=deleteOne)
    button_delete.pack(side='right', padx=5)

    button_clearTable = tk.Button(bottomButtonsFrame, text="CLEAR Table", bg="yellow2", command=deleteAll)
    button_clearTable.pack(side='right', padx=5)

def userGuide():
    newWindow = Toplevel(root)
    newWindow.title("About Studabase")
    newWindow.geometry("500x500")
    newWindow.iconbitmap('hat.ico')
    newWindow.resizable(width=True, height=True)     # Window size changeability
    
    about_Label = Label(newWindow, text = "STUDABASE (stoo-da-base) is a GUI style student database organizational software that allows its users to:" + '\n' + "Take data from a MySQL database and translate it to a GUI system." + '\n' + "Sort data by fields such as student ID, first and last name, email, department, etc." + '\n' + "Add and remove students as well as search for specific ones." + '\n' + "Restrict displayed data through various filters.")
    about_Label.grid(row = 0, column = 0, pady = (10, 0))
   

def aboutStudabase():
    newWindow = Toplevel(root)
    newWindow.title("About Studabase")
    newWindow.geometry("500x800")
    newWindow.iconbitmap('hat.ico')
    newWindow.resizable(width=True, height=True)     # Window size changeability
    
    about_Label = Label(newWindow, text = "SRDG - STUDABASE: The Student Database (Stoo-da-base)"  + '\n' + "Santosh Khadka        santoshkhadka@my.unt.edu"  + '\n' + "Reynaldo Ferrari      reynaldoferrari@my.unt.edu"  + '\n' + "Duncan Campbell       duncancampbell@my.unt.edu" + '\n' + "Gregory Tillotson     gregorytillotson@my.unt.edu")
    about_Label.grid(row = 0, column = 0, pady = (10, 0))
   
def mainWindow():
    # Root Options
    root.title("STUDABASE: The Student Database ")
    # Icon - .ico file should be in the same directory as this file.
    root.iconbitmap('hat.ico')
    # Window Size: root.geometry('500x600')
    root.geometry('800x800')
    # Stops windows size from being changeable
    root.resizable(width=True, height=True)
    # root.configure(bg = 'gray24')

    # MENU BAR
    menubar = tk.Menu(root)
    # File - Menu Bar
    fileMenu = tk.Menu(menubar, tearoff=0)
    #fileMenu.add_command(label="New Database", command=menuFunctions.placeHolderFunc)
    fileMenu.add_command(label="Open Database", command=insertData)
    fileMenu.add_command(label="Save As...(Current Database)", command=saveFile)
    fileMenu.add_separator()
    #fileMenu.add_command(label="Properties...", command=menuFunctions.placeHolderFunc)
    #fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=fileMenu)

    # Edit - Menu Bar
    editMenu = tk.Menu(menubar, tearoff=0)
    editMenu.add_command(label="Refresh Database", command=refreshTable)
    editMenu.add_separator()
    #editMenu.add_command(label="Select All", command=menuFunctions.placeHolderFunc)
    editMenu.add_separator()
    editMenu.add_command(label="Add Student", command=addStudent)
    editMenu.add_command(label="Delete Student(s)", command=deleteOne)
    editMenu.add_separator()
    menubar.add_cascade(label="Edit", menu=editMenu)

    # View - Menu Bar
    #viewMenu = tk.Menu(menubar, tearoff=0)
    #viewMenu.add_command(label="Choice 1", command=menuFunctions.placeHolderFunc)
    #viewMenu.add_command(label="Choice 2", command=menuFunctions.placeHolderFunc)
    #viewMenu.add_separator()
    #viewMenu.add_command(label="Choice 3", command=menuFunctions.placeHolderFunc)
    #viewMenu.add_command(label="Choice 4", command=menuFunctions.placeHolderFunc)
    #menubar.add_cascade(label="View", menu=viewMenu)
    
    # Settings - Menu Bar
    #settingsMenu = tk.Menu(menubar, tearoff=0)
    # Change id & pass for current database
    #settingsMenu.add_command(label="Database Settings", command=menuFunctions.placeHolderFunc)
    # Change email platform/tool
    #settingsMenu.add_command(label="Email Platform", command=menuFunctions.placeHolderFunc)
    # Block changes - disables adding and deleting students (basically a read only mode)
    #settingsMenu.add_command( label="View Only Mode", command=menuFunctions.placeHolderFunc)
    # settingsMenu.add_separator()
    #menubar.add_cascade(label="Settings", menu=settingsMenu)

    # Help - Menu Bar
    helpmenu = tk.Menu(menubar, tearoff=0)
    # Display guide on how to use STUDABASE
    helpmenu.add_command(label="User Guide", command=userGuide)
    # Display info abut STUDABASE - Creators, when made, etc.
    helpmenu.add_command(label="About STUDABASE", command=aboutStudabase)
    # helpmenu.add_separator()
    menubar.add_cascade(label="Help", menu=helpmenu)

    filterOptions()
    dataTable()
    bottomButtons()
  
    # Needed for Menu bar
    root.config(menu=menubar)
    # GUI program is constantly looping to check for changes - Loop created
    root.mainloop()  # THIS SHOULD BE THE LAST LINE
