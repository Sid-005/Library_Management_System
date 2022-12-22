pas = ''
import ctypes
import tkinter
ctypes.windll.shcore.SetProcessDpiAwareness(1)   # to increase clarity

# View Transactions (5)______________________________________________________________________________________________________________________ 
L3 = []
def return_3(e):
    """Function used to return values inserted into the entry widget of tkinter module for further processing"""
    global L3
    x = e.widget.get()
    L3.append(x)
    
def history():
    """Function to view all the transactions that have been carried out within the library"""
    import mysql.connector
    global pas
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = pas,
        database = "library")
    cursor = db.cursor()
    cursor.execute ("Select LibID, Name, transactions.BookID, BookName, Issue_Date, Status, Return_Date from Transactions, booklog where Booklog.BookID = transactions.BookID")
    print()
    print("Transaction History")
    print ()
    for i in cursor:
        print ("Lib ID:\t\t", i[0])
        print ("Name:\t\t", i[1])
        print ("BookID:\t\t", i[2])
        print ("Book Name:\t", i[3])
        print ("Issue Date:\t", i[4])
        print ("Status:\t\t", i[5])
        print ("Return Date:\t", i[6])
        print ()
    db.close()

def search ():
    """Function to search all the transactions tha have been carried out for instances of a particular entry"""
    global L3
    name = L3[0]
    libid = L3[1]
    import mysql.connector
    global pas
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = pas,
        database = "library")
    cursor = db.cursor()
    cursor.execute ("Select LibID, Name, transactions.BookID, BookName, Issue_Date, Status, Return_Date from Transactions, booklog where Booklog.BookID = transactions.BookID and LibID = {}". format(libid))
    print()
    print("Transaction History")
    print ()
    x = cursor.fetchall()
    if x == []:
        print ("No record Found. Library ID may be invalid")
        L3 = []
    else:
        for i in x:
            print ("Lib ID:\t\t", i[0])
            print ("Name:\t\t", i[1])
            print ("BookID:\t\t", i[2])
            print ("Book Name:\t", i[3])
            print ("Issue Date:\t", i[4])
            print ("Status:\t\t", i[5])
            print ("Return Date:\t", i[6])
            print ()
        db.close()
        L3 = []

def transac():
    """Function to generate the window to carry out the transaction review processes"""
    window = tkinter.Toplevel()
    window.title("Transactions")
    window.geometry ("700x480")
    img = tkinter.PhotoImage (file = "image.png")
    looks = tkinter.Label (window, image = img).place (x=0, y=0)
    head = tkinter.Label (window, font =("Arial", 30), text = "Transaction History", bg = "#FF4040", fg = "white", width = 26).place (x=0, y=0)
    
    name = tkinter.Label (window, font =("Arial", 23), text = "Name", bg = "#B22222", fg = "#FFD700").place(x=50, y = 100)
    number = tkinter.Label (window, font = ("Arial", 23), text ="Lib ID", bg = "#B22222", fg = "#FFD700").place (x=50, y=200)

    e1 = tkinter.Entry (window, font=("Arial", 20), bg = "grey80", fg = "black", width = 20 )
    e2 = tkinter.Entry (window, font=("Arial", 20), bg = "grey80", fg = "black", width = 20 )
    e1.place(x=300, y=100)
    e2.place (x=300, y=200)
    e1.bind("<Return>", return_3)
    e2.bind("<Return>", return_3)

    Button1 = tkinter.Button (window, font=("Arial", 20), width = 10, text="Search", bg = "#483D8B", fg = "#FFD700", command =  lambda: [search(), window.destroy()]).place(x=280, y =280)
    Or = tkinter.Label(window, font =("Arial", 15), text = "OR", bg = "#B22222", fg = "#FFD700").place(x= 360, y = 360)
    button2 = tkinter.Button (window, font =("Arial", 20), width = 15, text="View all", bg= "#483D8B", fg = "#FFD700", command = lambda: [history(), window.destroy()]). place(x=240, y=400)
    window.mainloop()

    
#__________issue (4) __________________________________________________________________________________________________________________________________
L2 = []
def return_2(e):
    """Function used to return values inserted into the entry widget of tkinter module for further processing"""
    global L2
    x = e.widget.get()
    L2.append(x)

