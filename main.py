#IMPORTING LIBRARIES:
from tkinter import *     #GUI Library for python
from tkinter import ttk   #Themed widgets from tkinter (e.g., Combobox, Treeview
from db import Database   #db: A separate file/module that handles database operations (Database class).
#
db = Database("Employee.db")  # Connects to the SQLite database
#
#
# #MAIN WINDOW SETUP:
root = Tk()                   # Main window
root.title("Employee management system")
root.geometry("1920x1080+0+0")  # Window size & position
root.config(bg="#2c3e58")       # Background color
root.state("zoomed")            # Maximizes the window
#
# #Tkinter Variables:
name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
Email = StringVar()
contact = StringVar()
#
# #  Frame for Input Fields:
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
#
# # Title label
title = Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
#
# # Name
lblName = Label(entries_frame, text="Name", font=("Calibri", 18), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")
#
# # Age
lblAge = Label(entries_frame, text="Age", font=("Calibri", 18), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2, padx=10, pady=10)
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10)
#
# # Date of Joining (D.O.J)
lblDOJ = Label(entries_frame, text="D.O.J", font=("Calibri", 18), bg="#535c68", fg="white")
lblDOJ.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtDOJ = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
txtDOJ.grid(row=2, column=1, padx=10, pady=10, sticky="w")
#
# # Contact
lblcontact = Label(entries_frame, text="Contact", font=("Calibri", 18), bg="#535c68", fg="white")
lblcontact.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtcontact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtcontact.grid(row=2, column=3, padx=10, pady=10, sticky="w")
#
# # Email
lblemail = Label(entries_frame, text="Email", font=("Calibri", 18), bg="#535c68", fg="white")
lblemail.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtemail = Entry(entries_frame, textvariable=Email, font=("Calibri", 16), width=30)
txtemail.grid(row=3, column=3, padx=10, pady=10, sticky="w")
#
# # Gender
lblGender = Label(entries_frame, text="Gender", font=("Calibri", 18), bg="#535c68", fg="white")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 18), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, pady=10, sticky="w")
#
# # Address
lblAddress = Label(entries_frame, text="Address", font=("Calibri", 18), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtAddress = Text(entries_frame, width=60, height=5, font=("Calibri", 16))
txtAddress.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky="w")
#
# #CRUD OPERATIONS:
def displayAll():
    # Clears the Treeview and re-populates it from the database
    for item in tv.get_children():
        tv.delete(item)
    # Insert rows from DB
    for row in db.fetch():
        tv.insert("", END, values=row)
#
#
def clearAll():  #The clearAll() function in your Employee Management System resets all the input fields in the form to empty, so you can start entering fresh data.
    print("ClearAll function called")  # debug
    name.set("")
    age.set("")
    doj.set("")
    Email.set("")
    gender.set("")
    contact.set("")
    txtAddress.delete("1.0", END)
#
# #ADD EMPLOYEE:
# # #Gets data from input field
# # Calls insert() from the database module
# # Updates the Treeview and clears the form
#
def add_employee():
    nm = name.get()
    ag = age.get()
    d = doj.get()
    em = Email.get()
    gen = gender.get()
    cont = contact.get()
    addr = txtAddress.get("1.0", END).strip()
#
    if not (nm and ag and d and em and gen and cont and addr):
        print("Please fill all the fields")
        return

    db.insert(nm, ag, d, em, gen, cont, addr)
    displayAll()
    clearAll()

#
# #Grabs currently selected row’s ID.
#
# # Reads & validates the form.
# # Calls db.update() with the ID + new data.
# # Refreshes and clears on success.
#
def update_employee():
    selected = tv.focus()
    if not selected:
        print("Select an employee to update")
        return

    values = tv.item(selected, 'values')
    if not values:
        print("No values found for the selected row")
        return

    emp_id = values[0]
#
    nm = name.get()
    ag = age.get()
    d = doj.get()
    em = Email.get()
    gen = gender.get()
    cont = contact.get()
    addr = txtAddress.get("1.0", END).strip()

    if not (nm and ag and d and em and gen and cont and addr):
        print("Please fill all fields")
        return
#
    success = db.update(emp_id, nm, ag, d, em, gen, cont, addr)
    if success:
        print("Employee updated successfully")
        displayAll()
        clearAll()
    else:
        print("Update failed")
#
# # #Gets selected row’s ID.
# # Calls db.remove().
# # Refreshes and clears if the deletion succeeded.
#
def delete_employee():
    selected = tv.focus()
    if not selected:
        print("No row selected.")
        return

    data = tv.item(selected)['values']
    if not data:
        return

    id = data[0]

    if db.remove(id):
        displayAll()
        clearAll()
        print("Employee deleted successfully!")
    else:
        print("Failed to delete.")

#
# #Frame to hold your four CRUD buttons:
btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
#
# #Creates and places the Add, Update, Delete, and Clear buttons in a single row:
# #
# # What is a grid in Tkinter?
# # In Tkinter, grid is a geometry manager — a system that controls where and how widgets (like buttons, labels, text boxes) are placed inside a window or frame.
# #
# # How does the grid work?
# # The container (like a window or frame) is imagined as a table made of rows and columns, just like a spreadsheet.
# #
# # You place widgets by specifying which row and column they should appear in.
# #
# # Each cell in this table can hold one widget.
# #
# # Widgets can also span multiple rows or columns.
#
#
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15,
                font=("Calibri", 16, "bold"), fg="white", bg="#16a085")  #fg = foreground colour
btnAdd.grid(row=0, column=0)
btnUpdate = Button(btn_frame, command=update_employee, text="Update", width=15,
                   font=("Calibri", 16, "bold"), fg="white", bg="#2980b9") #bg background colour
btnUpdate.grid(row=0, column=1, padx=5, pady=5)

btnDelete = Button(btn_frame, command=delete_employee, text="Delete", width=15,
                   font=("Calibri", 16, "bold"), fg="white", bg="#c0392b")
btnDelete.grid(row=0, column=2, padx=5, pady=5)

btnClear = Button(btn_frame, command=clearAll, text="Clear All", width=15,
                  font=("Calibri", 16, "bold"), fg="white", bg="#f39c12")
btnClear.grid(row=0, column=3, padx=5, pady=5)

#Table (Treeview) Setup:
# tree_frame is the frame where your table (Treeview) will be placed
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
#
#Frame for the data table; fills remaining space:
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))
#
#
# #Configures font and row height for rows and headers:
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=50)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3", width=50)
tv.heading("4", text="D.O.J")
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.column("6", width=80)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv["show"] = 'headings'
tv.pack(fill=X)
#
# #Enable row selection from the Treeview:
#
# # When you click a row, getData() is called:
# # Retrieves the values of that row.
# # Populates the form fields so you can Update/Delete them.
#
def getData(event):
    selected_row = tv.focus()
    if not selected_row:
        return

    data = tv.item(selected_row)['values']
    if not data:
        return

    # Fill form fields
    name.set(data[1])
    age.set(data[2])
    doj.set(data[3])
    Email.set(data[4])
    gender.set(data[5])
    contact.set(data[6])
    txtAddress.delete("1.0", END)
    txtAddress.insert(END, data[7])
#
tv.bind("<ButtonRelease-1>", getData)

#Bootstrap & Event Loop:
#Enters Tk’s event loop so the GUI becomes interactive until you close it:


displayAll()

root.mainloop() 
