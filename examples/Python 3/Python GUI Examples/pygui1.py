import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0,0)

# Modified Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# Button Click Event Handler
def clickMe():
    action.configure(text="** I have been Clicked! **")
    aLabel.configure(foreground='red')
    aLabel.configure(text='A Red Label')

#Add a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)

win.mainloop()