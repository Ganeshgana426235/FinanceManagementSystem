import tkinter as tk
import HomePage
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkcalendar import Calendar, DateEntry
from datetime import datetime

mypass = "mysql"
con = pymysql.connect(host="localhost", user="root", password=mypass, database="fnb")
cur = con.cursor()

def addguarantor(gua_id_Field, cust_id_Field, guarantor_name_Field, guarantor_mobile_Field, guarantor_aadhar_Field, guarantor_pancard_Field, relationship_Field):
    gua_id = gua_id_Field.get()
    cust_id = cust_id_Field.get()
    guarantor_name = guarantor_name_Field.get()
    guarantor_mobile = guarantor_mobile_Field.get()
    guarantor_aadhar = guarantor_aadhar_Field.get()
    guarantor_pancard= guarantor_pancard_Field.get()
    relationship     = relationship_Field.get()
    if gua_id == "":
        gua_id = "null"
    if cust_id == "":
        cust_id = "null"
    if guarantor_name == "":
        guarantor_name = "null"
    if guarantor_mobile == "":
        guarantor_mobile= "null"
    if guarantor_aadhar == "":
        guarantor_aadhar = "null"
    if guarantor_pancard == "":
        guarantor_pancard = "null"
    if relationship == "":
        relationship = "null"
        messagebox.showinfo("Empty Field", "Enter all required fields")
    else:
        try:
            insert1 = "insert into guarantor (gua_id,cust_id,guarantor_name,guarantor_mobile,guarantor_aadhar,guarantor_pancard,relationship) value (%s,%s,%s,%s,%s,%s,%s)"
            values = (gua_id,cust_id,guarantor_name,guarantor_mobile,guarantor_aadhar,guarantor_pancard,relationship)
            cur.execute(insert1, values)
            con.commit()
            messagebox.showinfo("Sucessfull","Guarantor Inserted sucessfully")
        except:
            cur.execute("select gua_id from guarantor where cust_id='%s'" % (gua_id))
            v = cur.fetchone()
            if int(v[0]) == int(cust_id):
                messagebox.showinfo("ID ERROR", "ID already Exists")
def Modifyguarantor(gua_id, cust_id_Field, guarantor_name_Field,guarantor_mobile_Field, guarantor_aadhar_Field,guarantor_pancard_Field, relationship_Field):
    cust_id_ = cust_id_Field.get()
    guarantor_name = guarantor_name_Field.get()
    guarantor_mobile = guarantor_mobile_Field.get()
    guarantor_aadhar = guarantor_aadhar_Field.get()
    guarantor_pancard = guarantor_pancard_Field.get()
    relationship = relationship_Field.get()

    if gua_id == "":
        gua_id = "null"
    if cust_id_ == "":
        cust_id_ = "null"
    if guarantor_name == "":
        guarantor_name = "null"
    if guarantor_mobile == "":
        guarantor_mobile = "null"
    if guarantor_aadhar == "":
        guarantor_aadhar = "null"
    if guarantor_pancard == "":
        guarantor_pancard = "null"
    if relationship == "":
        relationship = "null"
    try:
        insert4 = "update guarantor set cust_id = %s, guarantor_name = %s, guarantor_mobile = %s, guarantor_aadhar = %s, guarantor_pancard = %s, relationship= %s where gua_id=%s"
        values4 = ( cust_id_, guarantor_name, guarantor_mobile, guarantor_aadhar, guarantor_pancard, relationship,gua_id)
        cur.execute(insert4, values4)
        con.commit()
        modify_guarantor.destroy()
        messagebox.showinfo("Sucessfull", "guarantor updated sucessfully")
    except:
        messagebox.showinfo("Unsucess", "Guarantor Not Updated")




