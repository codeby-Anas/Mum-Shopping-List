import tkinter as tk
from tkinter import messagebox
import json

# قائمة التسوق كمصفوفة فارغة
shopping_list = []

# دالة لحفظ القائمة في ملف JSON
def save_list():
    with open("shopping_list.json", "w") as file:
        json.dump(shopping_list, file)
    messagebox.showinfo("Saved", "Shopping list saved successfully.")

# دالة لتحميل القائمة من ملف JSON
def load_list():
    global shopping_list
    try:
        with open("shopping_list.json", "r") as file:
            shopping_list = json.load(file)
        messagebox.showinfo("Loaded", "Shopping list loaded successfully.")
    except FileNotFoundError:
        messagebox.showwarning("No saved list", "No saved list found. Starting with an empty list.")

# دالة لإضافة عنصر للقائمة مع الكمية والسعر والفئة
def add_item():
    item = entry_item.get()
    quantity = int(entry_quantity.get())
    price = float(entry_price.get())
    category = entry_category.get()

    if item and category:
        shopping_list.append({"item": item, "quantity": quantity, "price": price, "category": category})
        update_listbox()
        messagebox.showinfo("Item Added", f"{quantity} {item}(s) added to the list.")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields!")

# دالة لعرض العناصر في القائمة
def update_listbox():
    listbox.delete(0, tk.END)
    for entry in shopping_list:
        listbox.insert(tk.END, f"{entry['quantity']} {entry['item']}(s) - {entry['category']} at ${entry['price']} each")

# دالة لحذف عنصر من القائمة
def remove_item():
    try:
        selected_item = listbox.get(listbox.curselection())
        item_name = selected_item.split(" ")[1]
        shopping_list[:] = [i for i in shopping_list if i["item"] != item_name]
        update_listbox()
        messagebox.showinfo("Item Removed", f"{item_name} removed from the list.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select an item to remove.")

# دالة لتحديث الكمية
def update_quantity():
    try:
        selected_item = listbox.get(listbox.curselection())
        item_name = selected_item.split(" ")[1]
        new_quantity = int(entry_quantity.get())
        
        for entry in shopping_list:
            if entry["item"] == item_name:
                entry["quantity"] = new_quantity
                update_listbox()
                messagebox.showinfo("Quantity Updated", f"Quantity of {item_name} updated to {new_quantity}.")
                return
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select an item to update.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid quantity.")

# دالة لحساب التكلفة الإجمالية
def total_cost():
    total = sum(entry["quantity"] * entry["price"] for entry in shopping_list)
    messagebox.showinfo("Total Cost", f"Total cost: ${total:.2f}")

# واجهة التطبيق
window = tk.Tk()
window.title("Shopping List App")
window.geometry("500x500")
window.config(bg="#f0f0f0")

# عنوان
title_label = tk.Label(window, text="Shopping List", font=("Arial", 24), bg="#f0f0f0", fg="#1e90ff")
title_label.pack(pady=10)

# إدخال اسم العنصر
label_item = tk.Label(window, text="Item:", font=("Arial", 12), bg="#f0f0f0")
label_item.pack(pady=5)
entry_item = tk.Entry(window, font=("Arial", 12), width=30)
entry_item.pack(pady=5)

# إدخال الكمية
label_quantity = tk.Label(window, text="Quantity:", font=("Arial", 12), bg="#f0f0f0")
label_quantity.pack(pady=5)
entry_quantity = tk.Entry(window, font=("Arial", 12), width=30)
entry_quantity.pack(pady=5)

# إدخال السعر
label_price = tk.Label(window, text="Price per Item:", font=("Arial", 12), bg="#f0f0f0")
label_price.pack(pady=5)
entry_price = tk.Entry(window, font=("Arial", 12), width=30)
entry_price.pack(pady=5)

# إدخال الفئة
label_category = tk.Label(window, text="Category:", font=("Arial", 12), bg="#f0f0f0")
label_category.pack(pady=5)
entry_category = tk.Entry(window, font=("Arial", 12), width=30)
entry_category.pack(pady=5)

# أزرار التطبيق
button_add = tk.Button(window, text="Add Item", font=("Arial", 12), bg="#4CAF50", fg="white", command=add_item)
button_add.pack(pady=10)

button_remove = tk.Button(window, text="Remove Selected Item", font=("Arial", 12), bg="#f44336", fg="white", command=remove_item)
button_remove.pack(pady=10)

button_update = tk.Button(window, text="Update Quantity", font=("Arial", 12), bg="#2196F3", fg="white", command=update_quantity)
button_update.pack(pady=10)

button_total = tk.Button(window, text="Show Total Cost", font=("Arial", 12), bg="#FF9800", fg="white", command=total_cost)
button_total.pack(pady=10)

# قائمة عرض العناصر
listbox = tk.Listbox(window, font=("Arial", 12), width=50, height=10)
listbox.pack(pady=10)

# تحميل القائمة المحفوظة
load_button = tk.Button(window, text="Load Saved List", font=("Arial", 12), bg="#607D8B", fg="white", command=load_list)
load_button.pack(pady=10)

# حفظ القائمة
save_button = tk.Button(window, text="Save List", font=("Arial", 12), bg="#607D8B", fg="white", command=save_list)
save_button.pack(pady=10)

# تشغيل التطبيق
window.mainloop()















