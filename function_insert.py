import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from main_Screen import *

requisition_id = [10000]
price_items = []
date = 0
staff_id = ""
staff_Name = ""
total_items = 0.0
pattern = "%Y-%m-%d"

def empty_field():
    print("-------")
    staff_id = staff_id_entry.get()
    date = date_entry.get()
    staff_Name = staff_Name_entry.get()

    if staff_id == "" or date == "" or staff_Name == "":
        messagebox.showerror("Empty Field", "Empty Fields!!")
        return True


def add_requisition():
    empyty = empty_field()

    if empyty:
        return
    name_item = item_name_entry.get()

    print(price_items)
    if name_item == "":
        messagebox.showerror("Error", "Empty Fields!!")
        return
    try:
        price_item = float(item_price_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid value!")
        return
    price_items.append(float(price_item))

    item_info = [name_item, price_item]
    item_list.insert(1, item_info)
    item_name_entry.delete(0, tk.END)
    item_price_entry.delete(0, tk.END)

def calculate_total():
    global total_items
    requisition_id.append(requisition_id[len(requisition_id) - 1] + 1)
    sum = 0.0
    for i in price_items:
        sum += float(i)
    if sum > 0:
        total_items = sum
        print("SUM",sum)
        print(f"Total: ${total_items}\n")
        messagebox.showinfo("", "You can Check Approval!")


def requisition_approval():
    empty_field()
    staff_id = staff_id_entry.get()

    global status
    global approval_reference
    status = "Pending"
    requisition = str(requisition_id[len(requisition_id) - 1])
    if total_items < 500.0:
        status = "Approved"
        approval_reference = staff_id + requisition[-3:]
        print(f"Total: ${total_items}")
        print(f"Status: {status}")
        print(f"Approval Reference Number: {approval_reference}")
    else:
        approval_reference = 000
    display_requisitions(staff_id)

def display_requisitions(staff_id):
    date = date_entry.get()
    staff_Name = staff_Name_entry.get()
    global total_items

    try:
        date_value = datetime.strptime(date, pattern)
        print("Valid date accepted:", date_value.date())
    except ValueError:
        print("Invalid format. Please use YYYY-MM-DD.")
        return
        top = tk.Toplevel()
        top.title('Requisitions')
        top.geometry("250x300")
        tk.Label(top, text="Printing requisitions:").grid(row=0, column=0, padx=15, pady=5)
        tk.Label(top, text=f"Date: {date_value.date()}").grid(row=1, column=0, padx=15, pady=5)
        tk.Label(top, text=f"Requisition ID: {requisition_id[len(requisition_id) - 1]}").grid(row=2, column=0, padx=15, pady=5)
        tk.Label(top, text=f"Staff ID: {staff_id}").grid(row=3, column=0, padx=15, pady=5)
        tk.Label(top, text=f"Staff Name: {staff_Name}").grid(row=4,column=0, padx=15, pady=5)
        tk.Label(top, text=f"Total ${total_items}").grid(row=5,column=0, padx=15, pady=5)
        tk.Label(top, text=f"Status:{status}").grid(row=6,column=0, padx=15, pady=5)
        tk.Label(top, text=f"Approval Reference Number: {approval_reference}").grid(row=7,column=0, padx=15, pady=5)

    item_list.delete(0, tk.END)
    total_items = 0.0
    price_items.clear()

    tk.mainloop()
