import tkinter

window = tkinter.Tk()
window.title("Pack Placement")
window.geometry("500x500")

lbl = tkinter.Label(window, text="This is a label", foreground="red", bg="white")
lbl.pack()

lbl2 = tkinter.Label(window, text="This is also a label",fg="pink", bg="yellow")
lbl2.pack(fill=tkinter.X)

lbl3 = tkinter.Label(window, text="This is a label with external padding added", bg="white")
lbl3.pack(pady = 10, padx=10)

lbl4 = tkinter.Label(window, text="This is a label with internal padding added", bg="green")
lbl4.pack(ipadx =10, ipady=10)

lbl5 = tkinter.Label(window, text="This is label", bg="purple")
lbl5.pack(padx=10,side=tkinter.LEFT) #can also change with different position

lbl6 = tkinter.Label(window, text="Label beside previous label", bg="lightblue")
lbl6.pack(padx = 10, side=tkinter.BOTTOM)

lbl7 = tkinter.Label(window, text="Label beside previous label", bg="lightgreen")
lbl7.pack(padx = 10, side=tkinter.RIGHT)

window.mainloop()