from tkinter import *
import Customer_Details
import Guarantor_Details
import Loan_Details
import Collection_Details
import Finance_Details
from PIL import Image, ImageTk
global Home
def Home(mainw):
    global mainwindow,login_frame_h
    mainwindow = mainw
    mainwindow.title("Home Page")
    login_frame_h = Frame(mainwindow, width=1500, height=100)
    login_frame_h.place(relx=0, rely=0, relwidth=1, relheight=1)
    login_frame_h.config(bg="#E3F0F1")
    cust_details_b = Button(login_frame_h, text="Customer Details", font=("bold", 12), command = lambda : Customer_Details.Customer_Home_page(mainwindow))
    cust_details_b.place(relx=0.25, rely=0.10, relwidth=0.5, relheight=0.08)
    gua_details_b = Button(login_frame_h, text="Guarantor Details", font=("bold", 12),command= lambda :Guarantor_Details.loginsucess(mainwindow))
    gua_details_b.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.08)
    loan_Details = Button(login_frame_h, text="Loan Details", font=("bold", 12), command= lambda : Loan_Details.loanDetails(mainwindow))
    loan_Details.place(relx=0.25, rely=0.40, relwidth=0.5, relheight=0.08)
    loan_collection_b = Button(login_frame_h, text="Loan Collection Details", font=("bold", 12),command= lambda :Collection_Details.loginsucess(mainwindow))
    loan_collection_b.place(relx=0.25, rely=0.55, relwidth=0.5, relheight=0.08)
    history = Button(login_frame_h, text="Finance Details", font=("bold", 12),command= lambda : Finance_Details.login_Finance(mainwindow))
    history.place(relx=0.25, rely=0.70, relwidth=0.5, relheight=0.08)