def modifyguarantor():
    selected_guarantors = [var.get() for var in checkboxs]
    global modify_gua,modify_guarantor
    if selected_guarantors.count(1)==1:
        try:
            cur.execute("select * from guarantor where gua_id = '%s'"%(int(selected_guarantor[selected_guarantors.index(1)])))
            modify_gua = cur.fetchone()
        except:
            pass
        modify_guarantor = Toplevel()
        modify_guarantor.title("Modify Guarantor")
        modify_guarantor.geometry("800x600")
        t_label = Label(modify_guarantor, text="Enter guarantor details", fg="blue", font=("bold", 16))
        t_label.place(relx=0.2, rely=0.0, relheight=0.04)
        gua_id_label = Label(modify_guarantor, text="GUARANTOR ID  :", font=("arial", 12))
        gua_id_label.place(relx=0.0, rely=0.05, relheight=0.04)
        gua_id_Field = Entry(modify_guarantor, font=("bold", 14))
        gua_id_Field.place(relx=0.25, rely=0.05, relwidth=0.4, relheight=0.04)
        gua_id_Field.insert(0,modify_gua[0])
        cust_id_label = Label(modify_guarantor, text="Customer ID :", font=("arial", 12))
        cust_id_label.place(relx=0.0, rely=0.10, relheight=0.04)
        cust_id_Field = Entry(modify_guarantor, width=25, font=("bold", 14))
        cust_id_Field.place(relx=0.25, rely=0.10, relwidth=0.4, relheight=0.04)
        cust_id_Field.insert(0, modify_gua[1])
        guarantor_name_label = Label(modify_guarantor, text="GUARANTOR NAME:", font=("arial", 12))
        guarantor_name_label.place(relx=0.0, rely=0.15, relheight=0.04)
        guarantor_name_Field = Entry(modify_guarantor, width=25, font=("bold", 14))
        guarantor_name_Field.place(relx=0.25, rely=0.15, relwidth=0.4, relheight=0.04)
        guarantor_name_Field.insert(0,modify_gua[2])
        guarantor_mobile_label = Label(modify_guarantor, text="GUARANTOR MOBILE:", font=("arial", 12))
        guarantor_mobile_label.place(relx=0.0, rely=0.20, relheight=0.04)
        guarantor_mobile_Field = Entry(modify_guarantor, width=25, font=("bold", 14))
        guarantor_mobile_Field.place(relx=0.25, rely=0.20, relwidth=0.4, relheight=0.04)
        guarantor_mobile_Field.insert(0,modify_gua[3])
        guarantor_aadhar_label = Label(modify_guarantor, text="GUARANTOR AADHAR :", font=("arial", 12))
        guarantor_aadhar_label.place(relx=0.0, rely=0.25, relheight=0.04)
        guarantor_aadhar_Field = Entry(modify_guarantor, width=25, font=("bold", 14))
        guarantor_aadhar_Field.place(relx=0.25, rely=0.25, relwidth=0.4, relheight=0.04)
        guarantor_aadhar_Field.insert(0,modify_gua[4])
        guarantor_pancard_label = Label(modify_guarantor, text="GUARANTOR PANCARD :", font=("arial", 12))
        guarantor_pancard_label.place(relx=0.0, rely=0.30, relheight=0.04)
        guarantor_pancard_Field = Entry(modify_guarantor, width=25, font=("bold", 14))
        guarantor_pancard_Field.place(relx=0.25, rely=0.30, relwidth=0.4, relheight=0.04)
        guarantor_pancard_Field.insert(0,modify_gua[5])
        relationship_label = Label(modify_guarantor, text="RELATIONSHIP :", font=("arial", 12))
        relationship_label.place(relx=0.0, rely=0.35, relheight=0.04)
        relationship_Field = Entry(modify_guarantor, width=25, font=("bold", 14))
        relationship_Field.place(relx=0.25, rely=0.35, relwidth=0.4, relheight=0.04)
        relationship_Field.insert(0,modify_gua[6])
        Add_user_button = Button(modify_guarantor, text="Modify Guarantor", width=15, bg="light green",
                                 command=lambda: Modifyguarantor(modify_gua[0], cust_id_Field, guarantor_name_Field,guarantor_mobile_Field, guarantor_aadhar_Field,guarantor_pancard_Field, relationship_Field))
        Add_user_button.place(relx=0.2, rely=0.75, relwidth=0.4, relheight=0.04)
        back_button = Button(modify_guarantor, text="Back", width=15, bg="light blue", command=modify_guarantor.destroy)
        back_button.place(relx=0.2, rely=0.85, relwidth=0.4, relheight=0.04)

