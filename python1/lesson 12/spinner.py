import tkinter as tk

def printvalue():
    print(spin3.get())

window = tk.Tk()
window.title("Creating Spinner")
window.geometry("500x300")

lbl1 = tk.Label(window, text="we can create a spinner for choosing a number")
#creating spinner
spin1 = tk.Spinbox(window, from_ = 0, to = 10, width = 10)
lbl2 = tk.Label(window, text="We can also create a spinner with chosen number")
#creating spinner with chosen number
spin2 = tk.Spinbox(window, values=(0,5,10), width = 10)
#changing state of spinner
lbl3 = tk.Label(window, text="We can change the state of the spinner so user can't edit the content of the spinner\nthe states available are Normal(default), readonly, and disabled")
spin3 = tk.Spinbox(window, from_=0, to=10, width = 20, state = "readonly")
button = tk.Button(window, text="Click for Spinner Value", command = printvalue)

lbl1.pack()
spin1.pack()
lbl2.pack()
spin2.pack()
lbl3.pack()
spin3.pack()
button.pack()

window.mainloop()