import tkinter as tk
from tkinter import *
import pymysql
import io
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkcalendar import Calendar, DateEntry
from datetime import datetime
import HomePage
from tkinter import filedialog
mypass = "mysql"
con = pymysql.connect(host="localhost", user="root", password=mypass, database="fnb")
cur = con.cursor()

def select_image():
    global image_location
    image_location = filedialog.askopenfilename()
    photo_text="Change Photo"
    return image_location
def update_image( image_location ,cust_id):
    with open(image_location, "rb") as file:
        photo_data = file.read()
    try:
        updatequery = "update customer_details set cust_photo=%s where cust_id=%s"
        updatevalue = (photo_data, cust_id)
        cur.execute(updatequery,updatevalue)
        con.commit()
        messagebox.showinfo("Updated Photo","photo updated success")
    except:
        messagebox.showerror("Update Failed","Select Image ")

def clear_view():
    #con.close()
    mypass = "mysql"
    con1 = pymysql.connect(host="localhost", user="root", password=mypass, database="fnb")
    cur = con.cursor()
    con.commit()
    selected_customers = [var.get() for var in checkboxs]
    global modify_values,modify_cust
    if selected_customers.count(1) == 1:
        try:
            cur.execute("select * from customer_details where cust_id= '%s'" % (str(selected_cust[selected_customers.index(1)])))
            rows = cur.fetchall()

        except:
            pass
        modify_cust = Toplevel()
        modify_cust.title("Modify customer details")
        modify_cust.geometry("1000x600")
        for modify_values in rows:
            t_label = Label(modify_cust, text="Customer Full Details", fg="blue", font=("bold", 16))
            t_label.place(relx=0.01, rely=0.0, relheight=0.04)
            cust_id_label = Label(modify_cust, text="Customer Photo :", font=("arial", 12))
            cust_id_label.place(relx=0.01, rely=0.05, relheight=0.04)
            if modify_values[2] is not None:
                try:
                    image = Image.open(BytesIO(modify_values[2]))
                    image = image.resize((200, 200))
                    photo = ImageTk.PhotoImage(image)
                    label = Label(modify_cust, image=photo)
                    label.image = photo
                    label.place(relx=0.03, rely=0.08)
                except:
                    label = Label(modify_cust, text="NA")
                    label.place(relx=0.03, rely=0.08)
            cust_name_label = Label(modify_cust, text=modify_values[1], font=("bold", 14))
            cust_name_label.place(relx=0.03, rely=0.42, relwidth=0.15, relheight=0.04)
            cust_id_label = Label(modify_cust, text="Customer ID  :", font=("arial", 12))
            cust_id_label.place(relx=0.3, rely=0.05, relheight=0.03)
            custidField = Label(modify_cust, text=modify_values[0], font=("arial", 12))
            custidField.place(relx=0.4, rely=0.05, relwidth=0.15, relheight=0.04)
            c_f_label = Label(modify_cust, text="Father Name:", font=("arial", 12))
            c_f_label.place(relx=0.3, rely=0.10, relheight=0.03)
            c_f_Field = Label(modify_cust,text=modify_values[3], font=("bold", 14))
            c_f_Field.place(relx=0.4, rely=0.10, relwidth=0.15, relheight=0.04)
            c_m_label = Label(modify_cust, text="Mother Name:", font=("arial", 12))
            c_m_label.place(relx=0.3, rely=0.15, relheight=0.04)
            c_m_Field = Label(modify_cust, text=modify_values[4], font=("bold", 14))
            c_m_Field.place(relx=0.4, rely=0.15, relwidth=0.15, relheight=0.04)
            c_add_label = Label(modify_cust, text="Address :", font=("arial", 12))
            c_add_label.place(relx=0.3, rely=0.20, relheight=0.04)
            c_add_Field = Label(modify_cust, text=modify_values[5], font=("bold", 14))
            c_add_Field.place(relx=0.4, rely=0.20, relwidth=0.15, relheight=0.04)
            dob_label = Label(modify_cust, text="Date Of Birth :", font=("arial", 12))
            dob_label.place(relx=0.3, rely=0.25, relheight=0.04)
            dobField = Label(modify_cust, text=modify_values[6],font=("bold", 14))
            dobField.place(relx=0.4, rely=0.25, relwidth=0.15, relheight=0.04)
            gender_set =""
            if modify_values[7] == "m":
                gender_set="Male"
            elif modify_values[7] == "f":
                gender_set = "Female"
            else:
                gender_set = "Transgender"

            gender_label = Label(modify_cust, text="Gender :", font=("arial", 12))
            gender_label.place(relx=0.3, rely=0.30, relheight=0.04)
            genderField = Label(modify_cust, text=gender_set, font=("bold",12))
            genderField.place(relx=0.4, rely=0.30, relwidth=0.15, relheight=0.04)
            occu_label = Label(modify_cust, text="Occupation :", font=("arial", 12))
            occu_label.place(relx=0.3, rely=0.35, relheight=0.04)
            occuField = Label(modify_cust,text=modify_values[8], font=("bold", 14))
            occuField.place(relx=0.4, rely=0.35, relwidth=0.15, relheight=0.04)
            Aadhar_label = Label(modify_cust, text="Aadhar Number :", font=("arial", 12))
            Aadhar_label.place(relx=0.7, rely=0.05, relheight=0.04)
            AadharField = Label(modify_cust,text=modify_values[9], font=("bold", 14))
            AadharField.place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.04)
            pan_label = Label(modify_cust, text="PAN card Number :", font=("arial", 12))
            pan_label.place(relx=0.7, rely=0.10, relheight=0.04)
            panField = Label(modify_cust, text=modify_values[10], font=("bold", 14))
            panField.place(relx=0.8, rely=0.10, relwidth=0.15, relheight=0.04)
            e_label = Label(modify_cust, text="Email :", font=("arial", 12))
            e_label.place(relx=0.7, rely=0.15, relheight=0.04)
            eField = Label(modify_cust,text=modify_values[11], font=("bold", 14))
            eField.place(relx=0.8, rely=0.15, relwidth=0.15, relheight=0.04)
            mob_label = Label(modify_cust, text="Mobile Number :", font=("arial", 12))
            mob_label.place(relx=0.7, rely=0.20, relheight=0.04)
            mobField = Label(modify_cust, text=modify_values[12], font=("bold", 14))
            mobField.place(relx=0.8, rely=0.20, relwidth=0.15, relheight=0.04)
            Amob_label = Label(modify_cust, text="Alternate mobile  :", font=("arial", 12))
            Amob_label.place(relx=0.7, rely=0.25, relheight=0.04)
            AmobField =Label(modify_cust, text=modify_values[13],font=("bold", 14))
            AmobField.place(relx=0.8, rely=0.25, relwidth=0.15, relheight=0.04)
            loan_s_label = Label(modify_cust, text="Loan Status:", font=("arial", 12))
            loan_s_label.place(relx=0.7, rely=0.30, relheight=0.04)
            loan_s_Field =Label(modify_cust, text=modify_values[14], font=("bold", 14))
            loan_s_Field.place(relx=0.8, rely=0.30, relwidth=0.15, relheight=0.04)
            l_d = Label(modify_cust, text="Loan Details :", fg="blue", font=("Bold", 16))
            l_d.place(relx=0.01, rely=0.5, relheight=0.04)
            try:
                t_l = Label(modify_cust, text="Total Loans:", font=("bold", 14))
                t_l.place(relx=0.01,rely=0.55, relheight=0.04)
                cur.execute("select count(*) from loan_details where cust_id='%s'"%(modify_values[0]))
                t_l_c = Label(modify_cust, text=cur.fetchone(),fg="green", font=("bold", 14))
                t_l_c.place(relx=0.2,rely=0.55, relheight=0.04)
                t_a_l = Label(modify_cust, text="Active Loans:", font=("bold", 14))
                t_a_l.place(relx=0.4,rely=0.55, relheight=0.04)
                cur.execute("select count(*) from loan_details where cust_id='%s' and loan_status=1"%(modify_values[0]))
                t_a_l_c = Label(modify_cust, text=cur.fetchone(),fg="green", font=("bold", 14))
                t_a_l_c.place(relx=0.6,rely=0.55, relheight=0.04)
                t_i_l = Label(modify_cust, text="Closed Loans:", font=("bold", 14))
                t_i_l.place(relx=0.7,rely=0.55, relheight=0.04)
                cur.execute("select count(*) from loan_details where cust_id='%s' and loan_status=0"%(modify_values[0]))
                t_i_l_c = Label(modify_cust, text=cur.fetchone(), fg="green",font=("bold", 14))
                t_i_l_c.place(relx=0.9,rely=0.55, relheight=0.04)

                t_l_a = Label(modify_cust, text="Total Loan Amount:", font=("bold", 14))
                t_l_a.place(relx=0.01, rely=0.65, relheight=0.04)
                cur.execute("select sum(loan_amount) from loan_details where cust_id='%s'" % (modify_values[0]))
                t_l_amount = cur.fetchone()[0]

                t_l_a_c = Label(modify_cust, text=t_l_amount, fg="green",font=("bold", 14))
                t_l_a_c.place(relx=0.2, rely=0.65, relheight=0.04)
                t_l_a_pa = Label(modify_cust, text="total Amount Payable:", font=("bold", 14))
                t_l_a_pa.place(relx=0.4, rely=0.65, relheight=0.04)
                t_l_amount_p = float(t_l_amount*0.6*(4/12))+float(t_l_amount)
                t_l_a_c = Label(modify_cust, text=t_l_amount_p, fg="green", font=("bold", 14))
                t_l_a_c.place(relx=0.6, rely=0.65, relheight=0.04)

                t_a_p = Label(modify_cust, text="Paid Amount:", font=("bold", 14))
                t_a_p.place(relx=0.7, rely=0.65, relheight=0.04)
                cur.execute("select no_of_installments_paid,amount_per_installment,advanced_payment_recieved  from loan_details where cust_id='%s'" % (modify_values[0]))
                l_d_t = cur.fetchall()
                a_p =0
                for l_d in l_d_t:
                    a_p = a_p+(l_d[0] * l_d[1]) + l_d[2]
                t_a_p_c = Label(modify_cust, text=a_p,fg="green", font=("bold", 14))
                t_a_p_c.place(relx=0.9, rely=0.65, relheight=0.04)
                t_a_r = Label(modify_cust, text="Recievable Amount:", font=("bold", 14))
                t_a_r.place(relx=0.01, rely=0.75, relheight=0.04)
                b_p_a = t_l_amount_p - a_p
                t_a_r_c = Label(modify_cust, text=b_p_a,fg="green", font=("bold", 14))
                t_a_r_c.place(relx=0.2, rely=0.75, relheight=0.04)

                t_i_t = Label(modify_cust, text="Total Installments:", font=("bold", 14))
                t_i_t.place(relx=0.4, rely=0.75, relheight=0.04)
                cur.execute("select sum(total_no_of_installments) from loan_details where cust_id='%s'" % (modify_values[0]))
                t_i_h = cur.fetchone()
                t_l_c = Label(modify_cust, text=t_i_h[0], fg="green", font=("bold", 14))
                t_l_c.place(relx=0.6, rely=0.75, relheight=0.04)

                t_i_t = Label(modify_cust, text="Installments Recievable:", font=("bold", 14))
                t_i_t.place(relx=0.7, rely=0.75, relheight=0.04)
                cur.execute("select sum(no_of_installments_paid) from loan_details where cust_id='%s'" % (modify_values[0]))
                t_i_p = cur.fetchone()
                t_i_p_v = t_i_h[0]-t_i_p[0]
                t_l_c = Label(modify_cust, text=t_i_p_v, fg="green", font=("bold", 14))
                t_l_c.place(relx=0.9, rely=0.75, relheight=0.04)

            except:
                pass
            #    l_d_not_found = Label(modify_cust, text="Loan Details Not Found :", fg="red", font=("Bold", 16))
             #   l_d_not_found.place(relx=0.3, rely=0.55, relheight=0.04)
            back_button = Button(modify_cust, text="Quit", width=15, bg="light blue", command=modify_cust.destroy)
            back_button.place(relx=0.3, rely=0.95, relwidth=0.4, relheight=0.04)
            con1.close()



    elif selected_customers.count(1) == 0:
        messagebox.showinfo("Select Error", "Select one customer to show")
    else:
        messagebox.showinfo("Select Error", "Select only one customer at a time")


