import tkinter as tk
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
# import time

#gui start
root = tk.Tk()

root.iconbitmap('images/favicon.ico')
root.title('Check SRC Error Tool')

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=4, rowspan=6)

#logo
logo = Image.open('images/knapp_logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#instructions
instructions = tk.Label(root, text="Search for an SRC error code!", font="Railway")
instructions.grid(columnspan=3, column=0, row=1)


#input field and submit button
searchBox = Entry(root, width=50)   #text="Example: M-ASR-SPID-0010"
searchBox.grid(column=1, row=3)


#btn function
def searchAction():
    button_text.set("Search again?")
    print(searchBox.get())
    searchBox.delete(0, END)

    # if len(searchBox.get()) == 0:
    #     print("try again!")
        

    
    conn = sqlite3.connect('srcappdb.db')
    a = conn.cursor()
    b = conn.cursor()
    c = conn.cursor()
    d = conn.cursor()
   
    error_code  = a.execute("select ERROR_CODE from src_errors where ERROR_CODE like " + "'%" + searchBox.get() + "%'") 
    message     = b.execute("select MESSAGE from src_errors where ERROR_CODE like " + "'%" + searchBox.get() + "%'")
    cause       = c.execute("select CAUSE from src_errors where ERROR_CODE like " + "'%" + searchBox.get() + "%'")
    resolution  = d.execute("select MESSAGE from src_errors where ERROR_CODE like " + "'%" + searchBox.get() + "%'")
    
    error_code_record   = a.fetchall()
    message_record      = b.fetchall()
    # cause_record        = c.fetchall()
    # resolution_record   = d.fetchall()

    #query labels - one for each column?
    query_label1 = Label(root, text=error_code_record)
    query_label1.grid(column= 0, row=5)
    query_label2 = Label(root, text=message_record)
    query_label2.grid(column= 1, row=5)
    # query_label3 = Label(root, text=cause_record)
    # query_label3.grid(column= 2, row=5, columnspan=1)
    # query_label4 = Label(root, text=resolution_record)
    # query_label4.grid(column= 3, row=5, columnspan=1)




    conn.commit()
    conn.close()
    print(searchBox.get())
    searchBox.delete(0, END)
    #button_text.set("Submit")


#search button
button_text = tk.StringVar()
submit_btn = tk.Button(root, textvariable=button_text, command=searchAction, font="Railway", height=2, width=15)
button_text.set("Submit")
submit_btn.grid(column=1, row=4)







#lazy method to pad-out bottom of gui
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


#infinite loop for app to remain open etc.
root.mainloop()
#gui end