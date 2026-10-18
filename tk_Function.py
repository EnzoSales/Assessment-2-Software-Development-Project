import tkinter as tk
import typing
if typing.TYPE_CHECKING:
    from main_Screen import staff_id_entry, date_entry, staff_Name_entry, item_name_entry, item_list, item_price_entry

class Tk_function:

    def __init__(self):
        self.staff_id = staff_id_entry.get()
        self.date = date_entry.get()
        self.staff_Name = staff_Name_entry.get()
        self.name_item = item_name_entry.get()

    def insert_Items(self, name_item, price_item):
        item_info = [name_item, price_item]
        item_list.insert(1, item_info)
        item_name_entry.delete(0, tk.END)
        item_price_entry.delete(0, tk.END)


    def tk_top(date_value, requisition_id, staff_id, staff_Name, total_items, status, approval_reference):
        top = tk.Toplevel()
        top.title('Requisitions')
        top.geometry("250x300")
        tk.Label(top, text="Printing requisitions:").grid(row=0, column=0, padx=15, pady=5)
        tk.Label(top, text=f"Date: {date_value}").grid(row=1, column=0, padx=15, pady=5)
        tk.Label(top, text=f"Requisition ID: {requisition_id}").grid(row=2, column=0, padx=15, pady=5)
        tk.Label(top, text=f"Staff ID: {staff_id}").grid(row=3, column=0, padx=15, pady=5)
        tk.Label(top, text=f"Staff Name: {staff_Name}").grid(row=4,column=0, padx=15, pady=5)
        tk.Label(top, text=f"Total ${total_items}").grid(row=5,column=0, padx=15, pady=5)
        tk.Label(top, text=f"Status:{status}").grid(row=6,column=0, padx=15, pady=5)
        tk.Label(top, text=f"Approval Reference Number: {approval_reference}").grid(row=7,column=0, padx=15, pady=5)
        tk.mainloop()