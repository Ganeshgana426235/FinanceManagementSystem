import tkinter as tk
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta
import HomePage

mypass = "mysql"
con = pymysql.connect(host="localhost", user="root", password=mypass, database="fnb")
cur = con.cursor()
def date_modify(date_str, day, date_format="%Y-%m-%d"):
    date = datetime.strptime(date_str, date_format)
    one_day = timedelta(days=day)
    new_date = date + one_day
    new_date_str = new_date.strftime(date_format)
    return new_date_str
def AddLoandeatils(loan_id_field, cust_id_Field, gua_id_Field,loan_type_Field, loan_amount_Field,loan_approved_date_field, status_Field):
    loan_id = loan_id_field.get()
    cust_id = cust_id_Field.get()
    gua_id = gua_id_Field.get()
    loan_type = loan_type_Field.get()
    loan_amount = int(loan_amount_Field.get())
    interest_rate = 0.6
    loan_approved_date = loan_approved_date_field.get_date()
    total_no_of_installments = 120
    loan_approved_date = datetime.strftime(loan_approved_date, "%Y-%m-%d")
    #loan_approved_date = loan_approved_date.replace("-","")
    no_installments_paid = 0
    amount_per_installment = ((int(loan_amount)*interest_rate*(4/12))+loan_amount)/total_no_of_installments
    advanced_payment_recieved =0
    over_dues = 0
    next_installment_date = date_modify(str(loan_approved_date), 1)
    #next_installment_date = next_installment_date.replace("-","")
    loan_closing_date = date_modify(str(loan_approved_date),120)
    #loan_closing_date = loan_closing_date.replace("-","")
    status = status_Field.get()

    try:
        insert3 = "insert into loan_details (loan_id,cust_id,gua_id,loan_type,loan_amount,interest_rate,loan_approved_date,total_no_of_installments,no_of_installments_paid,amount_per_installment,advanced_payment_recieved,over_dues,next_installment_date,loan_closing_date,loan_status) value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values3 = (loan_id, cust_id, gua_id, loan_type, loan_amount, interest_rate, loan_approved_date, total_no_of_installments,no_installments_paid,amount_per_installment, advanced_payment_recieved,over_dues,next_installment_date,loan_closing_date,status)
        cur.execute(insert3, values3)
        con.commit()
        messagebox.showinfo("Successful", "Loan Details Inserted successfully")

    except:
        cur.execute("select loan_id from loan_details where loan_id = '%s'" % (loan_id))
        m = cur.fetchone()
        print(m)
        try:
            if int(m[0]) == int(loan_id):
                messagebox.showinfo("Id Error", "Loan Details ID already exists ")
        except:
            messagebox.showinfo("Error", "Enter Details correctly")
def modifyLoanDetails(loan_id, cust_id_Field, gua_id_Field, loan_type_Field,loan_amount_Field, interest_rate_field,loan_start_date_field,t_n_i_pfield,status_Field):
    cust_id = cust_id_Field.get()
    gua_id = gua_id_Field.get()
    loan_type = loan_type_Field.get()
    loan_start_date = loan_start_date_field.get_date()
    loan_amount1 = loan_amount_Field.get()
    loan_amount = float(loan_amount1)
    interest_rate = 0.6
    status = status_Field.get()
    total_no_of_installments = 120
    no_installments_paid = t_n_i_pfield.get()
    amount_per_installment = ((loan_amount * interest_rate * (4 / 12)) + loan_amount) / total_no_of_installments
    loan_approved_date = datetime.strftime(loan_start_date, "%y-%m-%d")
    loan_closing_date = date_modify(str(loan_approved_date), 120)
    if status == "":
        status = 0
    if loan_id == "":
        messagebox.showinfo("Empty Values", "Enter All Required Details correctly")
    else:
        try:
            update_query = "update loan_details set cust_id = %s, gua_id = %s, loan_type = %s, loan_amount = %s,interest_rate = %s, no_of_installments_paid =%s,amount_per_installment =%s ,loan_approved_date = %s,  loan_closing_date = %s, status = %s where loan_id=%s"
            update_value = (cust_id, gua_id, loan_type,loan_amount, interest_rate,no_installments_paid,amount_per_installment,loan_approved_date, loan_closing_date, status,cust_id)
            cur.execute(update_query, update_value)
            con.commit()
            modify_loan.destroy()
            messagebox.showinfo("Successful", "Customer updated successfully")
        except:
            messagebox.showinfo("UnSuccess", "Customer Not updated ")


