from __future__ import annotations
import tkinter as tk
import typing
import function_insert

def send_add_requisition():
    values = [staff_Name_entry.get(), staff_id_entry.get(), date_entry.get(), item_name_entry.get(), item_price_entry.get()]
    func = function_insert.Requisition(values)
    func.add_requisition()

def send_calculate_total():
    values = [staff_Name_entry.get(), staff_id_entry.get(), date_entry.get(), item_name_entry.get(), item_price_entry.get()]
    func = function_insert.Requisition(values)
    func.calculate_total()

def send_requisition_approval():
    values = [staff_Name_entry.get(), staff_id_entry.get(), date_entry.get(), item_name_entry.get(), item_price_entry.get()]
    func = function_insert.Requisition(values)
    func.requisition_approval()


root = tk.Tk()
root.title("Requisition System")
root.geometry("425x500")
tk.Label(root, text="Enter your information:").grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Staff Name:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Staff ID:").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Date(YYYY-MM-DD):").grid(row=3,column=0, padx=10, pady=5)
tk.Label(root, text="Add items:").grid(row=4,column=1, padx=10, pady=5)
tk.Label(root, text="Item Name:").grid(row=5,column=0, padx=10, pady=5)
tk.Label(root, text="Item price ($): ").grid(row=6,column=0, padx=10, pady=5)


staff_Name_entry = tk.Entry(root)
staff_id_entry = tk.Entry(root)
date_entry = tk.Entry(root)
item_name_entry = tk.Entry(root)
item_price_entry = tk.Entry(root)

staff_Name_entry.grid(row=1, column=1)
staff_id_entry.grid(row=2, column=1)
date_entry.grid(row=3, column=1)
item_name_entry.grid(row=5, column=1)
item_price_entry.grid(row=6, column=1)
item_list = tk.Listbox(root, width=45, height=6)
item_list.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
buttonAddRequisition = tk.Button(root, text="Add Item", width=15, command= send_add_requisition)
buttonAddRequisition.grid(row = 8, column = 0, padx=15, pady=10)
buttonCalculeteTotal = tk.Button(root, text="Calculate Total", width=15, command= send_calculate_total)
buttonCalculeteTotal.grid(row=8, column=1, padx=15, pady=10)
buttonCheckApproval = tk.Button(root, text="Check Approval", width=15, command= send_requisition_approval)
buttonCheckApproval.grid(row=8, column=2, padx=15, pady=10)
root.mainloop()