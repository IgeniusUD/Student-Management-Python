import sqlite3

connection=sqlite3.connect('stud_manage.db')
print("Database opened successfully")

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_PHONE = "student_phone"
STUDENT_COLLEGE = "student_college"

connection.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME +
                   " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " + STUDENT_PHONE + " INTEGER);")
print("table created successfully")



import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("DATABASE")

heading_label = tk.Label(mainWindow, text ="Student Database Management")
heading_label.pack()

l1=tk.Label(mainWindow, text="Enter Name")
l1.pack()
a = tk.Entry(mainWindow)
a.pack()

l2=tk.Label(mainWindow, text="Enter College")
l2.pack()
b = tk.Entry(mainWindow)
b.pack()

l3=tk.Label(mainWindow, text="Enter ID")
l3.pack()
c = tk.Entry(mainWindow)
c.pack()

l4=tk.Label(mainWindow, text="Enter Phone")
l4.pack()
d = tk.Entry(mainWindow)
d.pack()

def add():
    name = a.get()
    college = b.get()
    id = c.get()
    phone = d.get()

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_ID + " , " +
                           STUDENT_NAME + " , " + STUDENT_PHONE + " , " +
                           STUDENT_COLLEGE + " ) VALUES ( " + id + ", '" + name + "', " + phone + ", '" + college + "'); ")
    connection.commit()



def sub():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    for row in cursor:
        print("Student id is: ", row[0])
        print("Student name is: ", row[1])
        print("Student college is: ", row[2])
        print("Student phone is:", row[3])

    connection.close()

add2 = tk.Button(mainWindow, text="New Entry to Database",command=lambda : add())
add2.pack()

sub2 = tk.Button(mainWindow, text="Retrieve data from Database",command=lambda : sub())
sub2.pack()

mainWindow.mainloop()