def addcollections_loan(collection_id_Field, loan_id_Field, cust_id_Field, total_amount_received_Field, payment_mode_Field, payment_received_date_Field, transaction_details_Field):
    collection_id = collection_id_Field.get()
    loan_id = loan_id_Field
    cust_id = cust_id_Field
    no_of_installments_paying = 0
    total_amount_received = total_amount_received_Field.get()
    payment_mode = payment_mode_Field.get()
    payment_received_date = payment_received_date_Field.get_date()
    transaction_details = transaction_details_Field.get()

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
                loanmessage = "Loan Closed Successfully "
            else:
                status = 1
                loanmessage = "Loan Paid Successfully "
            next_installment_date = date_modify(str(va[3]),no_of_installments_paying)

            insertl = "update loan_details set advanced_payment_recieved = %s,no_of_installments_paid = %s,next_installment_date=%s, loan_status = %s where loan_id = %s"
            vals = (adv_amount, no_of_installments_paying+va[2],next_installment_date,status, loan_id)
            cur.execute(insertl, vals)

            insertque = "insert into collections (collection_id, loan_id, cust_id,no_of_installments_paying,total_amount_received,payment_mode,payment_received_date,transaction_details) value(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (collection_id, loan_id, cust_id, no_of_installments_paying, total_amount_received, payment_mode, payment_received_date, transaction_details)
            cur.execute(insertque, values)
            con.commit()
            messagebox.showinfo(title="sucessfully", message=loanmessage)
            try:
                collections_frame.destroy()
            except:
                pass

        except:
            cur.execute("select collection_id from collections where collection_id ='%s'" % (collection_id))
            v = cur.fetchone()
            if v[0] == collection_id:
                messagebox.showinfo("Id Error", "collection record already exists ")

def collection_window_loan():
    selected_loan_detail = [var.get() for var in checkboxs]
    global modify_values, modify_loan
    if selected_loan_detail.count(1) == 1:
        try:
            cur.execute("select * from loan_details where loan_id = '%s' " % (str(selected_loan_details[selected_loan_detail.index(1)])))
            modify_values = cur.fetchone()
        except:
            pass
    global collections_frame
    collections_frame = Toplevel()
    collections_frame.title("Pay Loan")
    collections_frame.geometry("800x600")
    t_label = Label(collections_frame, text="Collection Details", fg="blue", font=("bold", 16))
    t_label.place(relx=0.2, rely=0.0, relheight=0.04)


    collection_id_label = Label(collections_frame, text="Collection ID", font=("arial", 12))
    collection_id_label.place(relx=0.2, rely=0.05, relheight=0.04)
    collection_id_Field = Entry(collections_frame, font=("bold", 14))
    collection_id_Field.place(relx=0.5, rely=0.05, relwidth=0.4, relheight=0.04)

    loan_id_label = Label(collections_frame, text="Loan ID :", font=("arial", 12))
    loan_id_label.place(relx=0.2, rely=0.10, relheight=0.04)
    loan_id_Field = Label(collections_frame, text=modify_values[0],fg="green", font=("arial", 12))
    loan_id_Field.place(relx=0.5, rely=0.10, relwidth=0.4, relheight=0.04)

    cust_id_label = Label(collections_frame, text="Customer ID", font=("arial", 12))
    cust_id_label.place(relx=0.2, rely=0.15, relheight=0.04)
    cust_id_Field = Label(collections_frame, text=modify_values[1],fg="green", font=("arial", 12))
    cust_id_Field.place(relx=0.5, rely=0.15, relwidth=0.4, relheight=0.04)

    #no_of_installments_paying_label = Label(collections_frame, text="No.of installments paying", font=("arial", 12))
    #no_of_installments_paying_label.place(relx=0.2, rely=0.20, relheight=0.04)
    #no_of_installments_paying_Field = Entry(collections_frame, text="N0 0f installments paying",font=("bold",12))
    #no_of_installments_paying_Field.place(relx=0.5, rely=0.20, relwidth=0.4, relheight=0.04)

    total_amount_received_label = Label(collections_frame, text="Total Amount Received", font=("arial", 12))
    total_amount_received_label.place(relx=0.2, rely=0.20, relheight=0.04)
    total_amount_received_Field = Entry(collections_frame, width=25, font=("bold", 14))
    total_amount_received_Field.place(relx=0.5, rely=0.20, relwidth=0.4, relheight=0.04)

    payment_mode_label = Label(collections_frame, text="Payment Mode", font=("arial", 12))
    payment_mode_label.place(relx=0.2, rely=0.25, relheight=0.04)
    payment_mode_Field = Entry(collections_frame, width=25, font=("bold", 14))
    payment_mode_Field.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.04)

    payment_received_date_label = Label(collections_frame, text="Payment Received Date:", font=("arial", 12))
    payment_received_date_label.place(relx=0.2, rely=0.30, relheight=0.04)
    payment_received_date_Field = DateEntry(collections_frame)
    payment_received_date_Field.place(relx=0.5, rely=0.30, relwidth=0.4, relheight=0.04)

    transaction_details_label = Label(collections_frame, text="Transcation Details", font=("arial", 12))
    transaction_details_label.place(relx=0.2, rely=0.35, relheight=0.04)
    transaction_details_Field = Entry(collections_frame, font=("bold",12))
    transaction_details_Field.place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.04)

    Add_collection_button = Button(collections_frame, text="Add Collection", width=15, bg="light green",command= lambda : addcollections_loan(collection_id_Field, modify_values[0], modify_values[1], total_amount_received_Field, payment_mode_Field, payment_received_date_Field, transaction_details_Field))
    Add_collection_button.place(relx=0.2, rely=0.75, relwidth=0.4, relheight=0.04)
    back_button = Button(collections_frame, text="Quit", width=15, bg="light blue", command=collections_frame.destroy)
    back_button.place(relx=0.2, rely=0.82, relwidth=0.4, relheight=0.04)