def add_2():
    """Function to add new transaction to the table storing all th transactions within the database"""
    global L2
    LibID = L2[0]
    Name = L2[1]
    BookID = L2[2]
    status = L2[3]
    
    import mysql.connector
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = pas,
        database = "library")
    cursor = db.cursor()
    cursor.execute ("select * from Booklog")
    x = cursor.fetchall()
    flag = 0
    if status.lower() == "issued":
        for i in x:
            if i[0] == int(BookID):
                cursor.execute ("insert into transactions (LibID, Name, BookID, Status) values ({}, '{}', {}, '{}')". format(LibID, Name, BookID, status))
                from tkinter import messagebox
                messagebox.showinfo(title= "SUCCESS", message= "Records have been updated succesfully!")
                flag = 1
                break
        if flag == 0:
            from tkinter import messagebox
            messagebox.showwarning(title= "INVALID", message= "Invalid Book ID. Please Close the window and try again.")
        db.commit()
        db.close()
        L2 = []
    else:
        for i in x:
            if i[0] == int(BookID):
                cursor.execute ("update transactions set Status = 'returned', Return_Date = NOW() where LibID = {} and Name = '{}' and BookID = {} and Status = 'issued'". format (LibID, Name, BookID))
                from tkinter import messagebox
                messagebox.showinfo(title= "SUCCESS", message= "Records have been updated succesfully!")
                flag = 1
                break
        if flag == 0:
            from tkinter import messagebox
            messagebox.showwarning(title= "INVALID", message= "Invalid Book ID. Please Close the window and try again.")
        db.commit()
        db.close()
        L2 = [] 


def issue():
    """Function to generate the window for allowing the user to issue books"""
    lib=tkinter.Toplevel()

    #Title/Window size
    lib.title("Book Issue")
    lib.geometry("700x770")
    image = tkinter.PhotoImage (file = "image.png")
    Back2 = tkinter. Label (lib, image = image). place(x=0, y=0)
    title = tkinter.Label (lib, font=("Arial" , 33),text="BOOK ISSUE", width= 22, bg="#483D8B" , fg="white").place (x=0, y=0)

    #Label
    ID = tkinter.Label(lib, text="Library ID",font=("Arial" , 25), bg = "#FFD39B").place(x=40, y=180)
    name = tkinter.Label(lib, text="Name",font=("Arial" , 25), bg="#FFD39B").place(x=40,y=280)
    bookID = tkinter.Label(lib, text="Book ID",font=("Arial" , 25), bg = "#FFD39B").place(x=40,y=380)
    status= tkinter.Label(lib, text="Status",font=("Arial" , 25), bg = "#FFD39B").place(x=40,y=480)

    #Entry
    e1 = tkinter.Entry(lib, font=("Arial" , 20), bg= "grey60", fg = "white", width=20)
    e2 = tkinter.Entry(lib, font=("Arial" , 20), bg= "grey60", fg = "white", width=20)
    e3 = tkinter.Entry(lib, font=("Arial" , 20), bg= "grey60", fg = "white", width=20)
    e4 = tkinter.Entry(lib, font=("Arial" , 20), bg= "grey60", fg = "white", width=20)
    e1.place(x= 300, y= 180)
    e2.place(x= 300, y= 280)
    e3.place(x= 300, y= 380)
    e4.place(x= 300, y= 480)
    e1.bind("<Return>", return_2)
    e2.bind("<Return>", return_2)
    e3.bind("<Return>", return_2)
    e4.bind("<Return>", return_2)


    #Button
    b = tkinter.Button (lib, text="Enter", font=("Arial", 25), width=20, bg="#2F4F4F" ,fg="#FFB90F" , command= lambda: [add_2(), lib.destroy()]).place(x= 60,y= 590)
    
    lib.mainloop()

# BookLog begins here (3)_________________________________________________________________________________________________________
L = []

def return_1(e):
    """Function used to return values inserted into the entry widget of tkinter module for further processing"""
    global L
    x = e.widget.get()
    L.append(x)

def delete():
    """Function to allow user to delete entries of books found in the library"""
    global L
    name = L[0]
    number = L[1]
    import mysql.connector
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = pas,
        database = "library")
    cursor = db.cursor()
    cursor.execute ("Delete from Booklog where BookID = {}". format (number))
    from tkinter import messagebox
    messagebox.showinfo(title= "SUCCESS", message= "Book has been deleted succesfully!")
    db.commit()
    db.close()
    L = []

def add():
    """Function to allow the user to add new entries for books found in the library"""
    global L
    name = L[0]
    number = L[1]
    
    import mysql.connector
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = pas,
        database = "library")
    cursor = db.cursor()
    cursor.execute ("insert into BookLog values ({}, '{}')". format(number, name))
    from tkinter import messagebox
    messagebox.showinfo(title= "SUCCESS", message= "Book has been added succesfully!")
    db.commit()
    db.close()
    L = []


def obtain():
    """Function to display all the books available in the library"""
    import mysql.connector
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = pas,
        database = "library")
    cursor = db.cursor()
    cursor.execute ("Select * from BookLog")
    x = cursor.fetchall()
    print()
    print("Details of books available")
    if x == []:
        print ("Empty Library")
    else:
        for i in x:
            print ("Book ID:\t\t", i[0])
            print ("Book Name:\t", i[1])
            print ()
    db.close()
  


