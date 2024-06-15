from tkinter import *
import pymysql

from tkcalendar import Calendar, DateEntry
from datetime import datetime ,timedelta,date
import HomePage
from tkinter import ttk
from tkinter import filedialog
mypass = "mysql"
con = pymysql.connect(host="localhost", user="root", password=mypass, database="fnb")
cur = con.cursor()
def date_modify(date_str, day, date_format="%Y-%m-%d"):
    date = datetime.strptime(date_str, date_format)
    one_day = timedelta(days=day)
    new_date = date + one_day
    new_date_str = new_date.strftime(date_format)
    return new_date_str
def Apply_filter(filter_day_type1 ,filter_type1,start_date_f, end_date1 ):
    filter_day_type = filter_day_type1.get()
    filter_type = filter_type1.get()
    start_date1 = start_date_f.get_date()
    start_date1 = datetime.strftime(start_date1, "%Y-%m-%d")
    end_date = end_date1.get_date()
    start_date = datetime.strftime(end_date, "%Y-%m-%d")
    #___.............---#

    loan_details = Frame(mainwindow, width=800, height=500)
    loan_details.place(relx=0.0, rely=0.3, relwidth=1, relheight=0.7)
    canvas = Canvas(loan_details)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbar = Scrollbar(loan_details, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    inner_frame = Frame(canvas)
    canvas.create_window((100, 0), window=inner_frame, anchor="nw")
    con.commit()

    if filter_day_type == "Daily":
        end_date = date_modify(str(start_date), 0)
    elif filter_day_type == "Weekly":
        end_date = date_modify(str(start_date), -7)
    elif filter_day_type == "Monthly":
        end_date = date_modify(str(start_date),-30)
    elif filter_day_type == "Yearly":
        end_date = date_modify(str(start_date),-365)
    elif filter_day_type == "Custome":
        end_date = start_date1
    end_date = str(end_date)
    value_1 = (end_date, start_date)
    if filter_type == "Loan Sanctioned" or filter_type == "Loan Receivable":
        query_1 =""
        global l_text,t_m
        t_m = 0
        if filter_type == "Loan Sanctioned":
            query_1 = "select * from loan_details where loan_approved_date between %s and %s"
            q_2 = "select sum(loan_amount) from loan_details where loan_approved_date between %s and %s "
            cur.execute(q_2,value_1)
            l_text = "Total Amount Sanctioned: "
            t_m = cur.fetchone()[0]
        elif filter_type == "Loan Receivable":
            query_1 = "select * from loan_details where next_installment_date between %s and %s"
            l_text = "Total Amount Receivable: "
        cur.execute(query_1,value_1)
        id_label = Label(inner_frame, text='loan_id', borderwidth=2, relief='ridge', anchor='w',
                         bg='gray')
        id_label.grid(row=0, column=0)
        e = Label(inner_frame, text='cust_id', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=1)
        e = Label(inner_frame,  text='gua_id', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=2)
        e = Label(inner_frame,  text='loan_type', borderwidth=2, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=3)
        e = Label(inner_frame, text='loan_amount', borderwidth=2, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=4)
        e = Label(inner_frame, text='interest rate', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=5)
        e = Label(inner_frame,  text='loan_approved_date', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=6)
        e = Label(inner_frame,  text='total_installments', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=7)
        e = Label(inner_frame,  text='paid_installments', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=8)
        e = Label(inner_frame,  text='amount_per_installment', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=9)
        e = Label(inner_frame,  text='adv_payment_recieved', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=10)
        e = Label(inner_frame, text='over dues ', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=11)
        e = Label(inner_frame, text='next_installment_date', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=12)
        e = Label(inner_frame, text='loan_closing_date', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=13)
        e = Label(inner_frame,  text='loan_status', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=14)
        i = 1
        k = 0
        t_day = date.today()
        for values in cur:
            if filter_type == "Loan Receivable":
                daysc = (t_day-values[12]).days
                t_m = t_m + values[9]*daysc
            for j in range(len(values)):
                l = Label(inner_frame, text=values[j], borderwidth=2, relief='ridge', anchor='w')
                l.grid(row=i,column=k)
                k=k+1

            k=0
            i=i+1

    elif filter_type == "Loan Received":
        l_text = "Total Amount Received: "
        q = "select sum(total_amount_received) from collections where payment_received_date between %s and %s"
        cur.execute(q,value_1)
        t_m = cur.fetchone()[0]
        query_3 = "select * from collections where payment_received_date between %s and %s"
        cur.execute(query_3,value_1)
        e = Label(inner_frame, text='coll ID', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=1)
        e = Label(inner_frame, text='Loan ID', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=2)
        e = Label(inner_frame, text='Cust ID', borderwidth=2, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=3)
        e = Label(inner_frame, text='No Of Installment paid', borderwidth=2, relief='ridge', anchor='w', bg='gray')
        e.grid(row=0, column=4)
        e = Label(inner_frame, text='Total Amount Received', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=5)
        e = Label(inner_frame, text='Payment Mode', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=6)
        e = Label(inner_frame, text='Payment Received Date', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=7)
        e = Label(inner_frame, text='Transaction Details', borderwidth=2, relief='ridge', anchor='w',
                  bg='gray')
        e.grid(row=0, column=8)

        i =1
        k=1
        for values in cur:
            for j in range(len(values)):
                l = Label(inner_frame, text=values[j], borderwidth=2, relief='ridge', anchor='w')
                l.grid(row=i,column=k)
                k=k+1

            k=1
            i=i+1


    d_text = "From "
    d_text += str(end_date)
    d_text += " To "
    d_text += str(start_date)
    date_l = Label(f_frame, text = d_text, font=("bold",14))
    date_l.place(relx=0.35, rely=0.6)
    t = Label(f_frame, text=l_text, font=("bold", 14), fg="blue")
    t.place(relx=0.3, rely=0.25)
    t_t = Label(f_frame, text ="                             ", font = ("bold", 14), fg="blue")
    t_t.place(relx=0.6, rely=0.25)
    t_a = Label(f_frame, text=str(t_m) + " ", font=("bold", 14), fg="green")
    t_a.place(relx=0.6, rely=0.25)

def login_Finance(wind):
    global mainwindow
    mainwindow = wind
    global f_frame
    mainwindow.title("Finance Details")
    f_frame = Frame(mainwindow, width=1500, height=35, highlightbackground='gray', highlightthicknes=1)
    f_frame.place(relx=0, rely=0, relwidth=1, relheight=0.25)

    filter_list = ["Daily", "Weekly", "Monthly","Yearly","Custome"]
    value_inside3 = StringVar(f_frame)
    value_inside3.set("Daily")
    filter_user = OptionMenu(f_frame, value_inside3, *filter_list)
    filter_user.place(relx=0.07, rely=0.01, relwidth=0.15, relheight=0.2)

    filter_list2 = ["Loan Sanctioned", "Loan Received", "Loan Receivable"]
    value_inside4 = StringVar(f_frame)
    value_inside4.set("Loan Sanctioned")
    filter_user = OptionMenu(f_frame, value_inside4, *filter_list2)
    filter_user.place(relx=0.18, rely=0.01, relwidth=0.18, relheight=0.2)

    start_date_l = Label(f_frame,text="Start Date:",fg="blue",font=("Arial",12,"bold"))
    start_date_l.place(relx=0.39, rely=0.01)
    start_date_f = DateEntry(f_frame)
    start_date_f.place(relx=0.50, rely=0.01, relwidth=0.12, relheight=0.2)

    end_date_l =Label(f_frame,text="End Date:",fg="blue",font=("Arial",12,"bold"))
    end_date_l.place(relx=0.62, rely=0.01)
    end_date = DateEntry(f_frame)
    end_date.place(relx=0.73, rely=0.01, relwidth=0.12, relheight=0.2)



    search_button = Button(f_frame, text="Apply", width=7, height=1, font=("bold", 12),command = lambda : Apply_filter(value_inside3,value_inside4,start_date_f,end_date))
    search_button.place(relx=0.9, rely=0, relwidth=0.1, relheight=0.2 )
    back_home = Button(f_frame, text="X", width=7, height=1, bg="#FD9F84", font=("bold", 18),
                          command=lambda: HomePage.Home(mainwindow))
    back_home.place(relx=0.0, rely=0.01, relwidth=0.05, relheight=0.2)

    fin_details = Frame(mainwindow, width=800, height=500)
    fin_details.place(relx=0, rely=0.25, relwidth=1, relheight=0.85)

    canvas = Canvas(fin_details)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(fin_details, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    inner_frame = Frame(canvas)
    canvas.create_window((100, 0), window=inner_frame, anchor="nw")
