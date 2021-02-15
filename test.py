from tkinter import *
from tkinter import ttk

root = Tk()
main = ttk.Frame(root)
main.grid(column=0, row=0, sticky=(N, W, E, S))
button = ttk.Button(main)

label = ttk.Label(root, text='Full name:')

resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display')

ttk.Label(main, textvariable=resultsContents).grid(column=1, row=1, sticky=(W, E))

root.mainloop()

