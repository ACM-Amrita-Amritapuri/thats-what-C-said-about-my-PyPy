from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import sqlite3
# import pyperclip

class Contact:

#-----------Defining section------------------

    def __init__(self,root):
        self.root=root
        self.root.title('Contacts Application')
        self.root.geometry('1350x700+0+0')


        title=Label(self.root,text='Contacts Application', font=('times new roman',25,'bold'),fg='black',bg='cyan',relief=GROOVE)
        title.pack(side=TOP,fill=X)

 #-----------Data section------------------

        self.name_var=StringVar()
        self.phno_var=StringVar()
        self.search_txt=StringVar()
        self.search_by_var=StringVar()


#-----------Manage section------------------

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='cyan')
        Manage_Frame.place(x=20,y=70,width=650,height=560)

        m_title=Label(Manage_Frame,text='Manage Contact', font=('times new roman',20,'bold'),fg='black',bg='cyan')
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_ntitle=Label(Manage_Frame,text='Name',font=('times new roman',15,'bold'),fg='black',bg='cyan')
        lbl_ntitle.grid(row=1,column=0,pady=20,padx=20,sticky='w')

        txt_ntitle=Entry(Manage_Frame, textvariable=self.name_var, font=('times new roman',15,'bold'),bd=5,fg='black',relief=GROOVE,bg='cyan')
        txt_ntitle.grid(row=1,column=1,pady=20,padx=20,sticky='w')

        lbl_phnontitle=Label(Manage_Frame,text='Ph mp', font=('times new roman',15,'bold'),fg='black',bg='cyan')
        lbl_phnontitle.grid(row=2,column=0,pady=20,sticky='w')

        txt_phnotitle=Entry(Manage_Frame, textvariable=self.phno_var, font=('times new roman',15,'bold'),bd=5,fg='black',relief=GROOVE,bg='cyan')
        txt_phnotitle.grid(row=2,column=1,pady=20,padx=20,sticky='w')

#-----------Manage button section------------------

        Btn_Frame=Frame(Manage_Frame,bd=4,bg='cyan')
        Btn_Frame.place(x=55,y=500,width=500)

        add_btn=Button(Btn_Frame,text='Add contact',command=self.add_contact,width=12,font=('times new roman',10,'bold'),fg='black',bg='cyan').grid(row=0,column=0,padx=10,pady=10)
        upd_btn=Button(Btn_Frame,text='Update contact',width=12,command=self.update_contact,font=('times new roman',10,'bold'),fg='black',bg='cyan').grid(row=0,column=1,padx=10,pady=10)
        del_btn=Button(Btn_Frame,text='Delete contact',width=12,command=self.delete_contact,font=('times new roman',10,'bold'),fg='black',bg='cyan').grid(row=0,column=2,padx=10,pady=10)
        clr_btn=Button(Btn_Frame,text='Clear fields',command=self.clear_fields,width=12,font=('times new roman',10,'bold'),fg='black',bg='cyan').grid(row=0,column=3,padx=10,pady=10)
        # clr_btn=Button(Btn_Frame,text='Copy number',command=self.copy_con,width=12,font=('times new roman',10,'bold'),fg='black').grid(row=0,column=4,padx=10,pady=10)




#-----------Display section------------------

        Display_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='cyan')
        Display_Frame.place(x=700,y=70,width=600,height=560)

        lbl_ntitle=Label(Display_Frame,text='Search by', font=('times new roman',15,'bold'),fg='black',bg='cyan')
        lbl_ntitle.grid(row=0,column=0,pady=20,sticky='w')

        combo_search=ttk.Combobox(Display_Frame,textvariable=self.search_by_var,font=('times new roman',15,'bold'),state='readonly')
        combo_search['values']=('Name','Phno')
        combo_search.grid(row=0,column=1,padx=10,pady=10)

        txt_ser=Entry(Display_Frame,font=('times new roman',15,'bold'), textvariable=self.search_txt,bd=5,fg='black',relief=GROOVE,bg='cyan')
        txt_ser.grid(row=0,column=2,pady=20,padx=10,sticky='w')

#-----------Display button section------------------

        ser_btn=Button(Display_Frame,text='Search',command=self.search_data,width=12,font=('times new roman',10,'bold'),fg='black',bg='cyan').grid(row=1,column=0,padx=10,pady=10)
        sho_btn=Button(Display_Frame,text='Show all',command=self.fetch_data,width=12,font=('times new roman',10,'bold'),fg='black',bg='cyan').grid(row=1,column=1,padx=10,pady=10)

#-----------Database section------------------

        con=sqlite3.connect('contacts.db')
        cur=con.cursor()
        cur.execute('''create table if not exists contact(id integer primary key autoincrement, name text,phno text)''')
        con.commit()
        con.close()

