# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import *
from tkinter.ttk import *
#from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.geometry('400x250')
root.title("8p2-certification GmbH")
root.iconbitmap("favicon.ico")


def open_file():
    global file
    file = askopenfile(initialdir="C:/Users/Asus/Desktop/Git Hub toki07/toki07", filetypes=[
        ('CSV Files', '*.csv'), ('All Files', '*.*')])


def see_graph():

    df = pd.read_csv(file)
    df.reset_index(drop=True)

    df.columns = ['no.', 'Real Power',
                  'Reactive Power Plant', 'Reactive Power Grid']

    y_axis = df['Real Power']
    rpg = df['Reactive Power Plant']
    rpp = df['Reactive Power Grid']

    plt.plot(rpp, y_axis, '-b', label='Real Power(P)')
    plt.plot(rpg, y_axis, '-r',  label='Reactive Power(Q)')
    plt.ylabel('P in p.u.', fontsize=12, fontfamily='Arial')
    plt.xlabel('Q in MVar', fontsize=12, fontfamily='Arial')
    plt.legend(loc='best')
    plt.title('PQ Diagram')
    plt.grid()
    plt.show()
    print(see_graph())


button_open = Button(root, text='Open', command=lambda: open_file())
button_open.grid(row=2, column=1)
button_open = Button(root, text='Plot Graph', command=lambda: see_graph())
button_open.grid(row=3, column=1)
button_exit = Button(root, text='Exit', command=root.quit)
button_exit.grid(row=4, column=1)


mainloop()
