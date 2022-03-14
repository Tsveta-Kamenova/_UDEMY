import tkinter as tk

window = tk.Tk()
frame = tk.Frame(background="black")
frame.pack(side=tk.BOTTOM)

w = tk.Label(frame, text="Flowers",)
w.pack(padx=5, pady=5, )

window.mainloop()