def addUser(custidField, cust_name_Field,image_location, c_f_Field, c_m_Field, c_add_Field, dobField, value_inside, occuField, AadharField, panField, eField, mobField, AmobField, loan_s_Field):
    global photo_data
    cust_id = custidField.get()
    cust_name = cust_name_Field.get()
    father_name = c_f_Field.get()
    mother_name = c_m_Field.get()
    address = c_add_Field.get()
    dob = dobField.get_date()
    gender = value_inside.get()
    occupation = occuField.get()
    aadhar_number = AadharField.get()
    pan_number = panField.get()
    email = eField.get()
    mobile_number = mobField.get()
    alternate_mobile = AmobField.get()
    loan_status = loan_s_Field.get()
    dob = datetime.strftime(dob, "%Y-%m-%d")
    if father_name == "":
        father_name = "null"
    if mother_name == "":
        mother_name = "null"
    if address == "":
        address = "null"
    if gender == "":
        gender = "null"
    elif gender == "Male":
        gender = "m"
    elif gender == "Female":
        gender = "f"
    else:
        gender = "t"
    if occupation == "":
        occupation = "null"
    if pan_number == "":
        pan_number = "null"
    if email == "":
        email = "null"
    if alternate_mobile == "":
        alternate_mobile = "null"
    if loan_status == "":
        loan_status = 0
    if cust_id == "" or cust_name == "" or aadhar_number == "" or mobile_number == "":
        messagebox.showinfo("Empty Field", "Enter all requires fields")
    else:
        with open(image_location, "rb") as file:
            photo_data = file.read()
        try:

            insert1 = "insert into customer_details (cust_id,customer_name,cust_photo,father_name,mother_name,address,date_of_birth,gender,occupation,aadhar_number,pan_card,email,mobile,alternate_mobile_number,loan_status) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            value = (cust_id, cust_name, photo_data, father_name, mother_name, address, dob, gender, occupation, aadhar_number, pan_number, email, mobile_number, alternate_mobile, loan_status)
            cur.execute(insert1, value)
            con.commit()
            messagebox.showinfo("Successful", "Customer Inserted successfully")

        except:
            cur.execute("select cust_id from customer_details where cust_id='%s'" % (cust_id))
            v = cur.fetchone()
            if int(v[0]) == int(cust_id):
                messagebox.showerror("Id Error", "Customer ID already exists ")
