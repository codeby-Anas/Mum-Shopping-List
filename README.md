README: Shopping List App
Overview:

This is a simple Shopping List App developed using Python's Tkinter library for creating the graphical user interface (GUI) and JSON for saving and loading the shopping list data. The app allows users to add, remove, update, and view shopping items, including their quantity, price, and category. It also computes the total cost of the items in the list.

Features:

Add Items: Allows users to add items to the shopping list with details like quantity, price, and category.

Remove Items: Users can remove selected items from the list.

Update Quantity: Modify the quantity of a selected item.

Show Total Cost: Calculates and displays the total cost of the shopping list based on the quantity and price of each item.

Save List: Save the shopping list to a JSON file for future use.

Load List: Load the previously saved shopping list from a JSON file.

Requirements:

Python 3.x

Tkinter (should be included in the standard library of Python)

JSON (standard library in Python)

File Structure:

shopping_list.json: A JSON file to store the shopping list data.

How to Run:

Clone or Download the code files.

Ensure you have Python installed on your machine.

If you don't have Tkinter installed (it usually comes pre-installed with Python), install it using: pip install tk

Run the application: python shopping_list_app.py
This will open a GUI window where you can interact with the shopping list.
Application Workflow:

Add an Item:

Enter the item name in the "Item" field.

Specify the quantity in the "Quantity" field.

Enter the price per item in the "Price per Item" field.

Enter the category in the "Category" field.

Click the Add Item button to add the item to the shopping list.

Remove an Item:

Select an item from the list displayed in the Listbox.

Click the Remove Selected Item button to remove it from the shopping list.

Update Item Quantity:

Select an item from the list in the Listbox.

Enter the new quantity in the "Quantity" field.

Click the Update Quantity button to update the item.

Show Total Cost:

Click the Show Total Cost button to view the total cost of all items in the shopping list, which is calculated as:

Total Cost
=∑(Quantity×Price)
Total Cost=∑(Quantity×Price)

Save List:

Click the Save List button to save the current shopping list to a JSON file (shopping_list.json).

Load List:

Click the Load Saved List button to load the shopping list from the shopping_list.json file (if available).
Functionality Details:

save_list(): Saves the current shopping list to a JSON file named shopping_list.json.

load_list(): Loads the shopping list from the shopping_list.json file (if available).

add_item(): Adds an item with its quantity, price, and category to the shopping list.

remove_item(): Removes a selected item from the list.

update_quantity(): Updates the quantity of a selected item.

total_cost(): Computes the total cost of all items in the shopping list.


