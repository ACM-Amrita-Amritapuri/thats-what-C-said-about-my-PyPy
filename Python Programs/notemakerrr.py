from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import sqlite3

class Note:

#-----------Defining section------------------

    def __init__(self,root):
        self.root=root
        self.root.title('Notemaker Application')
        self.root.geometry('1350x700+0+0')


        title=Label(self.root,text='Notemaker Application', font=('times new roman',25,'bold'),fg='black')
        title.pack(side=TOP,fill=X)

 #-----------Data section------------------

        self.title_var=StringVar()
        self.note_var=StringVar()
        self.search_txt=StringVar()


#-----------Manage section------------------

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE)
        Manage_Frame.place(x=20,y=70,width=650,height=560)

        m_title=Label(Manage_Frame,text='Manage Notes', font=('times new roman',20,'bold'),fg='black')
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_ntitle=Label(Manage_Frame,text='Title',font=('times new roman',15,'bold'),fg='black')
        lbl_ntitle.grid(row=1,column=0,pady=20,sticky='w')

        txt_ntitle=Entry(Manage_Frame, textvariable=self.title_var, font=('times new roman',15,'bold'),bd=5,fg='black',relief=GROOVE)
        txt_ntitle.grid(row=1,column=1,pady=20,padx=20,sticky='w')

        lbl_ntitle=Label(Manage_Frame,text='Note', font=('times new roman',15,'bold'),fg='black')
        lbl_ntitle.grid(row=2,column=0,pady=20,sticky='w')

        self.txt_note=Text(Manage_Frame,width=55,height=10, font=('times new roman',15,'bold'))
        self.txt_note.grid(row=2,column=1,pady=20,padx=20,sticky='w')

#-----------Manage button section------------------

        Btn_Frame=Frame(Manage_Frame,bd=4)
        Btn_Frame.place(x=55,y=500,width=500)

        add_btn=Button(Btn_Frame,text='Add',command=self.add_notes,width=12,font=('times new roman',10,'bold'),fg='black').grid(row=0,column=0,padx=10,pady=10)
        upd_btn=Button(Btn_Frame,text='Update',width=12,command=self.update,font=('times new roman',10,'bold'),fg='black').grid(row=0,column=1,padx=10,pady=10)
        del_btn=Button(Btn_Frame,text='Delete',width=12,command=self.delete,font=('times new roman',10,'bold'),fg='black').grid(row=0,column=2,padx=10,pady=10)
        clr_btn=Button(Btn_Frame,text='Clear',command=self.clear,width=12,font=('times new roman',10,'bold'),fg='black').grid(row=0,column=3,padx=10,pady=10)




#-----------Display section------------------

        Display_Frame=Frame(self.root,bd=4,relief=RIDGE)
        Display_Frame.place(x=700,y=70,width=600,height=560)

        d_title=Label(Display_Frame,text='Display Notes', font=('times new roman',20,'bold'),fg='black')
        d_title.grid(row=0,columnspan=2,pady=20)

        lbl_ntitle=Label(Display_Frame,text='Title', font=('times new roman',15,'bold'),fg='black')
        lbl_ntitle.grid(row=1,column=0,pady=20,sticky='w')

        txt_ser=Entry(Display_Frame,font=('times new roman',15,'bold'), textvariable=self.search_txt,bd=5,fg='black',relief=GROOVE)
        txt_ser.grid(row=1,column=1,pady=20,padx=20,sticky='w')

#-----------Display button section------------------

        ser_btn=Button(Display_Frame,text='Search',command=self.search_data,width=12,font=('times new roman',10,'bold'),fg='black').grid(row=1,column=2,padx=10,pady=10)
        sho_btn=Button(Display_Frame,text='Show all',command=self.fetch_data,width=12,font=('times new roman',10,'bold'),fg='black').grid(row=1,column=3,padx=10,pady=10)