def search():
    global guarantor_details, checkboxs, values, selected_guarantor
    selected_guarantor=[]
    checkboxs=[]
    gua_id_name = searchField.get()
    if gua_id_name == "":
        messagebox.showinfo("Error", "Enter guarantor details to find")
    else:
        try:
            try:
                new_guarantor_frame.destroy()
            except:
                pass
            cur.execute("select * from guarantor where gua_id='%s' or guarantor_name='%s' or cust_id='%s'"%(gua_id_name,gua_id_name,gua_id_name))
            guarantor_details = Frame(mainwindow , width=800,height=500)
            guarantor_details.place(relx=0.0,rely=0.07,relwidth=1, relheight=1)
            id_label = Label(guarantor_details, width=10, text='GUA_ID', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            id_label.place(relx=0.15, rely=0.05,relwidth=0.1, relheight=0.04)
            e = Label(guarantor_details, width=15, text='CUST_ID', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.place(relx=0.25, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(guarantor_details, width=15, text='GUARANTOR_NAME', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.place(relx=0.35, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(guarantor_details, width=10, text='GUARANTOR_MOBILE', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.place(relx=0.45, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(guarantor_details, width=10, text='GUARANTOR_AADHAR', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.place(relx=0.55, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(guarantor_details, width=10, text='GUARANTOR_PANCARD', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.place(relx=0.65, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(guarantor_details, width=10, text='RELATIONSHIP', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.place(relx=0.75, rely=0.05,relwidth=0.1, relheight=0.04)
            i = 1
            k = 0
            rx=0.15
            rdx = rx
            ry = 0.1
            k=0
            for values in cur:
                var = IntVar()
                checkboxs.append(var)
                checkbox = tk.Checkbutton(guarantor_details, variable=var)
                checkbox.place(relx=0.05,rely=ry ,relwidth=0.1, relheight=0.04)
                selected_guarantor.append(values[0])
                for j in range(7):
                    l = Label(guarantor_details, text=values[j], borderwidth=2, relief='ridge', anchor='w')
                    l.place(relx=rx, rely=ry,relwidth=0.1, relheight=0.04)
                    rx = rx+0.10
                ry = ry+0.05
                rx = rdx
            modify_button = Button(guarantor_details,text="Modify",width=15,bg="light green",command= modifyguarantor)
            modify_button.place(relx=0.1, rely=0.75, relwidth=0.25, relheight=0.04)
            delete_button = Button(guarantor_details, text="Delete", width=15, bg="red")
            delete_button.place(relx=0.6, rely=0.75, relwidth=0.25, relheight=0.04)
            back_button = Button(guarantor_details, text="Back", width=15, bg="light blue", command=guarantor_details.destroy)
            back_button.place(relx=0.25, rely=0.85, relwidth=0.5, relheight=0.04)
        except:
            pass

def new_guarantor_window():
    try:
        guarantor_details.destroy()
    except:
        pass
    global new_guarantor_frame
    new_guarantor_frame = Frame(mainwindow, width=800, height=500)
    new_guarantor_frame.place(relx=0.22, rely=0.07, relwidth=1, relheight=1)
    t_label = Label(new_guarantor_frame, text="Enter guarantor details", fg="blue", font=("bold", 16))
    t_label.place(relx=0.2, rely=0.0, relheight=0.04)
    gua_id_label = Label(new_guarantor_frame, text="GUARANTOR ID  :", font=("arial", 12))
    gua_id_label.place(relx=0.0, rely=0.05, relheight=0.04)
    gua_id_Field = Entry(new_guarantor_frame, font=("bold", 14))
    gua_id_Field.place(relx=0.25, rely=0.05, relwidth=0.4, relheight=0.04)
    cust_id_label = Label(new_guarantor_frame, text="Customer ID :", font=("arial", 12))
    cust_id_label.place(relx=0.0, rely=0.10, relheight=0.04)
    cust_id_Field = Entry(new_guarantor_frame, width=25, font=("bold", 14))
    cust_id_Field.place(relx=0.25, rely=0.10, relwidth=0.4, relheight=0.04)
    guarantor_name_label = Label(new_guarantor_frame, text="GUARANTOR NAME:", font=("arial", 12))
    guarantor_name_label.place(relx=0.0, rely=0.15, relheight=0.04)
    guarantor_name_Field = Entry(new_guarantor_frame, width=25, font=("bold", 14))
    guarantor_name_Field.place(relx=0.25, rely=0.15, relwidth=0.4, relheight=0.04)
    guarantor_mobile_label = Label(new_guarantor_frame, text="GUARANTOR MOBILE:", font=("arial", 12))
    guarantor_mobile_label.place(relx=0.0, rely=0.20, relheight=0.04)
    guarantor_mobile_Field = Entry(new_guarantor_frame, width=25, font=("bold", 14))
    guarantor_mobile_Field.place(relx=0.25, rely=0.20, relwidth=0.4, relheight=0.04)
    guarantor_aadhar_label = Label(new_guarantor_frame, text="GUARANTOR AADHAR :", font=("arial", 12))
    guarantor_aadhar_label.place(relx=0.0, rely=0.25, relheight=0.04)
    guarantor_aadhar_Field = Entry(new_guarantor_frame, width=25, font=("bold", 14))
    guarantor_aadhar_Field.place(relx=0.25, rely=0.25, relwidth=0.4, relheight=0.04)
    guarantor_pancard_label = Label(new_guarantor_frame, text="GUARANTOR PANCARD :", font=("arial", 12))
    guarantor_pancard_label.place(relx=0.0, rely=0.30, relheight=0.04)
    guarantor_pancard_Field = Entry(new_guarantor_frame, width=25, font=("bold", 14))
    guarantor_pancard_Field.place(relx=0.25, rely=0.30, relwidth=0.4, relheight=0.04)
    relationship_label = Label(new_guarantor_frame, text="RELATIONSHIP :", font=("arial", 12))
    relationship_label.place(relx=0.0, rely=0.35, relheight=0.04)
    relationship_Field = Entry(new_guarantor_frame, width=25, font=("bold", 14))
    relationship_Field.place(relx=0.25, rely=0.35, relwidth=0.4, relheight=0.04)

    Add_user_button = Button(new_guarantor_frame, text="Add Guarantor", width=15, bg="light green",
                             command=lambda: addguarantor(gua_id_Field,cust_id_Field,guarantor_name_Field,guarantor_mobile_Field,guarantor_aadhar_Field,
                                                     guarantor_pancard_Field,relationship_Field))
    Add_user_button.place(relx=0.2, rely=0.75, relwidth=0.4, relheight=0.04)
    back_button = Button(new_guarantor_frame, text="Back", width=15, bg="light blue", command=new_guarantor_frame.destroy)
    back_button.place(relx=0.2, rely=0.85, relwidth=0.4, relheight=0.04)

def loginsucess(mainwindow5):
    global searchField,login_frame2,mainwindow
    mainwindow=mainwindow5
    login_frame2 = Frame(mainwindow, width=1500, height=35, highlightbackground='gray', highlightthicknes=1)
    login_frame2.place(relx=0, rely=0, relwidth=1, relheight=1)
    new_user = Button(login_frame2, text="New Guarantor", font=("bold", 12), command=new_guarantor_window)
    new_user.place(relx=0, rely=0, relwidth=0.14, relheight=0.04)
    search_label = Label(login_frame2, text="Enter guarantor id or name to find:", font=("arial", 12))
    search_label.place(relx=0.15, rely=0, relwidth=0.35, relheight=0.04)
    searchField = Entry(login_frame2, width=25, font=("bold", 14))
    searchField.place(relx=0.48, rely=0, relwidth=0.4, relheight=0.04)
    search_button = tk.Button(login_frame2, text="Search", width=7, height=1, font=("bold", 12), command=search)
    search_button.place(relx=0.89, rely=0, relwidth=0.1, relheight=0.04)
    back_home = tk.Button(login_frame2, text="Back", width=7, height=1, bg="light blue", font=("bold", 12),
                          command=lambda: HomePage.Home(mainwindow))
    back_home.place(relx=0.25, rely=0.9, relwidth=0.5, relheight=0.04)