def modifyUserDetails(cust_id, cust_name_Field, c_f_Field, c_m_Field, c_add_Field, dobField, value_inside, occuField, AadharField, panField, eField, mobField, AmobField, loan_s_Field):
    cust_name = cust_name_Field.get()
    father_name = c_f_Field.get()
    mother_name = c_m_Field.get()
    address = c_add_Field.get()
    dob = dobField.get_date()
    gender = value_inside.get()
    occupation = occuField.get()
    aadhar_number = AadharField.get()
    pan_number = panField.get()
    email = eField.get()
    mobile_number = mobField.get()
    alternate_mobile = AmobField.get()
    loan_status = loan_s_Field.get()
    dob = datetime.strftime(dob, "%Y-%m-%d")

    if father_name == "":
        father_name = "null"
    if mother_name == "":
        mother_name = "null"
    if address == "":
        address = "null"
    if gender == "":
        gender = "null"
    elif gender == "Male":
        gender = "m"
    elif gender == "Female":
        gender = "f"
    else:
        gender = "t"
    if occupation == "":
        occupation = "null"
    if pan_number == "":
        pan_number = "null"
    if email == "":
        email = "null"
    if alternate_mobile == "":
        alternate_mobile = "null"
    if loan_status == "":
        loan_status = 0
    try:
        update_query = "update customer_details set customer_name=%s, father_name=%s, mother_name=%s ,address=%s, date_of_birth=%s, gender=%s,occupation=%s, aadhar_number=%s, pan_card=%s, email=%s, mobile=%s, alternate_mobile_number=%s,loan_status=%s where cust_id=%s"
        update_value = (cust_name, father_name, mother_name , address , dob , gender , occupation , aadhar_number , pan_number, email , mobile_number , alternate_mobile , loan_status , cust_id)
        cur.execute(update_query, update_value)
        con.commit()
        modify_cust.destroy()
        messagebox.showinfo("Successful", "Customer updated successfully")
    except:
        messagebox.showinfo("UnSuccess", "Customer Not updated ")

