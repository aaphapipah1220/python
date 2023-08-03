import tkinter

def changetext():
    btn2.configure(text="the text is changing !")

def clrlabel():
    lbl5.configure(fg="red", bg="black")

def clrbtn():
    btn4.configure(fg="blue", bg="orange")

def countclick():
    global totalclick
    totalclick = totalclick + 1
    newstr = "You have click the button " + str(totalclick) + " time(s)"
    lbl7.configure(text=newstr)

totalcl
ick  = 0

window = tkinter.Tk()
window.title("My Attempt on Creating GUI")
window.geometry("360x500")

lbl = tkinter.Label(window, text="This is a simple GUI i created using tkinter library")
lbl2 = tkinter.Label(window, text="This is a label which have a lot of usage")
lbl3 = tkinter.Label(window, text="There is also a button where if we clicked it, something will happen")
btn = tkinter.Button(window, text="This is a button, try to click me")
lbl4 = tkinter.Label(window, text="Nothing happens, now let's try this one")
btn2 = tkinter.Button(window, text="click me", command=changetext)
lbl5 = tkinter.Label(window, text="we can also change color")
btn3 = tkinter.Button(window, text="Click me to change the label's color", command=clrlabel)
btn4 = tkinter.Button(window, text="Click me to change the color of the button", command=clrbtn)
lbl6= tkinter.Label(window, text="we can also do something like a counting function")
btn5= tkinter.Button(window, text="Click to increase your counter", command = countclick)
lbl7= tkinter.Label(window, text="")

lbl.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl3.grid(column=0, row=2)
btn.grid(column =0, row =3)
lbl4.grid(column=0, row=4)
btn2.grid(column=0, row=5)
lbl5.grid(column=0, row=6)
btn3.grid(column=0, row=7)
btn4.grid(column =0 ,row=8)
lbl6.grid(column=0, row=9)
btn5.grid(column=0, row=10)
lbl7.grid(column=0, row=11)

window.mainloop()