import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0,0)

# Button Click Event Handler
def clickMe():
    action.configure(text='Hello' + name.get())

#Change the label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

#Add a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

#Add a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)

win.mainloop()