def modifyLoanDetailsFrame():
    selected_loan_detail = [var.get() for var in checkboxs]
    global modify_values, modify_loan
    if selected_loan_detail.count(1) == 1:
        try:
            cur.execute("select * from loan_details where loan_id = '%s' " %(str(selected_loan_details[selected_loan_detail.index(1)])))
            modify_values = cur.fetchone()
        except:
            pass
        modify_loan = Toplevel()
        modify_loan.title("modify customer details")
        modify_loan.geometry("800x600")
        t_label = Label(modify_loan, text="Enter Loan details to modify", fg="blue", font=("bold", 16))
        t_label.place(relx=0.2, rely=0.0, relheight=0.04)
        loan_id_label = Label(modify_loan, text="Loan ID  :", font=("arial", 12))
        loan_id_label.place(relx=0.2, rely=0.05, relheight=0.04)
        loan_id_field = Label(modify_loan, text=modify_values[0], font=("arial", 12))
        loan_id_field.place(relx=0.4, rely=0.05, relwidth=0.4, relheight=0.04)
        cust_id_label = Label(modify_loan, text="Customer ID :", font=("arial", 12))
        cust_id_label.place(relx=0.2, rely=0.10, relheight=0.04)
        cust_id_Field = Entry(modify_loan, width=25, font=("bold", 14))
        cust_id_Field.place(relx=0.4, rely=0.10, relwidth=0.4, relheight=0.04)
        cust_id_Field.insert(0, modify_values[1])
        gua_id_label = Label(modify_loan, text="Guarantor ID:", font=("arial", 12))
        gua_id_label.place(relx=0.2, rely=0.15, relheight=0.04)
        gua_id_Field = Entry(modify_loan, width=25, font=("bold", 14))
        gua_id_Field.place(relx=0.4, rely=0.15, relwidth=0.4, relheight=0.04)
        gua_id_Field.insert(0, modify_values[2])
        loan_type_label = Label(modify_loan, text="Loan Type:", font=("arial", 12))
        loan_type_label.place(relx=0.2, rely=0.20, relheight=0.04)
        loan_type_Field = Entry(modify_loan, width=25, font=("bold", 14))
        loan_type_Field.insert(0, modify_values[3])
        loan_type_Field.place(relx=0.4, rely=0.20, relwidth=0.4, relheight=0.04)
        loan_amount_label = Label(modify_loan, text="Loan Amount :", font=("arial", 12))
        loan_amount_label.place(relx=0.2, rely=0.25, relheight=0.04)
        loan_amount_Field = Entry(modify_loan, width=25, font=("bold", 14))
        loan_amount_Field.place(relx=0.4, rely=0.25, relwidth=0.4, relheight=0.04)
        loan_amount_Field.insert(0, modify_values[4])
        interest_rate_label = Label(modify_loan, text="Interest Rate :", font=("arial", 12))
        interest_rate_label.place(relx=0.2, rely=0.30, relheight=0.04)
        interest_rate_field = Entry(modify_loan, width=25, font=("bold", 14))
        interest_rate_field.place(relx=0.4, rely=0.30, relwidth=0.4, relheight=0.04)
        interest_rate_field.insert(0, modify_values[5])
        loan_start_date_label = Label(modify_loan, text=" Loan Approved Date :", font=("arial", 12))
        loan_start_date_label.place(relx=0.2, rely=0.35, relheight=0.04)
        loan_start_date_field = DateEntry(modify_loan)
        loan_start_date_field.place(relx=0.4, rely=0.35, relwidth=0.4, relheight=0.04)
        loan_start_date_field.set_date(modify_values[6])


        t_n_i_plabel = Label(modify_loan, text="No Of Installments Paid:", font=("arial", 12))
        t_n_i_plabel.place(relx=0.2, rely=0.40, relheight=0.04)
        t_n_i_pfield = Entry(modify_loan, width=25, font=("bold", 14))
        t_n_i_pfield.place(relx=0.4, rely=0.40, relwidth=0.4, relheight=0.04)
        t_n_i_pfield.insert(0, modify_values[8])


        status_label = Label(modify_loan, text="Loan Status:", font=("arial", 12))
        status_label.place(relx=0.2, rely=0.45, relheight=0.04)
        status_Field = Entry(modify_loan, width=25, font=("bold", 14))
        status_Field.place(relx=0.4, rely=0.45, relwidth=0.4, relheight=0.04)
        status_Field.insert(0, modify_values[14])

        Add_LoanDetails_button = Button(modify_loan, text="Modify User", width=15, bg="light green", command=lambda: modifyLoanDetails(modify_values[0], cust_id_Field, gua_id_Field, loan_type_Field,loan_amount_Field, interest_rate_field,loan_start_date_field,t_n_i_pfield, status_Field))
        Add_LoanDetails_button.place(relx=0.4, rely=0.75, relwidth=0.4, relheight=0.04)
        back_button = Button(modify_loan, text="Quit", width=15, bg="light blue", command=modify_loan.destroy)
        back_button.place(relx=0.4, rely=0.82, relwidth=0.4, relheight=0.04)
    elif selected_loan_detail.count(1) == 0:
        messagebox.showinfo("Select Error", "select one Loan Details to modify")
    else:
        messagebox.showinfo("Select Error", "Select only one Loan details at a time")

