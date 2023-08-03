import tkinter as tk

window = tk.Tk()
window.title("Getting Radio Value")
window.geometry("500x300")

def printvalue():
    print("The Value is " + radvar.get())

radvar = tk.StringVar()
radvar.set("false")

lbl1 = tk.Label(window, text="To get the radio button value, \n we need to use the tkinter variable we already learned")
rad1 = tk.Radiobutton(window, text="Value 1", value = 1, var = radvar, command = printvalue)

lbl1.pack()
rad1.pack()

window.mainloop()