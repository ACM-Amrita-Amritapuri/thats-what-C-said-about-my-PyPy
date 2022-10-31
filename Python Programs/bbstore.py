from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox as mb

class Book:

    def __init__(self,root):
        self.root=root
        self.root.title('Book keeping app')
        self.root.geometry('600x600')


        self.title_text=StringVar()
        self.author_text=StringVar()
        self.year_text=StringVar()
        self.isbn_text=StringVar()
        self.search_var=StringVar()
        self.search_by_var=StringVar()

        Frame1=Frame(self.root,bd=4,bg='grey')
        Frame1.place(x=20,y=20,width=250,height=250)

        l1=Label(Frame1, text="Title",bg='grey').grid(row=0,column=0,pady=10,sticky='w')
        l2=Label(Frame1, text="Author",bg='grey').grid(row=1,column=0,pady=10,sticky='w')
        l3=Label(Frame1, text="Year",bg='grey').grid(row=2,column=0,pady=10,sticky='w')
        l4=Label(Frame1, text="ISBN",bg='grey').grid(row=3,column=0,pady=10,sticky='w')

        t1=Entry(Frame1,textvariable=self.title_text).grid(row=0, column=1)
        t2=Entry(Frame1,textvariable=self.author_text).grid(row=1, column=1)
        t3=Entry(Frame1,textvariable=self.year_text).grid(row=2,column=1)
        t4=Entry(Frame1,textvariable=self.isbn_text).grid(row=3, column=1)

        Frame2=Frame(self.root,bd=4,bg='grey')
        Frame2.place(x=300,y=20,width=250,height=250)

        b1 =Button(Frame2,text="View All",width=10,command=self.fetch_data).grid(row=1, column=0,padx=1,pady=4,sticky='w')
        b3 =Button(Frame2,text="Add",width=10,command=self.add_book).grid(row=1, column=1,padx=1,pady=4,sticky='w')
        b4 =Button(Frame2,text="Update",width=10,command=self.update_book).grid(row=2,column=0,padx=1,pady=4,sticky='w')
        b5 =Button(Frame2,text="Delete",width=10,command=self.delete_book).grid(row=2,column=1,padx=1,pady=4,sticky='w')

        l5=Label(Frame2, text="Search book",bg='grey',fg='black').grid(row=3,column=0,pady=4,sticky='w')
        t5=Entry(Frame2,textvariable=self.search_var).grid(row=3,column=1,padx=3,pady=4,sticky='w')
        l6=Label(Frame2, text="Search by",bg='grey',fg='black').grid(row=4,column=0,pady=4,sticky='w')
        combo_search=ttk.Combobox(Frame2,textvariable=self.search_by_var,width=10,state='readonly')
        combo_search['values']=('Title','Year','Author')
        combo_search.grid(row=4,column=1,padx=3,pady=3)
        b8 =Button(Frame2,text="Search",width=12,command=self.search_book).grid(row=5, column=0,pady=4)
        b9 =Button(Frame2,text="Show all",width=12,command=self.fetch_data).grid(row=5, column=1,pady=4)


        b6 =Button(Frame2,text="Clear",width=12,command=self.clear).grid(row=6, column=0,pady=4)
        b7 =Button(Frame2,text="Close",width=12,command=self.root.destroy).grid(row=6, column=1,pady=4)


        con=sqlite3.connect('books.db')
        cur=con.cursor()
        cur.execute('''create table if not exists book(id integer primary key autoincrement, title text,author text, year text, isbn text)''')
        con.commit()
        con.close()

        Frame3=Frame(self.root,bd=4,bg='grey')
        Frame3.place(x=20,y=300,width=550,height=250)

        scrool_v=Scrollbar(Frame3,orient=HORIZONTAL)
        scrool_y=Scrollbar(Frame3,orient=VERTICAL)
        self.Book_Table=ttk.Treeview(Frame3,columns=('ID','Title','Author','Year','ISBN'),xscrollcommand=scrool_v.set,yscrollcommand=scrool_y.set)
        scrool_v.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)
        scrool_v.config(command=self.Book_Table.xview)
        scrool_y.config(command=self.Book_Table.yview)
        self.Book_Table.heading('ID',text='ID')
        self.Book_Table.heading('Title',text='Title')
        self.Book_Table.heading('Author',text='Author')
        self.Book_Table.heading('Year',text='Year')
        self.Book_Table.heading('ISBN',text='ISBN')

        self.Book_Table['show']='headings'
        self.Book_Table.column('ID',width=50)
        self.Book_Table.column('Title',width=100)
        self.Book_Table.column('Author',width=100)
        self.Book_Table.column('Year',width=100)
        self.Book_Table.column('ISBN',width=100)
        self.Book_Table.pack(fill=BOTH,expand=1)
        self.Book_Table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    def fetch_data(self):
        con=sqlite3.connect('books.db')
        cur=con.cursor()
        cur.execute('select * from book')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Book_Table.delete(*self.Book_Table.get_children())
            for i in rows:
                self.Book_Table.insert('',END,values=i)
            con.commit()
        else:
            self.Book_Table.delete(*self.Book_Table.get_children())
        con.close()

    def get_cursor(self,event):
        cursor_row=self.Book_Table.focus()
        cont=self.Book_Table.item(cursor_row)
        row=cont['values']
        self.title_text.set(row[1])
        self.author_text.set(row[2])
        self.year_text.set(row[3])
        self.isbn_text.set(row[4])


    def clear(self):
        self.title_text.set('')
        self.author_text.set('')
        self.year_text.set('')
        self.isbn_text.set('')
        self.search_var.set('')
    
    def add_book(self):
        if self.title_text.get()=='' or self.author_text.get()=='' or self.year_text.get()=='':
            pass
        else:
            con=sqlite3.connect('books.db')
            cur=con.cursor()
            cur.execute('insert into book(title,author,year,isbn)values(?,?,?,?)',(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))
            con.commit()
            self.fetch_data()
            con.close()

    def update_book(self):
        con=sqlite3.connect('books.db')
        cur=con.cursor()
        cursor_row=self.Book_Table.focus()
        cont=self.Book_Table.item(cursor_row)
        row=cont['values']
        query='update book set title=?,author=?,year=?,isbn=? where id =?'
        data=(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get(),row[0])
        cur.execute(query,data)
        con.commit()
        self.fetch_data()
        con.close()
    
    def delete_book(self):
        con=sqlite3.connect('books.db')
        cur=con.cursor()
        cursor_row=self.Book_Table.focus()
        cont=self.Book_Table.item(cursor_row)
        row=cont['values']
        cur.execute('delete from book where id=%d' %(row[0]))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_book(self):
        if self.search_var.get()=='':
            mb.showerror('Error','Search text not found')
        else:
            con=sqlite3.connect('books.db')
            cur=con.cursor()
            if self.search_by_var.get()=='Title':
                cur.execute("select * from book where title like ?", ('%'+self.search_var.get()+'%',))
            elif self.search_by_var.get()=='Year':
                cur.execute("select * from book where year like ?", ('%'+self.search_var.get()+'%',))
            elif self.search_by_var.get()=='Author':
                cur.execute("select * from book where author like ?", ('%'+self.search_var.get()+'%',))
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Book_Table.delete(*self.Book_Table.get_children())
                for row in rows:
                    self.Book_Table.insert('',END,values=row)
                con.commit()
            else:
                mb.showerror('Error','Not found')
            con.close()


root=Tk()
ob=Book(root)
root.mainloop()
