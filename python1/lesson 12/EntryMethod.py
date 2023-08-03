import tkinter as tk

def focus1():
    inpt1.focus()

def focus2():
    inpt2.focus()

def erasetext():
    inpt3.delete(0 , tk.END)

def insertext():
    inpt3.insert(tk.INSERT, " Inserted text")

def appendtext():
    inpt3.insert(tk.END, " Appended Text")

window = tk.Tk()
window.title("Input Field Methods")
window.geometry("400x400")

lbl1 = tk.Label(window, text="What function available for Entry Widget ?")
lbl2 = tk.Label(window, text="We have a function to focus to a specific entry")
inpt1 = tk.Entry(window, width = 20)
inpt2 = tk.Entry(window, width = 20)
btn1 = tk.Button(window, text="Focus on First Entry",command = focus1)
btn2 = tk.Button(window, text="Focus on Second Entry", command = focus2)
lbl3 = tk.Label(window, text="We can also configure the text inside the entry using several functions")
inpt3 = tk.Entry(window, width = 20)
btn3 = tk.Button(window, command = erasetext, text="Erase Text")
btn4 = tk.Button(window, command = insertext, text="Insert Text (depends on cursor position)")
btn5 = tk.Button(window, command = appendtext, text="Append Text (always from last position of text)")
lbl4 = tk.Label(window, text = "By using insert function, we can have a default text available for the entry")
inpt4 = tk.Entry(window, width = 20)
inpt4.insert(0, "Enter Your Name")

lbl1.pack()
lbl2.pack()
inpt1.pack()
inpt2.pack()
btn1.pack()
btn2.pack()
lbl3.pack()
inpt3.pack()
btn3.pack()
btn4.pack()
btn5.pack()
lbl4.pack()
inpt4.pack()

window.mainloop()