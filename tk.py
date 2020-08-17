# create a tkinter window

import tkinter as tk
from csv import DictWriter
import os
from tkinter import ttk
win =tk.Tk()
win.title("Devansh") # devansh as a title of window


# Create Labels  -- ttk --> radio button, labels

# from tkinter import ttk

name_label=ttk.Label(win,text="Enter your name :")
name_label.grid(row=0, column=0, sticky=tk.W) # pack can also be used as grid

email_label=ttk.Label(win, text="Enter your email :")
email_label.grid(row=1, column=0, sticky=tk.W)

age_label=ttk.Label(win,text="Enter your age :")
age_label.grid(row=2, column =0, sticky=tk.W)  # after the name_label so row =1

gender_label=ttk.Label(win, text="Select your gender")
gender_label.grid(row=3, column=0)

#CREATE ENTRY BOX
name_var=tk.StringVar() # to strore entered name
name_entrybox=ttk.Entry(win, width=16, textvariable= name_var)
name_entrybox.grid(row=0,column=1)

name_entrybox.focus() #--> automatic cursor on name

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var=tk.StringVar() # to strore entered name
age_entrybox=ttk.Entry(win, width=16, textvariable= age_var)
age_entrybox.grid(row=2,column=1)

#Create COMBOBOX- MALE/FEMALE

gender_var= tk.StringVar()

gender_combobox= ttk.Combobox(win, width=14,textvariable=gender_var, state="readonly") # state--> user cannot type in combobox
gender_combobox["values"]= ("Male","Female","Other")
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# Create a RADIO BUTTON  --> select one from many

usertype=tk.StringVar()

radiobtn1=ttk.Radiobutton(win, text="Student", value="Student", variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win, text="Teacher", value="Teacher", variable=usertype)
radiobtn2.grid(row=4,column=1)

#Create a CHECK BUTTON
checkbtn_var=tk.IntVar()

checkbtn=ttk.Checkbutton(win, text="Check if you love me",variable= checkbtn_var)
checkbtn.grid(row=5, columnspan=3) #columnspan--> take 3 columns but dont extend the other columns




# # SAVE THE DATA IN A FILE THAT USER HAVE ENTERED in txt file

# # CREATE BUTTON 
# def action():  # action for submit button
#     username=name_var.get()
#     userage=age_var.get()
#     useremail=email_var.get()
#     usergender=gender_var.get()
#     user_type=usertype.get()
#     if checkbtn_var.get()==0:
#         love_me="NO"
#     else:
#         love_me="Yes"
    
#     print(usergender, user_type, love_me) #--> baad ke 3 variable

#     print(f"{username} is {userage} years old and email is {useremail}")



#     with open("file.txt", "a") as f:

#         f.write(f"{username},{userage},{usergender},{useremail},{user_type},{love_me}\n")

#     name_entrybox.delete(0, tk.END)
#     age_entrybox.delete(0, tk.END)
#     email_entrybox.delete(0, tk.END)


#     name_label.config(foreground="Blue")




#TO WRITE ENTERED DATA IN CSV FILE


def action():  # action for submit button
    username= name_var.get()
    userage= age_var.get()
    useremail= email_var.get()
    usergender= gender_var.get()
    user_type= usertype.get()
    if checkbtn_var.get()==0:
        love_me="NO"
    else:
        love_me="Yes"

    #csv file

    with open("file1.csv","a", newline="") as f:
        dict_writer= DictWriter(f, fieldnames=["UserName","EmailAddress","UserGender","Usertype","Love me"])
        if os.stat("file1.csv").st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            "UserName": username,
            "EmailAddress": useremail,
            "UserGender": usergender,
            "Usertype" : user_type,
            "Love me" : love_me
        })





    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)


submit_button=ttk.Button(win, text="Submit", command=action)
submit_button.grid(row=6,column=0)



win.mainloop()