def delete_customer():
    selected_customers = [var.get() for var in checkboxs]
    if selected_customers.count(1)>0:
        ans = askyesno(title="Confirmation", message="Are you sure to delete customer")
        if ans:
            try:
                for d in range(len(selected_customers)):
                    if selected_customers[d] == 1:
                        try:
                            delete_cus = selected_cust[d]
                            cur.execute("set foreign_key_checks=0")
                            cur.execute("delete from customer_details where cust_id=%s",(delete_cus))
                            cur.execute("set foreign_key_checks=1")
                            con.commit()
                            messagebox.showinfo("Successful", "Customer deleted successfully")
                        except:
                            messagebox.showinfo("User Not Found", "Customer Not Found")
            except:
                pass
    else:
        messagebox.showinfo("Select", "Select atleast one customer")


def modify_customer():
    selected_customers = [var.get() for var in checkboxs]
    global modify_values,modify_cust, rows
    if selected_customers.count(1) == 1:
        try:
            cur.execute("select * from customer_details where cust_id= '%s'" % (str(selected_cust[selected_customers.index(1)])))
            rows = cur.fetchall()
        except:
            pass
        modify_cust = Toplevel()
        modify_cust.title("modify customer details")
        modify_cust.geometry("800x600")
        for modify_values in rows:
            t_label = Label(modify_cust, text="Enter customer details to modify", fg="blue", font=("bold", 16))
            t_label.place(relx=0.3, rely=0.0, relheight=0.04)
            cust_id_label = Label(modify_cust, text="Customer Photo :", font=("arial", 12))
            cust_id_label.place(relx=0.01, rely=0.05, relheight=0.04)
            if modify_values[2] is not None:
                image = Image.open(BytesIO(modify_values[2]))
                image = image.resize((200, 200))
                photo = ImageTk.PhotoImage(image)
                label = Label(modify_cust, image=photo)
                label.image = photo
                label.place(relx=0.03, rely=0.08)
            cust_photo_button = Button(modify_cust, text="Change Photo", font=("bold", 14), command=select_image)
            cust_photo_button.place(relx=0.03, rely=0.42, relwidth=0.2, relheight=0.04)
            update_button = Button(modify_cust, text="Update", font=("bold",12),command= lambda : update_image(image_location,modify_values[0]))
            update_button.place(relx=0.03, rely=0.48, relwidth=0.2, relheight=0.04)
            cust_id_label = Label(modify_cust, text="Customer ID  :", font=("arial", 12))
            cust_id_label.place(relx=0.3, rely=0.05, relheight=0.04)
            custidField = Label(modify_cust, text=modify_values[0], font=("arial", 12))
            custidField.place(relx=0.5, rely=0.05, relwidth=0.4, relheight=0.04)
            cust_name_label = Label(modify_cust, text="Customer Name :", font=("arial", 12))
            cust_name_label.place(relx=0.3, rely=0.10, relheight=0.04)
            cust_name_Field = Entry(modify_cust, width=25, font=("bold", 14))
            cust_name_Field.place(relx=0.5, rely=0.10, relwidth=0.4, relheight=0.04)
            cust_name_Field.insert(0, modify_values[1])
            c_f_label = Label(modify_cust, text="Father Name:", font=("arial", 12))
            c_f_label.place(relx=0.3, rely=0.15, relheight=0.04)
            c_f_Field = Entry(modify_cust, width=25, font=("bold", 14))
            c_f_Field.place(relx=0.5, rely=0.15, relwidth=0.4, relheight=0.04)
            c_f_Field.insert(0, modify_values[3])
            c_m_label = Label(modify_cust, text="Mother Name:", font=("arial", 12))
            c_m_label.place(relx=0.3, rely=0.20, relheight=0.04)
            c_m_Field = Entry(modify_cust, width=25, font=("bold", 14))
            c_m_Field.insert(0,modify_values[4])
            c_m_Field.place(relx=0.5, rely=0.20, relwidth=0.4, relheight=0.04)
            c_add_label = Label(modify_cust, text="Address :", font=("arial", 12))
            c_add_label.place(relx=0.3, rely=0.25, relheight=0.04)
            c_add_Field = Entry(modify_cust, width=25, font=("bold", 14))
            c_add_Field.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.04)
            c_add_Field.insert(0, modify_values[5])
            dob_label = Label(modify_cust, text="Date Of Birth :", font=("arial", 12))
            dob_label.place(relx=0.3, rely=0.30, relheight=0.04)
            dobField = DateEntry(modify_cust, text="Date Of Birth")
            dobField.place(relx=0.5, rely=0.30, relwidth=0.4, relheight=0.04)
            dobField.set_date(modify_values[6])
            gender_set =""
            if modify_values[7] == "m":
                gender_set="Male"
            elif modify_values[7] == "f":
                gender_set = "Female"
            else:
                gender_set = "Transgender"
            gender_list = ["Male", "Female", "Transgender"]
            value_inside = StringVar(modify_cust)
            value_inside.set(gender_set)
            gender_label = Label(modify_cust, text="Gender :", font=("arial", 12))
            gender_label.place(relx=0.3, rely=0.35, relheight=0.04)
            genderField = OptionMenu(modify_cust, value_inside, *gender_list)
            genderField.place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.04)
            occu_label = Label(modify_cust, text="Occupation :", font=("arial", 12))
            occu_label.place(relx=0.3, rely=0.40, relheight=0.04)
            occuField = Entry(modify_cust, width=25, font=("bold", 14))
            occuField.place(relx=0.5, rely=0.40, relwidth=0.4, relheight=0.04)
            occuField.insert(0,modify_values[8])
            Aadhar_label = Label(modify_cust, text="Aadhar Number :", font=("arial", 12))
            Aadhar_label.place(relx=0.3, rely=0.45, relheight=0.04)
            AadharField = Entry(modify_cust, width=25, font=("bold", 14))
            AadharField.place(relx=0.5, rely=0.45, relwidth=0.4, relheight=0.04)
            AadharField.insert(0,modify_values[9])
            pan_label = Label(modify_cust, text="PAN card Number :", font=("arial", 12))
            pan_label.place(relx=0.3, rely=0.50, relheight=0.04)
            panField = Entry(modify_cust, width=25, font=("bold", 14))
            panField.place(relx=0.5, rely=0.50, relwidth=0.4, relheight=0.04)
            panField.insert(0,modify_values[10])
            e_label = Label(modify_cust, text="Email :", font=("arial", 12))
            e_label.place(relx=0.3, rely=0.55, relheight=0.04)
            eField = Entry(modify_cust, width=25, font=("bold", 14))
            eField.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.04)
            eField.insert(0,modify_values[11])
            mob_label = Label(modify_cust, text="Mobile Number :", font=("arial", 12))
            mob_label.place(relx=0.3, rely=0.60, relheight=0.04)
            mobField = Entry(modify_cust, width=25, font=("bold", 14))
            mobField.place(relx=0.5, rely=0.60, relwidth=0.4, relheight=0.04)
            mobField.insert(0,modify_values[12])
            Amob_label = Label(modify_cust, text="Alternate mobile  :", font=("arial", 12))
            Amob_label.place(relx=0.3, rely=0.65, relheight=0.04)
            AmobField = Entry(modify_cust, width=25, font=("bold", 14))
            AmobField.place(relx=0.5, rely=0.65, relwidth=0.4, relheight=0.04)
            AmobField.insert(0,modify_values[13])
            loan_s_label = Label(modify_cust, text="Loan Status:", font=("arial", 12))
            loan_s_label.place(relx=0.3, rely=0.70, relheight=0.04)
            loan_s_Field = Entry(modify_cust, width=25, font=("bold", 14))
            loan_s_Field.place(relx=0.5, rely=0.70, relwidth=0.4, relheight=0.04)
            loan_s_Field.insert(0,modify_values[14])
            Add_user_button = Button(modify_cust, text="Modify User", width=15, bg="light green",
                                 command=lambda: modifyUserDetails(modify_values[0], cust_name_Field, c_f_Field, c_m_Field,
                                                         c_add_Field, dobField, value_inside, occuField, AadharField,
                                                         panField, eField, mobField, AmobField, loan_s_Field))
            Add_user_button.place(relx=0.4, rely=0.75, relwidth=0.4, relheight=0.04)
            back_button = Button(modify_cust, text="Quit", width=15, bg="light blue", command=modify_cust.destroy)
            back_button.place(relx=0.4, rely=0.82, relwidth=0.4, relheight=0.04)
    elif selected_customers.count(1) == 0:
        messagebox.showinfo("Select Error", "select one customer to modify")
    else:
        messagebox.showinfo("Select Error", "Select only one customer at a time")