def search_loan():
    global loan_details, checkboxs, values, selected_loan_details
    selected_loan_details = []
    checkboxs = []
    name_id = searchField.get()
    if name_id == "":
        messagebox.showinfo("Error", "Enter Loan details to find")
    else:
        try:
            try:
                new_user_frame.destroy()
            except:
                pass
            cur.execute("select * from loan_details where loan_id='%s' or cust_id='%s'" % (name_id, name_id))
            loan_details = Frame(mainwindow, width=800, height=500)
            loan_details.place(relx=0.0, rely=0.07, relwidth=1, relheight=1)
            id_label = Label(loan_details, width=10, text='loan_id', borderwidth=2, relief='ridge', anchor='w',
                                 bg='gray')
            id_label.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=15, text='cust_id', borderwidth=2, relief='ridge', anchor='w',
                          bg='gray')
            e.place(relx=0.11, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=15, text='gua_id', borderwidth=2, relief='ridge', anchor='w',
                          bg='gray')
            e.place(relx=0.17, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='loan_type', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.place(relx=0.23, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='loan_amount', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.place(relx=0.29, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='interest rate', borderwidth=2, relief='ridge', anchor='w',
                          bg='gray')
            e.place(relx=0.35, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='loan_approved_date', borderwidth=2, relief='ridge', anchor='w',
                          bg='gray')
            e.place(relx=0.41, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='total_installments', borderwidth=2, relief='ridge', anchor='w',
                          bg='gray')
            e.place(relx=0.47, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='paid_installments', borderwidth=2, relief='ridge', anchor='w',
                          bg='gray')
            e.place(relx=0.53, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='amount_per_installment', borderwidth=2, relief='ridge', anchor='w',
                          bg='gray')
            e.place(relx=0.59, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='adv_payment_recieved', borderwidth=2, relief='ridge', anchor='w',
                      bg='gray')
            e.place(relx=0.65, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='over dues ', borderwidth=2, relief='ridge', anchor='w',
                      bg='gray')
            e.place(relx=0.71, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='next_installment_date', borderwidth=2, relief='ridge', anchor='w',
                      bg='gray')
            e.place(relx=0.77, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='loan_closing_date', borderwidth=2, relief='ridge', anchor='w',
                      bg='gray')
            e.place(relx=0.83, rely=0.05, relwidth=0.1, relheight=0.04)
            e = Label(loan_details, width=10, text='loan_status', borderwidth=2, relief='ridge', anchor='w',
                      bg='gray')
            e.place(relx=0.89, rely=0.05, relwidth=0.1, relheight=0.04)
            i = 1
            k = 0
            rx = 0.05
            rdx = rx
            ry = 0.1
            k = 0
            for values in cur:
                var = tk.IntVar()
                checkboxs.append(var)
                checkbox = tk.Checkbutton(loan_details, variable=var)
                checkbox.place(relx=0.03, rely=ry, relwidth=0.02, relheight=0.04)
                selected_loan_details.append(values[0])
                for j in range(len(values)):
                    l = Label(loan_details, text=values[j], borderwidth=2, relief='ridge', anchor='w')
                    l.place(relx=rx, rely=ry, relwidth=0.1, relheight=0.04)
                    rx = rx + 0.06
                ry = ry + 0.05
                rx = rdx
            modify_button = Button(loan_details, text="Modify", width=15, bg="light green", command = modifyLoanDetailsFrame)
            modify_button.place(relx=0.1, rely=0.75, relwidth=0.25, relheight=0.04)
            delete_button = Button(loan_details, text="PayLoan", width=15, bg="sky blue", command = collection_window_loan)
            delete_button.place(relx=0.6, rely=0.75, relwidth=0.25, relheight=0.04)
            back_button = Button(loan_details, text="Back", width=15, bg="light blue", command = loan_details.destroy)
            back_button.place(relx=0.25, rely=0.85, relwidth=0.5, relheight=0.04)
        except:
            pass

def new_loan():
    try:
        loan_details.destroy()
    except:
        pass
    global new_user_frame
    new_user_frame = Frame(mainwindow, width=800, height=500)
    new_user_frame.place(relx=0.22, rely=0.07, relwidth=1, relheight=1)
    t_label = Label(new_user_frame, text="Enter new loan details", fg="blue", font=("bold", 16))
    t_label.place(relx=0.2, rely=0.0, relheight=0.04)
    loan_id_label = Label(new_user_frame, text="loan ID  :", font=("arial", 12))
    loan_id_label.place(relx=0.03, rely=0.15, relheight=0.04)
    loan_id_field = Entry(new_user_frame, font=("bold", 14))
    loan_id_field.place(relx=0.2, rely=0.15, relwidth=0.4, relheight=0.04)

    cust_id_label = Label(new_user_frame, text="Customer ID  :", font=("arial", 12))
    cust_id_label.place(relx=0.03, rely=0.2, relheight=0.04)
    cust_id_Field = Entry(new_user_frame, font=("bold", 14))
    cust_id_Field.place(relx=0.2, rely=0.20, relwidth=0.4, relheight=0.04)

    gua_id_label = Label(new_user_frame, text="Guarantor ID :", font=("arial", 12))
    gua_id_label.place(relx=0.03, rely=0.25, relheight=0.04)
    gua_id_Field = Entry(new_user_frame, width=25, font=("bold", 14))
    gua_id_Field.place(relx=0.2, rely=0.25, relwidth=0.4, relheight=0.04)

    loan_type_list = ["Daily", "Weekly", "Monthly", "Yearly"]
    value_inside = StringVar(new_user_frame)
    value_inside.set("Loan Type")
    loan_type_label = Label(new_user_frame, text="Payment Type :", font=("arial", 12))
    loan_type_label.place(relx=0.03, rely=0.30, relheight=0.04)
    loan_type_Field = OptionMenu(new_user_frame, value_inside, *loan_type_list)
    loan_type_Field.place(relx=0.2, rely=0.30, relwidth=0.4, relheight=0.04)

    loan_amount_label = Label(new_user_frame, text="Loan Amount :", font=("arial", 12))
    loan_amount_label.place(relx=0.03, rely=0.35, relheight=0.04)
    loan_amount_Field = Entry(new_user_frame, width=25, font=("bold", 14))
    loan_amount_Field.place(relx=0.2, rely=0.35, relwidth=0.4, relheight=0.04)

    interest_rate_label = Label(new_user_frame, text="Interest Rate :", font=("arial", 12))
    interest_rate_label.place(relx=0.03, rely=0.40, relheight=0.04)
    interest_rate_field = Label(new_user_frame, text="0.60",fg="green", font=("arial", 12))
    interest_rate_field.place(relx=0.2, rely=0.40, relwidth=0.4, relheight=0.04)

    loan_approved_date_label = Label(new_user_frame, text="Approved Date:", font=("arial", 12))
    loan_approved_date_label.place(relx=0.03, rely=0.45, relheight=0.04)
    loan_approved_date_field = DateEntry(new_user_frame, text="Loan Start Date")
    loan_approved_date_field.place(relx=0.2, rely=0.45, relwidth=0.4, relheight=0.04)

    t_n_i = Label(new_user_frame, text="Total Installments:", font=("arial", 12))
    t_n_i.place(relx=0.03, rely=0.50, relheight=0.04)
    total_no_of_installments_LABEL = Label(new_user_frame, text="120 Days",fg="green", font=("arial", 12))
    total_no_of_installments_LABEL.place(relx=0.2, rely=0.50, relwidth=0.4, relheight=0.04)

    status_label = Label(new_user_frame, text="Status:", font=("arial", 12))
    status_label.place(relx=0.03, rely=0.55, relheight=0.04)
    status_Field = Entry(new_user_frame, width=25, font=("bold", 14))
    status_Field.place(relx=0.2, rely=0.55, relwidth=0.4, relheight=0.04)
    Add_Loan_button = Button(new_user_frame, text="Add Loan", width=15, bg="light green",
                                 command=lambda: AddLoandeatils(loan_id_field, cust_id_Field, gua_id_Field,
                                                         value_inside, loan_amount_Field,
                                                         loan_approved_date_field,
                                                         status_Field))
    Add_Loan_button.place(relx=0.2, rely=0.75, relwidth=0.4, relheight=0.04)
    back_button = Button(new_user_frame, text="Back", width=15, bg="light blue", command=new_user_frame.destroy)
    back_button.place(relx=0.2, rely=0.82, relwidth=0.4, relheight=0.04)

#mainwindow = tk.Tk()
#mainwindow.title("Customer Details")
#mainwindow.geometry("800x600")
def loanDetails(window):
    global searchField, login_frame2, mainwindow
    mainwindow = window
        #mainwindow = wind
    mainwindow.title("Loan Details")
    login_frame2 = Frame(mainwindow, width=1500, height=35, highlightbackground='gray', highlightthicknes=1)
    login_frame2.place(relx=0, rely=0, relwidth=1, relheight=1)
    new_user = Button(login_frame2, text="New Loan", font=("bold", 12),command=new_loan)
    new_user.place(relx=0, rely=0, relwidth=0.1, relheight=0.04)
    search_label = Label(login_frame2, text="Enter customer id or name to find:", font=("arial", 12))
    search_label.place(relx=0.11, rely=0, relwidth=0.4, relheight=0.04)
    searchField = Entry(login_frame2, width=25, font=("bold", 14))
    searchField.place(relx=0.48, rely=0, relwidth=0.4, relheight=0.04)
    search_button = tk.Button(login_frame2, text="Search", width=7, height=1, font=("bold", 12),command=search_loan)
    search_button.place(relx=0.89, rely=0, relwidth=0.1, relheight=0.04)
    back_home = tk.Button(login_frame2, text="Back", width=7, height=1, bg="light blue", font=("bold", 12),command = lambda : HomePage.Home(mainwindow))
    back_home.place(relx=0.25, rely=0.9, relwidth=0.5, relheight=0.04)
