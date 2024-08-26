#############################################################################
#Improved SQL and Panda
#############################################################################

import pandas as pd
import sqlalchemy
import tkinter as tk
from tkinter import ttk

# Correct the path to your SQLite database
database_url = 'sqlite:///C:/Users/User/Downloads/linuxpeer/northwind-SQLite3/dist/northwind.db'

# Connect to the database
engine = sqlalchemy.create_engine(database_url)

# Update the query with the correct table name
query = "SELECT * FROM Customers"
try:
    df = pd.read_sql(query, engine)
except Exception as e:
    print(f"Error reading from SQL: {e}")
    df = pd.DataFrame()  # Create an empty DataFrame on error

# Set up the Tkinter GUI
root = tk.Tk()
root.title("SQL Data Viewer")

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a Treeview widget
tree = ttk.Treeview(frame)

# Add a scrollbar to the Treeview
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

# Define the columns
if not df.empty:
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    # Add the columns and set the column headings
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.W, width=150)  # Adjust width as needed

    # Add the DataFrame rows to the Treeview
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
else:
    print("No data available to display.")

tree.pack(fill=tk.BOTH, expand=True)

# Start the GUI event loop
root.mainloop()
