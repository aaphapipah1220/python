import tkinter as tk

def gettext():
    inpttext = inpt2.get()
    lbl3.config(text=inpttext)

window = tk.Tk()
window.title("Creating Input Field")
window.geometry("500x500")

lbl1 = tk.Label(window, text="This is an input field")
inpt1 = tk.Entry(window, width = 50)
lbl2 = tk.Label(window, text="We can get the inputted text inside the field")
inpt2 = tk.Entry(window, width = 50)
btn1 = tk.Button(window, text="Get Text", command = gettext)
lbl3 = tk.Label(window)

lbl1.pack()
inpt1.pack()
lbl2.pack()
inpt2.pack()
btn1.pack()
lbl3.pack()

window.mainloop()