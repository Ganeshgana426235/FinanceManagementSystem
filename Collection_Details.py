import datetime
from tkinter import *
from tkinter import messagebox
import HomePage
import pymysql
from datetime import datetime,timedelta
from tkcalendar import Calendar, DateEntry

mypass = "mysql"
con = pymysql.connect(host="localhost", user="root", password=mypass, database="fnb")
cur = con.cursor()


def date_modify(date_str, day, date_format="%Y-%m-%d"):
    date = datetime.strptime(date_str, date_format)
    one_day = timedelta(days=day)
    new_date = date + one_day
    new_date_str = new_date.strftime(date_format)
    return new_date_str
def addcollections(collection_id_Field, loan_id_Field, cust_id_Field, total_amount_received_Field, payment_mode_Field, payment_received_date_Field, transaction_details_Field):
    collection_id = collection_id_Field.get()
    loan_id = loan_id_Field.get()
    cust_id = cust_id_Field.get()
    no_of_installments_paying = 0
    total_amount_received = total_amount_received_Field.get()
    payment_mode = payment_mode_Field.get()
    payment_received_date= payment_received_date_Field.get_date()
    transaction_details= transaction_details_Field.get()

    if payment_mode == "":
        payment_mode = "null"
    if payment_received_date == "":
        payment_received_date = "null"
    if transaction_details == "":
        transaction_details = "null"

    if collection_id == "" or loan_id == "" or cust_id == "" or no_of_installments_paying == "" or total_amount_received == "" or payment_mode == "" or payment_received_date == "" or transaction_details == "":
        messagebox.showinfo(title="Empty Field", message="Enter all requried Fields")
    else:
        try:
            cur.execute("select amount_per_installment,advanced_payment_recieved,no_of_installments_paid,next_installment_date from loan_details where loan_id=%s", loan_id)
            va = cur.fetchone()
            total_amount_received1 = int(total_amount_received)+int(va[1])
            no_of_installments_paying = total_amount_received1//va[0]
            adv_amount = total_amount_received1 % va[0]
            status = 1
            if no_of_installments_paying+va[2] >= 120:
                status = 0
                loanmessage = "Loan Closed Successfully"
            else:
                status = 1
                loanmessage = "Loan Paid Successfully"
            next_installment_date = date_modify(str(va[3]), no_of_installments_paying)

            insertl = "update loan_details set advanced_payment_recieved = %s,no_of_installments_paid = %s,next_installment_date = %s,loan_status = %s where loan_id = %s"
            vals = (adv_amount, no_of_installments_paying+va[2],next_installment_date,status, loan_id)
            cur.execute(insertl, vals)
            insertque = "insert into collections (collection_id, loan_id, cust_id,no_of_installments_paying,total_amount_received,payment_mode,payment_received_date,transaction_details) value(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (collection_id, loan_id, cust_id, no_of_installments_paying, total_amount_received, payment_mode, payment_received_date, transaction_details)
            cur.execute(insertque, values)
            con.commit()
            messagebox.showinfo(title="sucessfully", message=loanmessage)
        except:
            cur.execute("select collection_id from collections where collection_id ='%s'" % (collection_id))
            v = cur.fetchone()
            if v[0] == collection_id:
                messagebox.showinfo("Id Error", "collection record already exists ")

