import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import typing
from tk_Function import Tk_function
if typing.TYPE_CHECKING:
    from main_Screen import *

class Requisition:

    def __init__(self, values: Tk_function):
        self.price_items = []
        self.date = values.date
        self.staff_id = values.staff_id
        self.staff_Name = values.staff_Name
        self.total_items = 0
        self.requisition_id = [10000]
        self.pattern = "%Y-%m-%d"
        self.status = "Pending"
        self.approval_reference = 0000
        self.name_item = ""
        self.price_item = 0

    def empty_field(self):
        self.define()
        print("-------")
        if self.staff_id == "" or self.date == "" or self.staff_Name == "":
            messagebox.showerror("Empty Field", "Empty Fields!!")
            return True


    def add_requisition(self):
        empty = self.empty_field()

        if empty:
            return
        self.name_item = item_name_entry.get()
        try:
            self.price_item = float(item_price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid value!")
            return
        if self.name_item == "":
            messagebox.showerror("Error", "Empty Fields!!")
            return

        Tk_function.insert_Items(self.name_item, self.price_item)

    def calculate_total(self):
        self.requisition_id.append(self.requisition_id[len(self.requisition_id) - 1] + 1)
        sum = 0.0
        for i in self.price_items:
            sum += float(i)
        if sum > 0:
            self.total_items = sum
            print("SUM",sum)
            print(f"Total: ${self.total_items}\n")
            messagebox.showinfo("", "You can Check Approval!")


    def requisition_approval(self):
        empty = self.empty_field()
        if empty:
            return
        
        self.requisition = str(self.requisition_id[len(self.requisition_id) - 1])
        if self.total_items < 500.0:
            self.status = "Approved"
            self.approval_reference = self.staff_id + self.requisition[-3:]
            print(f"Total: ${self.total_items}")
            print(f"Status: {self.status}")
            print(f"Approval Reference Number: {self.approval_reference}")
        self.display_requisitions()

    def display_requisitions(self):

        try:
            date_value = datetime.strptime(self.date, self.pattern)
            print("Valid date accepted:", date_value.date())
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD.")
            return

        Tk_function.tk_top(date_value.date(), self.requisition_id[len(self.requisition_id) - 1], self.staff_id, self.staff_Name, self.total_items, self.status, self.approval_reference)
        self.clear(self.total_items, self.price_items)

    def clear(self):
        item_list.delete(0, tk.END)
        self.total_items = 0.0
        self.price_items.clear()