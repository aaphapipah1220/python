import tkinter as tk

window = tk.Tk()
window.title("Checkbox")
window.geometry("500x400")

# function
def printSelection():
    print(checkValue2.get())

check = tk.Checkbutton(window, text="Checkbox 1")
check2 = tk.Checkbutton(window, text="Checkbox 2")
check.select()
check.deselect()
check.toggle()
check.pack()
check2.pack()

# variable
checkValue = tk.BooleanVar()
checkValue.set(True)

check3 = tk.Checkbutton(window, text="I am selected using variable", variable=checkValue)
check3.pack()

# variable
checkValue2 = tk.StringVar()
checkValue2.set("True")

check4 = tk.Checkbutton(window, text="example", onvalue="This is example", offvalue="", variable=checkValue2, command=printSelection)
check4.pack()

window.mainloop()