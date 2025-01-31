from tkinter import *
from tkinter import ttk

from traverse.db.tables.User import User
from traverse.db.tables.Customer import Customer as cus

class Customer:
    def __init__(self, session):
        self.customer_screen = Tk()
        self.session = session
        self.customer_screen.title("Customer Dashboard")
        self.customer_screen.geometry("915x600")
        self.container_tree = Frame(self.customer_screen, width=100, height=300)
        self.container_tree.grid(row=0, column=0)
        self.container_tree.pack_propagate(0)
        columns = ('name', 'dob', 'phno', 'address', 'email', 'username', 'password', 'age')
        self.customer_tree = ttk.Treeview(self.container_tree, columns=columns, show='headings')
        self.customer_tree.heading('name', text='name')
        self.customer_tree.heading('dob', text='dob')
        self.customer_tree.heading('phno', text='phno')
        self.customer_tree.heading('address', text='address')
        self.customer_tree.heading('email', text='email')
        self.customer_tree.heading('username', text='username')
        self.customer_tree.heading('password', text='password')
        self.customer_tree.heading('age', text='age')
        self.customer_tree.column("name", width=150)
        self.customer_tree.column("dob", width=80)
        self.customer_tree.column("phno", width=80) 
        self.customer_tree.column("address", width=200)
        self.customer_tree.column("email", width=150)
        self.customer_tree.column("username", width=100)
        self.customer_tree.column("password", width=120) 
        self.customer_tree.column("age", width=30)
        contacts = []
        result = session.query(cus).join(User).all()
        for row in result:
            u = row.user
            contacts.append((u.name, u.dob, u.phno, u.address, u.email, u.username, u.password, u.age))
        for contact in contacts:
            self.customer_tree.insert('', END, values=contact)
        self.customer_tree.grid(row=0, column=0, sticky='nsew')
        h = Scrollbar(self.customer_screen, orient = 'horizontal')
        h.configure(command=self.customer_tree.xview)
        h.grid(row=1, column=0, sticky='we', columnspan=3)
        v = Scrollbar(self.customer_screen)
        v.grid(row=0, column=1, sticky='ns')
        self.customer_tree.configure(yscrollcommand=v.set, xscrollcommand=h.set)
        self.customer_screen.mainloop()