def booklog():
    """Function to generate the window for allowing the user to view all the books available in the library"""
    window = tkinter.Toplevel()
    window.title("Book Log")
    window.geometry ("700x480")
    img = tkinter.PhotoImage (file = "image.png")
    looks = tkinter.Label (window, image = img).place (x=0, y=0)
    head = tkinter.Label (window, font =("Arial", 30), text = "Add Book to Library", bg = "#FF4040", fg = "white", width = 26).place (x=0, y=0)

    name = tkinter.Label (window, font =("Arial", 23), text = "Name", bg = "#B22222", fg = "#FFD700").place(x=50, y = 150)
    number = tkinter.Label (window, font = ("Arial", 23), text ="Book ID", bg = "#B22222", fg = "#FFD700").place (x=50, y=250)

    e1 = tkinter.Entry (window, font=("Arial", 20), bg = "grey80", fg = "black", width = 20 )
    e2 = tkinter.Entry (window, font=("Arial", 20), bg = "grey80", fg = "black", width = 20 )
    e1.place(x=300, y=150)
    e2.place (x=300, y=250)
    e1.bind("<Return>", return_1)
    e2.bind("<Return>", return_1)
    
    Button1 = tkinter.Button (window, font=("Arial", 20), width = 10, text="Add", bg = "#483D8B", fg = "#FFD700", command =  lambda: [add(), window.destroy()]).place(x=130, y =310)
    button2 = tkinter.Button (window, font =("Arial", 20), width = 15, text="View all Books", bg= "#483D8B", fg = "#FFD700", command = lambda: [obtain(), window.destroy()]). place(x=190, y=390)
    Button3 = tkinter.Button (window, font=("Arial", 20), width = 10, text="Delete", bg = "#483D8B", fg = "#FFD700", command =  lambda: [delete(), window.destroy()]).place(x=330, y =310)

    window.mainloop()
    
# Menu for choosing (2) _________________________________________________________________________________________________________
def new():
    """Function to generate the main window of the program"""
    
    main = tkinter.Tk()
    main.title("LIBRARY DATABASE")
    bg = tkinter.PhotoImage (file = "image.png")
    frame= tkinter.Frame(main, bg="grey60", width= 800 , height=550).pack()
    Backg = tkinter.Label(main, image = bg).place (x=0, y=0)
    main.geometry("800x550")
    title = tkinter.Label(main , font =("Arial", 35), text = "Library Database", bg="#E3CF57" , width = 25).place( x=0 ,y=0)

    #Options: (buttons)
    b1 = tkinter.Button(main, text ="Book Log", font=("Arial", 25), width=10, bg="white smoke", fg="Black", command = lambda:booklog()).place (x = 260, y = 150)
    b2 = tkinter.Button (main, text = "Issue & Return", font =("Arial", 25), width = 13, bg="white smoke", fg="Black", command =lambda: issue()).place(x=240, y = 275)
    b3 = tkinter.Button (main, text = "Transactions", font = ("Arial", 25), width = 10, bg="white smoke", fg="Black", command =lambda: transac()).place (x=260, y= 400)

    main.mainloop()

# Login Window (1) ______________________________________________________________________________________________________________  
def button_click():
    """Function to create a new database if the database does not already exist on the computer"""
    import mysql.connector
    global pas
    try:
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = pas)
        cursor = db.cursor()
        cursor.execute ("create database library")
        cursor.execute ("use library")
        cursor.execute ("CREATE TABLE booklog(BookID INT PRIMARY KEY, BookName VARCHAR(100))")
        cursor.execute (" CREATE TABLE transactions (LibID INT , Name VARCHAR(50),  BookID INT, Issue_Date DATETIME DEFAULT NOW(), Status VARCHAR (50), Return_Date DATETIME DEFAULT NULL)")
        db.close()
        win.destroy()
        new()

    except mysql.connector.errors.ProgrammingError: #check this area.....
        from tkinter import messagebox
        messagebox.showerror (title = "INCORRECT PASSWORD", message = "Invalid Password. Please try again")
        #until here
    except:
        win.destroy()
        new()
        


    
    
def r(e):
    """Function used to return values inserted into the entry widget of tkinter module for further processing"""
    global pas
    pas = e.widget.get()

# main
win = tkinter.Tk()
win.geometry = ("750x 220")
f = tkinter.Frame (win, bg = "grey60", width = "750", height = "220").pack()
win.title ("User Login Confirmation")
image1 = tkinter.PhotoImage (file = "image.png")
Looks = tkinter.Label (win, image = image1).place (x=0, y= 0)

# Options
l = tkinter.Label(win, font =("Arial", 22), text = "Please enter MySQL root password", bg = "#030303",fg = "#FFD700", width = 35).place(x=0,y=0)
e = tkinter.Entry (win, show = "*", font = ("Arial", 18), width = 30)
e.place (x = 125, y = 70)
e.bind("<Return>", r)
b = tkinter.Button (win, text = "Get", font = ("Arial", 19), width = 20, bg = "#FFD700", fg="#030303", command = lambda: button_click()).place (x = 170, y = 140)
win.mainloop()
#______________________________________________________________________________________________________________________________