def collection_window():
    global collections_frame
    collections_frame = Frame(mainwindow, width=800, height=500)
    collections_frame.place(relx=0.22, rely=0.07, relwidth=1, relheight=1)
    t_label = Label(collections_frame, text="Collection details", fg="blue", font=("bold", 16))
    t_label.place(relx=0.2, rely=0.0, relheight=0.04)


    collection_id_label = Label(collections_frame, text="Collection ID", font=("arial", 12))
    collection_id_label.place(relx=0.0, rely=0.05, relheight=0.04)
    collection_id_Field = Entry(collections_frame, font=("bold", 14))
    collection_id_Field.place(relx=0.25, rely=0.05, relwidth=0.4, relheight=0.04)

    loan_id_label = Label(collections_frame, text="Loan ID :", font=("arial", 12))
    loan_id_label.place(relx=0.0, rely=0.10, relheight=0.04)
    loan_id_Field = Entry(collections_frame, width=25, font=("bold", 14))
    loan_id_Field.place(relx=0.25, rely=0.10, relwidth=0.4, relheight=0.04)

    cust_id_label = Label(collections_frame, text="Customer ID", font=("arial", 12))
    cust_id_label.place(relx=0.0, rely=0.15, relheight=0.04)
    cust_id_Field = Entry(collections_frame, width=25, font=("bold", 14))
    cust_id_Field.place(relx=0.25, rely=0.15, relwidth=0.4, relheight=0.04)

    #no_of_installments_paying_label = Label(collections_frame, text="No.of installments paying", font=("arial", 12))
    #no_of_installments_paying_label.place(relx=0.0, rely=0.20, relheight=0.04)
    #no_of_installments_paying_Field = Entry(collections_frame, text="N0 0f installments paying")
    #no_of_installments_paying_Field.place(relx=0.25, rely=0.20, relwidth=0.4, relheight=0.04)

    total_amount_received_label = Label(collections_frame, text="Total Amount Received", font=("arial", 12))
    total_amount_received_label.place(relx=0.0, rely=0.20, relheight=0.04)
    total_amount_received_Field = Entry(collections_frame, width=25, font=("bold", 14))
    total_amount_received_Field.place(relx=0.25, rely=0.20, relwidth=0.4, relheight=0.04)

    payment_mode_label = Label(collections_frame, text="Payment Mode", font=("arial", 12))
    payment_mode_label.place(relx=0.0, rely=0.25, relheight=0.04)
    payment_mode_Field = Entry(collections_frame, width=25, font=("bold", 14))
    payment_mode_Field.place(relx=0.25, rely=0.25, relwidth=0.4, relheight=0.04)

    payment_received_date_label = Label(collections_frame, text="Payment Received Date:", font=("arial", 12))
    payment_received_date_label.place(relx=0.0, rely=0.30, relheight=0.04)
    payment_received_date_Field = DateEntry(collections_frame, text="Payment Received Date")
    payment_received_date_Field.place(relx=0.25, rely=0.30, relwidth=0.4, relheight=0.04)

    transaction_details_label = Label(collections_frame, text="Transcation Details", font=("arial", 12))
    transaction_details_label.place(relx=0.0, rely=0.35, relheight=0.04)
    transaction_details_Field = Entry(collections_frame)
    transaction_details_Field.place(relx=0.25, rely=0.35, relwidth=0.4, relheight=0.04)

    Add_collection_button = Button(collections_frame, text="Add Collection", width=15, bg="light green",command= lambda : addcollections(collection_id_Field, loan_id_Field, cust_id_Field,total_amount_received_Field, payment_mode_Field, payment_received_date_Field, transaction_details_Field))
    Add_collection_button.place(relx=0.2, rely=0.75, relwidth=0.4, relheight=0.04)
    back_button = Button(collections_frame, text="Quit", width=15, bg="light blue", command=collections_frame.destroy)
    back_button.place(relx=0.2, rely=0.82, relwidth=0.4, relheight=0.04)







def loginsucess(window):
    global searchField,login_frame2,mainwindow
    mainwindow = window
    login_frame2 = Frame(mainwindow, width=1500, height=35, highlightbackground='gray', highlightthicknes=1)
    login_frame2.place(relx=0, rely=0, relwidth=1, relheight=1)
    new_user = Button(login_frame2, text="New Collection", font=("bold", 12), command=collection_window)
    new_user.place(relx=0, rely=0, relwidth=0.14, relheight=0.04)
    search_label = Label(login_frame2, text="Enter Customer ID or Name To Find:", font=("arial", 12))
    search_label.place(relx=0.15, rely=0, relwidth=0.35, relheight=0.04)
    searchField = Entry(login_frame2, width=25, font=("bold", 14))
    searchField.place(relx=0.48, rely=0, relwidth=0.4, relheight=0.04)
    search_button = Button(login_frame2, text="Search", width=7, height=1, font=("bold", 12))
    search_button.place(relx=0.89, rely=0, relwidth=0.1, relheight=0.04)
    back_home = Button(login_frame2, text="Back", width=7, height=1, bg="light blue", font=("bold", 12),
                          command= login_frame2.destroy)
    back_home.place(relx=0.25, rely=0.9, relwidth=0.5, relheight=0.04)
