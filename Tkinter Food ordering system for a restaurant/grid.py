import tkinter as tk

window = tk.Tk()

for x in range(3):
    for y in range(3):
        label = tk.Label(window, text=f"Row {x} \n Column {y}", relief=tk.RAISED, borderwidth=1)
        label.grid(row=x, column=y)

label = tk.Label(window, text=f"This is a wide label - 3 columns", relief=tk.RAISED, borderwidth=1)
label.grid(row=3, column=0, columnspan=3)

window.mainloop()
