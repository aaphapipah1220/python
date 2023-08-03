import tkinter as tk

window = tk.Tk()
window.title("Radio button in category")
window.geometry("500x400")

lbl1 = tk.Label(window, text="we can categorized radio button so we can have multiple usage of radio button")
lbl2 = tk.Label(window, text="we categorized radio button using tkinter Variable whch can be used only for tkinter components")

#declaring tkinter variable
#for string data type
radvar = tk.StringVar()
#setting a value to tkinter variable
radvar.set("False")

rad1 = tk.Radiobutton(window, text = "value1", value = 1)
rad2 = tk.Radiobutton(window, text = "value2", value = 2)
rad3 = tk.Radiobutton(window, text = "value3", value = 3, var = radvar)
rad4 = tk.Radiobutton(window, text = "value4", value = 4, var = radvar)

lbl1.pack()
lbl2.pack()
rad1.pack()
rad2.pack()
rad3.pack()
rad4.pack()

window.mainloop()