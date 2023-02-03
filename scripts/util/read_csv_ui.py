import tkinter as tk
from pandastable import Table

def show_csv(path):
    root = tk.Tk()
    root.title('Data')

    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)

    pt = Table(frame)
    pt.show()

    pt.importCSV(filename=f'{path}', dialog=False)

    root.mainloop()
