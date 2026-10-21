from __future__ import annotations
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tk_Function import Tk_Function



class Requisition():

    staff_id = 0
    requisition_id = [10000]
    def __init__(self, values):
        print(values)
        self.staff_id = values[0]
        self.date = values[1]
        self.staff_Name = values[2]
        self.name_item = values[3]
        self.price_item = values[4]
        self.total_items = 0
        self.pattern = "%Y-%m-%d"
        self.status = "Pending"
        self.approval_reference = 0000
    
    def empty_field(self):
        print(self.staff_id, self.date, self.staff_Name)
        if self.staff_id == "" or self.date == "" or self.staff_Name == "":
            messagebox.showerror("Empty Field", "Empty Fields!!")
            return True

    def add_requisition(self):
        empty = self.empty_field()

        if empty:
            return
        try:
            self.price_item = float(self.price_item)
        except ValueError:
            messagebox.showerror("Error1", "Invalid value!")
            return
        if self.name_item == "":
            messagebox.showerror("Error2", "Empty Fields!!")
            return

        # tk.insert_Items(self.name_item, self.price_item)

    def calculate_total(self):
        self.requisition_id.append(self.requisition_id[len(self.requisition_id) - 1] + 1)
        sum = 0.0
        for i in self.price_item:
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

        #tk.tk_top(date_value.date(), self.requisition_id[len(self.requisition_id) - 1], self.staff_id, self.staff_Name, self.total_items, self.status, self.approval_reference)
        self.clear(self.total_items, self.price_items)

    def clear(self):
        #item_list.delete(0, tk.END)
        self.total_items = 0.0
        self.price_items.clear()