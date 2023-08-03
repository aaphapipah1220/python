import tkinter as tk

window = tk.Tk()
window.title("Creating radio selection with Value")
window.geometry("500x400")

lbl1 = tk.Label(window, text="To be able to select the radiobutton, we need to separate them into different groups")
lbl2 = tk.Label(window, text="Because when using radio button as input, user can only give one input")
rad1 = tk.Radiobutton(window, text="Value 1", value = 1)
rad2 = tk.Radiobutton(window, text="Value 2", value = 2)

lbl1.pack()
lbl2.pack()
rad1.pack()
rad2.pack()

window.mainloop()