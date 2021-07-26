import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd


def import_csv_data():
    global v
    csv_file_path = askopenfilename(mode='r', initialdir="C:/Users/Asus/Desktop/Git Hub toki07/toki07", filetypes=[
        ('CSV Files', '*.csv'), ('All Files', '*.*')])

    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path)
    return df

root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set',
          command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Close', command=root.destroy).grid(row=1, column=1)
root.mainloop()
