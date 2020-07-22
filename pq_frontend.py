# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog
# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.geometry('400x250')
root.title("8p2-certification GmbH")
root.iconbitmap("favicon.ico")
# This function will be used to open
# file in read mode and only Python files
# will be opened
"""file = askopenfile(mode='r', filetypes=[  # initialdir="C:/Users/nn/Downloads",
        ('CSV Files', '*.csv'), ('All Files', '*.*')])"""


def open_file():
    file = askopenfile(mode='r', initialdir="C:/Users/nn/Downloads", filetypes=[
        ('CSV Files', '*.csv'), ('All Files', '*.*')])
    """root.filename = filedialog.askopenfilename( mode='r',
    initialdir='C:/Users/nn/Downloads', title='Open File', filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))"""


button_open = Button(root, text='Open', command=lambda: open_file())
button_open.grid(row=2, column=1)
button_exit = Button(root, text='Exit', command=root.quit)
button_exit.grid(row=3, column=1)


mainloop()
