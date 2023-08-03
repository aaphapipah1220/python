import tkinter

#setting window
window = tkinter.Tk()
window.geometry("600x500")
window.title("create Label Py 1")

#widgets
label = tkinter.Label(window, text="This is a label")
label.pack() #show the label

label2 = tkinter.Label(window, text="This is example for label 2", font=("Calibri", 20))
label2.pack()

label3 = tkinter.Label(window, text="This is example for label 3", font=("Arial", 25), foreground="red")
label3.pack()

#image
img = tkinter.PhotoImage(file="kupu-kupu.png")
resizeImage = img.subsample(5,5)

label4 = tkinter.Label(window, image=resizeImage)
label4.pack()

window.mainloop()