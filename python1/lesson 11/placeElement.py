import tkinter

window = tkinter.Tk()
window.title("This is an example of a place placement")
window.geometry("300x300")

lbl = tkinter.Label(window, text="This is a label", bg="lightgreen")
lbl.place(x=30, y=50, width=100, height=50)

window.mainloop()