def search(value_inside2):
    global cust_details, checkboxs, values, selected_cust
    try:
        modify_cust.destroy()
    except:
        pass
    selected_cust =[]
    checkboxs = []
    name_id = searchField.get()
    name_id2 = "%"+name_id+"%"
    filter_option = value_inside2.get()
    if name_id == "":
        messagebox.showinfo("Error", "Enter customer details to find")
    else:
        try:
            if filter_option == "All Customers":
                if name_id == "@":
                    cur.execute("select * from customer_details")
                else:
                    cur.execute("select * from customer_details where customer_name='%s' or cust_id='%s' or customer_name like '%s'" % (name_id, name_id,name_id2))
            elif filter_option == "Active Customers":
                if name_id == "@":
                    cur.execute("select * from customer_details where loan_status = 1")
                else:
                    cur.execute("select * from customer_details where customer_name= %s or cust_id= %s or customer_name like '%s' and loan_status = 1",(name_id, name_id,name_id2))
            elif filter_option == "Inactive Customers":
                if name_id == "@":
                    cur.execute("select * from customer_details where loan_status = 0")
                else:
                    cur.execute("select * from customer_details where customer_name=%s or cust_id=%s or customer_name like '%s' and loan_status = 0",(name_id, name_id,name_id2))
            else:
                cur.execute("select * from customer_details where customer_name='%s' or cust_id='%s'" % (name_id, name_id))
            try:
                new_user_frame.destroy()
            except:
                pass

            cust_details = Frame(mainwindow, width=800, height=500)
            cust_details.place(relx=0, rely=0.07, relwidth=1, relheight=1)

            canvas = Canvas(cust_details)
            canvas.pack(side=LEFT, fill=BOTH, expand=1)

            scrollbar = Scrollbar(cust_details, orient=VERTICAL, command=canvas.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            inner_frame = Frame(canvas)
            canvas.create_window((100, 0), window=inner_frame, anchor="nw")

            id_label = Label(inner_frame, width=10, text='CUST_ID', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            id_label.grid(row=0, column=2)
            e = Label(inner_frame, width=15, text='CUSTOMER_NAME', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.grid(row=0, column=3)
            e = Label(inner_frame, width=15, text='FATHER_NAME', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.grid(row=0, column=4)
            e = Label(inner_frame, width=10, text='ADDRESS', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.grid(row=0, column=5)
            e = Label(inner_frame, width=10, text='GENDER', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.grid(row=0, column=6)
            e = Label(inner_frame, width=10, text='OCCUPATION', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.grid(row=0, column=7)
            e = Label(inner_frame, width=10, text='LOAN STATUS', borderwidth=2, relief='ridge', anchor='w', bg='gray')
            e.grid(row=0, column=8)

            i = 1
            k=2
            rows = cur.fetchall()
            for row in rows:
                var = tk.IntVar()
                checkboxs.append(var)
                checkbox = tk.Checkbutton(inner_frame, variable=var)
                checkbox.grid(row=i, column=0)

                selected_cust.append(row[0])
                if row[2] is not None:
                    try:
                        image = Image.open(BytesIO(row[2]))
                        image = image.resize((100, 100))
                        photo = ImageTk.PhotoImage(image)
                        label = Label(inner_frame, image=photo)
                        label.image = photo
                        label.grid(row=i, column=1)
                    except:
                        pass

                for j in range(len(row)):
                    if j==2 or j == 4 or j == 6 or j == 12 or j == 11 or j == 9 or j == 10 or j == 13:
                        continue
                    l = Label(inner_frame, text=row[j], borderwidth=2, relief='ridge', anchor='w')
                    l.grid(row=i, column=k)
                    k=k+1
                k=2

                i += 1

            modify_button = Button(cust_details, text="Modify", width=15, bg="light blue",command=modify_customer)
            modify_button.place(relx=0.05, rely=0.75, relwidth=0.25, relheight=0.04)
            cv_button = Button(cust_details, text="Show", width=15, bg="light green",command=clear_view)
            cv_button.place(relx=0.7, rely=0.75, relwidth=0.25, relheight=0.04)
            delete_button = Button(cust_details, text="Delete", width=15, bg="red", command=delete_customer)
            delete_button.place(relx=0.38, rely=0.75, relwidth=0.25, relheight=0.04)
            back_button = Button(cust_details, text="Back", width=15, bg="sky blue", command = cust_details.destroy)
            back_button.place(relx=0.25, rely=0.85, relwidth=0.5, relheight=0.04)
        except Exception as e:
            print(e)

def new_user_window():
    global image_location
    image_location= ""
    try:
        cust_details.destroy()
    except:
        pass
    global new_user_frame,photo_text
    photo_text="Upload Photo"
    new_user_frame = Frame(mainwindow, width=800, height=500)
    new_user_frame.place(relx=0.22, rely=0.07, relwidth=1, relheight=1)
    t_label = Label(new_user_frame, text="Enter new user details", fg="blue", font=("bold", 16))
    t_label.place(relx=0.2, rely=0.0, relheight=0.04)
    cust_id_label = Label(new_user_frame, text="Customer ID  :", font=("arial", 12))
    cust_id_label.place(relx=0.03, rely=0.05, relheight=0.04)
    custidField = Entry(new_user_frame, font=("bold", 14))
    custidField.place(relx=0.2, rely=0.05, relwidth=0.4, relheight=0.04)
    cust_name_label = Label(new_user_frame, text="Customer Name :", font=("arial", 12))
    cust_name_label.place(relx=0.03, rely=0.10, relheight=0.04)
    cust_name_Field = Entry(new_user_frame, width=25, font=("bold", 14))
    cust_name_Field.place(relx=0.2, rely=0.10, relwidth=0.4, relheight=0.04)
    cust_photo = Label(new_user_frame, text="Customer Photo :", font=("arial", 12))
    cust_photo.place(relx=0.03, rely=0.15, relheight=0.04)
    cust_photo_Field = Button(new_user_frame,text=photo_text, font=("bold", 14),command=select_image)
    cust_photo_Field.place(relx=0.2, rely=0.15, relwidth=0.4, relheight=0.04)
    c_f_label = Label(new_user_frame, text="Father Name:", font=("arial", 12))
    c_f_label.place(relx=0.03, rely=0.20, relheight=0.04)
    c_f_Field = Entry(new_user_frame, width=25, font=("bold", 14))
    c_f_Field.place(relx=0.2, rely=0.20, relwidth=0.4, relheight=0.04)
    c_m_label = Label(new_user_frame, text="Mother Name:", font=("arial", 12))
    c_m_label.place(relx=0.03, rely=0.25, relheight=0.04)
    c_m_Field = Entry(new_user_frame, width=25, font=("bold", 14))
    c_m_Field.place(relx=0.2, rely=0.25, relwidth=0.4, relheight=0.04)
    c_add_label = Label(new_user_frame, text="Address :", font=("arial", 12))
    c_add_label.place(relx=0.03, rely=0.30, relheight=0.04)
    c_add_Field = Entry(new_user_frame, width=25, font=("bold", 14))
    c_add_Field.place(relx=0.2, rely=0.30, relwidth=0.4, relheight=0.04)
    dob_label = Label(new_user_frame, text="Date Of Birth :", font=("arial", 12))
    dob_label.place(relx=0.03, rely=0.35, relheight=0.04)
    dobField = DateEntry(new_user_frame, text="Date Of Birth")
    dobField.place(relx=0.2, rely=0.35, relwidth=0.4, relheight=0.04)
    gender_list = ["Male", "Female", "Transgender"]
    value_inside = StringVar(new_user_frame)
    value_inside.set("Select Gender")
    gender_label = Label(new_user_frame, text="Gender :", font=("arial", 12))
    gender_label.place(relx=0.03, rely=0.40, relheight=0.04)
    genderField = OptionMenu(new_user_frame, value_inside, *gender_list)
    genderField.place(relx=0.2, rely=0.40, relwidth=0.4, relheight=0.04)
    occu_label = Label(new_user_frame, text="Occupation :", font=("arial", 12))
    occu_label.place(relx=0.03, rely=0.45, relheight=0.04)
    occuField = Entry(new_user_frame, width=25, font=("bold", 14))
    occuField.place(relx=0.2, rely=0.45, relwidth=0.4, relheight=0.04)
    Aadhar_label = Label(new_user_frame, text="Aadhar Card No :", font=("arial", 12))
    Aadhar_label.place(relx=0.03, rely=0.50, relheight=0.04)
    AadharField = Entry(new_user_frame, width=25, font=("bold", 14))
    AadharField.place(relx=0.2, rely=0.50, relwidth=0.4, relheight=0.04)
    pan_label = Label(new_user_frame, text="PAN Card No :", font=("arial", 12))
    pan_label.place(relx=0.03, rely=0.55, relheight=0.04)
    panField = Entry(new_user_frame, width=25, font=("bold", 14))
    panField.place(relx=0.2, rely=0.55, relwidth=0.4, relheight=0.04)
    e_label = Label(new_user_frame, text="Email :", font=("arial", 12))
    e_label.place(relx=0.03, rely=0.60, relheight=0.04)
    eField = Entry(new_user_frame, width=25, font=("bold", 14))
    eField.place(relx=0.2, rely=0.60, relwidth=0.4, relheight=0.04)
    mob_label = Label(new_user_frame, text="Mobile Number :", font=("arial", 12))
    mob_label.place(relx=0.03, rely=0.65, relheight=0.04)
    mobField = Entry(new_user_frame, width=25, font=("bold", 14))
    mobField.place(relx=0.2, rely=0.65, relwidth=0.4, relheight=0.04)
    Amob_label = Label(new_user_frame, text="Alt Mobile No :", font=("arial", 12))
    Amob_label.place(relx=0.03, rely=0.70, relheight=0.04)
    AmobField = Entry(new_user_frame, width=25, font=("bold", 14))
    AmobField.place(relx=0.2, rely=0.70, relwidth=0.4, relheight=0.04)
    loan_s_label = Label(new_user_frame, text="User Status:", font=("arial", 12))
    loan_s_label.place(relx=0.03, rely=0.75, relheight=0.04)
    loan_s_Field = Entry(new_user_frame, width=25, font=("bold", 14))
    loan_s_Field.place(relx=0.2, rely=0.75, relwidth=0.4, relheight=0.04)
    Add_user_button = Button(new_user_frame, text="Add User", width=15, bg="light green",
                             command=lambda: addUser(custidField, cust_name_Field,image_location, c_f_Field, c_m_Field,
                                                     c_add_Field, dobField, value_inside, occuField, AadharField,
                                                     panField, eField, mobField, AmobField, loan_s_Field))
    Add_user_button.place(relx=0.2, rely=0.80, relwidth=0.4, relheight=0.04)
    back_button = Button(new_user_frame, text="Back", width=15, bg="light blue",command=new_user_frame.destroy)
    back_button.place(relx=0.2, rely=0.85, relwidth=0.4, relheight=0.04)
#mainwindow = tk.Tk()
#mainwindow.title("Customer Details")
#mainwindow.geometry("800x600")
def Customer_Home_page(wind):
    global searchField,login_frame2,mainwindow
    mainwindow=wind
    mainwindow.title("Customer Details")
    login_frame2 = Frame(mainwindow, width=1500, height=35, highlightbackground='gray', highlightthicknes=1)
    login_frame2.place(relx=0, rely=0, relwidth=1, relheight=1)
    new_user = Button(login_frame2, text="New User", font=("bold", 12), command=new_user_window)
    new_user.place(relx=0, rely=0, relwidth=0.1, relheight=0.04)
    filter_list = ["All Customers", "Active Customers", "Inactive Customers"]
    value_inside2 = StringVar(login_frame2)
    value_inside2.set("All Customers")
    filter_user = OptionMenu(login_frame2, value_inside2, *filter_list)
    filter_user.place(relx=0.11, rely=0, relwidth=0.15, relheight=0.04)
    search_label = Label(login_frame2, text="Enter customer id or name to find:", font=("arial", 14))
    search_label.place(relx=0.22, rely=0, relwidth=0.35, relheight=0.04)
    searchField = Entry(login_frame2, width=20, font=("bold", 14))
    searchField.place(relx=0.55, rely=0, relwidth=0.4, relheight=0.04)
    search_button = tk.Button(login_frame2, text="Search", width=7, height=1, font=("bold", 12), command= lambda :search(value_inside2))
    search_button.place(relx=0.89, rely=0, relwidth=0.1, relheight=0.04)
    back_home = tk.Button(login_frame2, text="Back", width=7, height=1,bg="light blue", font=("bold", 12), command= lambda : HomePage.Home(mainwindow))
    back_home.place(relx=0.25, rely=0.9, relwidth=0.5, relheight=0.04)
#loginsucess()
#mainwindow.mainloop()

