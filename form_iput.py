from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pyodbc
# import mysql.connector



conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=MSI;'
                    'Database=attendancedb;'
                    'Trusted_Connection=yes;')
cursor = conn.cursor()

def Insert(id_f,Name_f,Indate, Intime, Outdate, Outtime):

    sql='''insert into attendancedb.dbo.tbl_attendance (id_f,Name_f,Indate, Intime, Outdate, Outtime) values(?, ?,?,?, ?,?)'''

    val=(id_f,Name_f,Indate, Intime, Outdate, Outtime)
    cursor.execute(sql,val)
    conn.commit()


# markAttendance(name,'',str(crDate.date()),str(crTime.time()),'','')

    
 
def Ok():
    empname = e2.get()
    phone = e3.get()
    salary = e4.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="payrollpy")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO records (id,empname,phone,salary) VALUES (%s, %s, %s, %s)"
       val = ("",empname,phone,salary)
       mycursor.execute(sql, val)
       mysqldb.commit()
 
       lastid = mycursor.lastrowid
 
       messagebox.showinfo("information", "Record inserted successfully...")
       e1.delete(0, END)
       e1.insert(END, lastid)
 
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e2.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
root = Tk()
root.title("Employee Registation")
root.geometry("1000x600")
global e1
global e2
global e3
global e4
global e5
global e6
global e7
Label(root, text="ID").place(x=10, y=10)
Label(root, text="Name").place(x=10, y=40)
Label(root, text="Gender").place(x=10, y=70)
Label(root, text="phone").place(x=10, y=100)
Label(root, text="Year").place(x=10, y=130)
Label(root, text="Major").place(x=10, y=160)
Label(root, text="Address").place(x=10, y=190)
 


#Button ID 
e1 = Entry(root)
e1.place(x=140, y=10)
 
#Button Name
e2 = Entry(root)
e2.place(x=140, y=40)
 
#Button Gender
e3 = Combobox(root,values=['Men','Female'])
e3.place(x=140, y=70)

#Button phone
e4 = Entry(root)
e4.place(x=140, y=100)

#Button Year
e5 = Combobox(root, values=['Year:1','Year:2','Year:3','Year:4','Year:5'])
e5.place(x=140, y=130)

#Button Major
e6 = Entry(root)
e6.place(x=140, y=160)

#Button Address
e7 = Entry(root)
e7.place(x=140, y=190)




# Button insert updeted deleted GUI python with SQL sever 
Button(root, text="Add", command=Ok ,height = 1, width = 10).place(x=10, y=220)
Button(root, text="Updete", command=Ok ,height = 1, width = 10).place(x=100, y=220)
Button(root, text="Delete", command=Ok ,height = 1, width = 10).place(x=190, y=220)

Button(root, text="Browse", command=Ok ,height = 1, width = 10).place(x=550, y=190)
 


root.mainloop()



        # >>>>>> x = np.array([1, 2, 3])
        # >>>>>> x.ndim
        # #OutPut: 1

        # >>>>>> y = np.zeros((2, 3, 4))
        # >>>>>> y.ndim
        # #OutPut: 3