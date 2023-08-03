import tkinter

window = tkinter.Tk()
window.title("Configuration of Grid Placement")
window.geometry("300x300")

lbl1 = tkinter.Label(window, text="Label 1" , bg="lightgreen")
lbl2 = tkinter.Label(window, text="Label 2", bg="lightblue")
lbl3 = tkinter.Label(window, text="Label 3", bg="pink")
lbl4 = tkinter.Label(window, text="Label 4", bg="yellow")
lbl5 = tkinter.Label(window, text="Label 5", bg="navy")
lbl6 = tkinter.Label(window, text="Label 6", bg="green")
lbl7 = tkinter.Label(window, text="Label 7", bg="brown")
btn1 = tkinter.Button(window, text="Button 1")
btn2 = tkinter.Button(window, text="Button 2")
btn3 = tkinter.Button(window, text="Button 3")
btn4 = tkinter.Button(window, text="Button 4")
btn5 = tkinter.Button(window, text="Button 5")
#label and button with internal padding
lbl1.grid(column = 0, row = 0, ipadx = 30)
btn1.grid(column = 1, row = 0, ipadx = 30)
#label and button with sticky option. label sticks to the right side, and button sticks to the left
lbl2.grid(column = 0, row = 1, sticky = tkinter.E)
btn2.grid(column = 1, row = 1, sticky = tkinter.W)
#label which is as wide as the column it is in. the button will automatically be forced to another column
lbl3.grid(column = 0, row = 2, columnspan = 2, sticky = tkinter.E+tkinter.W)
btn3.grid(column = 2, row = 2)
#normal  labels on the first column
lbl4.grid(column = 0, row = 3)
lbl5.grid(column = 0, row = 4)
lbl6.grid(column = 0, row = 5)
lbl7.grid(column = 0, row = 6)
#button which takes up two rows
btn4.grid(column = 1, row = 3, rowspan = 2, sticky = tkinter.N+tkinter.S)
#button which takes up two rows and two columns
btn5.grid(column = 1, row = 5, columnspan = 2, rowspan = 2, sticky = tkinter.S+tkinter.N+tkinter.E+tkinter.W)

window.mainloop()