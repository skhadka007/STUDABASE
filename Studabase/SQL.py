from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import pymysql

root = Tk()
root.title('STUDABASE - Students Database')
root.geometry('400x400')


'''
First_Name
Last_Name
Student_ID
Email
Department
Major
Grad_Date
'''

#Creates Function to Delete Record from Database
def submit():
    host = "reydb3444.cf8ohqjek0e0.us-east-2.rds.amazonaws.com"
    port = 3306
    dbname = "reydb"
    user = "masterUsername"
    password = "3444testdb"

    conn = pymysql.connect(host, user=user, port=port,
                           passwd=password, db=dbname)

    # create cursor
    c = conn.cursor()


    c.execute("INSERT INTO student_table VALUES (:First_Name, :Last_Name, :Student_ID, :Email, :Department, :Major, :Grad_Date)")
    {
            'First_Name': First_Name.get(),
            'Last_Name': Last_Name.get(),
            'Student_ID': Student_ID.get(),
            'Email': Email.get(),
            'Department': Department.get(),
            'Major': Major.get(),
            'Grad_Date': Grad_Date.get()
    }

    c.commit()

    c.close()

#Create Function to Query from Database
def query():
    host = "reydb3444.cf8ohqjek0e0.us-east-2.rds.amazonaws.com"
    port = 3306
    dbname = "reydb"
    user = "ASK"
    password = "ASK"

    conn = pymysql.connect(host, user=user, port=port,
                           passwd=password, db=dbname)

    # create cursor
    c = conn.cursor()

    # QUERY FROM TABLE
    c.execute('SELECT * FROM student_table ')
    records = c.fetchall()
    # print(records)

    # Loop Thru Results
    print_records = ''
    for each_record in records:
        print_records += str(each_record) + '\n'

    query_label = Label(root, text = print_records)
    query_label.grid(row = 8, column = 0, columnspan = 2)



    #conn.commit()

    conn.close()




    # Clear The Text Boxes
    First_Name.delete(0, END)
    Last_Name.delete(0, END)
    Student_ID.delete(0, END)
    Email.delete(0, END)
    Department.delete(0, END)
    Major.delete(0, END)
    Grad_Date.delete(0, END)




#Create Text Boxes
First_Name = Entry(root, width = 30)
First_Name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

Last_Name = Entry(root, width = 30)
Last_Name.grid(row = 1, column = 1, padx = 20)

Student_ID = Entry(root, width = 30)
Student_ID.grid(row = 2, column = 1, padx = 20)

Email = Entry(root, width = 30)
Email.grid(row = 3, column = 1, padx = 20)

Department = Entry(root, width = 30)
Department.grid(row = 4, column = 1, padx = 20)

Major = Entry(root, width = 30)
Major.grid(row = 5, column = 1, padx = 20)

Grad_Date = Entry(root, width = 30)
Grad_Date.grid(row = 6, column = 1, padx = 20)

#Create Text Box Labels
First_Name_Label = Label(root, text = 'First Name')
First_Name_Label.grid(row = 0, column = 0, pady = (10, 0))

Last_Name_Label = Label(root, text = 'Last Name')
Last_Name_Label.grid(row = 1, column = 0)

Student_ID_Label = Label(root, text = 'Student ID')
Student_ID_Label.grid(row = 2, column = 0)

Email_Label = Label(root, text = 'Email')
Email_Label.grid(row = 3, column = 0)

Department_Label = Label(root, text = 'Department')
Department_Label.grid(row = 4, column = 0)

Major_Label = Label(root, text = 'Major')
Major_Label.grid(row = 5, column = 0)

Grad_Date_Label = Label(root, text = 'Grad Date')
Grad_Date_Label.grid(row = 6, column = 0)

#Create Submit Button

Submit_button = Button(root, text = 'Add Record to Database', command = submit )
Submit_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#Create Query Button
query_button = Button(root, text = 'Show Record', command = query)
query_button.grid(row = 8, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#Create Delete Button


root.mainloop()