#-----------Table section------------------

        Table_Frame=Frame(Display_Frame,bd=4,bg='cyan')
        Table_Frame.place(x=25,y=150,width=550,height=360)

        scrool_v=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scrool_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Contact_Table=ttk.Treeview(Table_Frame,columns=('ID','Name','phno'),xscrollcommand=scrool_v.set,yscrollcommand=scrool_y.set)
        scrool_v.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)
        scrool_v.config(command=self.Contact_Table.xview)
        scrool_y.config(command=self.Contact_Table.yview)
        self.Contact_Table.heading('ID',text='ID')
        self.Contact_Table.heading('Name',text='Name')
        self.Contact_Table.heading('phno',text='phno')

        self.Contact_Table['show']='headings'
        self.Contact_Table.column('ID',width=20)
        self.Contact_Table.column('Name',width=50)
        self.Contact_Table.column('phno',width=50)
        self.Contact_Table.pack(fill=BOTH,expand=1)
        self.Contact_Table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()


#-----------Functions section------------------

    def add_contact(self):
        if self.name_var.get()=="" or self.phno_var.get()=="":
            mb.showwarning('Error','All fields are requided')

        elif not self.phno_var.get().isnumeric():
            mb.showwarning('Error','Incorrect phno')
            
        else:
            con=sqlite3.connect('contacts.db')
            cur=con.cursor()
            sqlite_query='''insert into contact(name,phno) values(?,?)'''
            datas=(self.name_var.get(),self.phno_var.get())
            cur.execute(sqlite_query,datas)
            con.commit()
            self.fetch_data()
            self.clear_fields()
            con.close()
            mb.showinfo('Success','Contact has been Added')
    
    def fetch_data(self):

        con=sqlite3.connect('contacts.db')
        cur=con.cursor()
        sqlite_query='''select id,name,phno from contact'''
        cur.execute(sqlite_query)
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Contact_Table.delete(*self.Contact_Table.get_children())
            for row in rows:
                self.Contact_Table.insert('',END,values=row)
            con.commit()
        else:
            self.Contact_Table.delete(*self.Contact_Table.get_children())
        con.close()

    def clear_fields(self):
        self.name_var.set('')
        self.phno_var.set('')

    def get_cursor(self,event):
        cursor_row=self.Contact_Table.focus()
        contents=self.Contact_Table.item(cursor_row)
        row=contents['values']
        self.name_var.set(row[1])
        self.phno_var.set(row[2])   

    def update_contact(self):
        if self.name_var.get()=="" or self.phno_var.get()=="":
            mb.showwarning('Error','All fields are requided')

        elif not self.phno_var.get().isnumeric():
            mb.showwarning('Error','Incorrect phno')
            
        else:
            con=sqlite3.connect('contacts.db')
            cur=con.cursor()
            sqlite_query='''update contact set name=?,phno=? where id=?'''
            cursor_row=self.Contact_Table.focus()
            contents=self.Contact_Table.item(cursor_row)
            row=contents['values']
            datas=(self.name_var.get(),self.phno_var.get(),row[0])
            cur.execute(sqlite_query,datas)
            con.commit()
            self.fetch_data()
            self.clear_fields()
            con.close()
            mb.showinfo('Success','Contact has been updated')

    def delete_contact(self):
        con=sqlite3.connect('contacts.db')
        cur=con.cursor()
        cursor_row=self.Contact_Table.focus()
        contents=self.Contact_Table.item(cursor_row)
        row=contents['values']
        cur.execute('''delete from contact where id=%d''' % (row[0]))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear_fields()
        mb.showwarning('Delete','Contact deleted')

    def search_data(self):
        if self.search_txt.get()=='':
            mb.showerror('Error','Search text not found')
        else:
            con=sqlite3.connect('contacts.db')
            cur=con.cursor()
            if self.search_by_var.get()=='Name':
                cur.execute("select * from contact where name like ?", ('%'+self.search_txt.get()+'%',))
            else:
                cur.execute("select * from contact where phno like ?", ('%'+self.search_txt.get()+'%',))
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Contact_Table.delete(*self.Contact_Table.get_children())
                for row in rows:
                    self.Contact_Table.insert('',END,values=row)
                con.commit()
            else:
                mb.showerror('Error','Not found')
            con.close()
    
    # def copy_con(self):
    #     if self.phno_var.get()=='':
    #         mb.showerror('Error','No number in field')
    #     else:
    #         pyperclip.copy(phno_var.get()) 

#-----------Loop section------------------

root=Tk()
ob=Contact(root)
root.mainloop()
