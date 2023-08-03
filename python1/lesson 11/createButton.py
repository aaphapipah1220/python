import tkinter

window = tkinter.Tk()
window.title("Button Widget")
window.geometry("500x500")

btn = tkinter.Button(window, text="This is a Button")
btn.pack()
btn2 = tkinter.Button(window, text="This is a Button with Configuration", fg="red", bg="yellow")
btn2.pack()

window.mainloop()