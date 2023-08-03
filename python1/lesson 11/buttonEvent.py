import tkinter

def changetext():
    lbl.configure(text="I am a Label", fg="red", bg="black")

window = tkinter.Tk()
window.title("Clicking the Button")
window.geometry("500x500")

btn = tkinter.Button(window, text="Click Me !", command=changetext)
btn.pack()
lbl = tkinter.Label(window)
lbl.pack()

window.mainloop()