#-----------Database section------------------

        con=sqlite3.connect('notes.db')
        cur=con.cursor()
        cur.execute('''create table if not exists note(id integer primary key autoincrement, title text,noted text)''')
        con.commit()
        con.close()

#-----------Table section------------------

        Table_Frame=Frame(Display_Frame,bd=4)
        Table_Frame.place(x=25,y=150,width=550,height=360)

        scrool_v=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scrool_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Note_Table=ttk.Treeview(Table_Frame,columns=('ID','Title','Note'),xscrollcommand=scrool_v.set,yscrollcommand=scrool_y.set)
        scrool_v.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)
        scrool_v.config(command=self.Note_Table.xview)
        scrool_y.config(command=self.Note_Table.yview)
        self.Note_Table.heading('ID',text='ID')
        self.Note_Table.heading('Title',text='Title')
        self.Note_Table.heading('Note',text='Note')

        self.Note_Table['show']='headings'
        self.Note_Table.column('ID',width=50)
        self.Note_Table.column('Title',width=100)
        self.Note_Table.column('Note',width=500)
        self.Note_Table.pack(fill=BOTH,expand=1)
        self.Note_Table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()


#-----------Functions section------------------

    def add_notes(self):
        if self.title_var.get()=="" or self.txt_note.get('1.0',END)=="":
            mb.showwarning('Error','All fields are requided')
        else:
            con=sqlite3.connect('notes.db')
            cur=con.cursor()
            sqlite_query='''insert into note(title,noted) values(?,?)'''
            datas=(self.title_var.get(),self.txt_note.get('1.0',END))
            cur.execute(sqlite_query,datas)
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            mb.showinfo('Success','Note has been Added')
    
    def fetch_data(self):

        con=sqlite3.connect('notes.db')
        cur=con.cursor()
        sqlite_query='''select id,title,noted from note'''
        cur.execute(sqlite_query)
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Note_Table.delete(*self.Note_Table.get_children())
            for row in rows:
                self.Note_Table.insert('',END,values=row)
            con.commit()
        else:
            self.Note_Table.delete(*self.Note_Table.get_children())
        con.close()
        self.search_txt.set('')

    def clear(self):
        self.title_var.set('')
        self.txt_note.delete('1.0',END)

    def get_cursor(self,event):
        cursor_row=self.Note_Table.focus()
        contents=self.Note_Table.item(cursor_row)
        row=contents['values']
        self.title_var.set(row[1])
        self.txt_note.delete('1.0',END)
        self.txt_note.insert(END,row[2])
        
    def update(self):
        con=sqlite3.connect('notes.db')
        cur=con.cursor()
        sqlite_query='''update note set title=?,noted=? where id=?'''
        cursor_row=self.Note_Table.focus()
        contents=self.Note_Table.item(cursor_row)
        row=contents['values']
        datas=(self.title_var.get(),self.txt_note.get('1.0',END),row[0])
        cur.execute(sqlite_query,datas)
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        mb.showinfo('Success','Note has been updated')

    def delete(self):
        con=sqlite3.connect('notes.db')
        cur=con.cursor()
        cursor_row=self.Note_Table.focus()
        contents=self.Note_Table.item(cursor_row)
        row=contents['values']
        cur.execute('''delete from note where id=%d''' % (row[0]))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        mb.showwarning('Delete','Note deleted')

    def search_data(self):
        if self.search_txt.get()=='':
            mb.showerror('Error','Search text not found')
        else:
            con=sqlite3.connect('notes.db')
            cur=con.cursor()
            cur.execute("select * from note where title like ?", ('%'+self.search_txt.get()+'%',))
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Note_Table.delete(*self.Note_Table.get_children())
                for row in rows:
                    self.Note_Table.insert('',END,values=row)
                con.commit()
            else:
                self.Note_Table.delete(*self.Note_Table.get_children())
            con.close()

#-----------Loop section------------------

root=Tk()
ob=Note(root)
root.mainloop()
