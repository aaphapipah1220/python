import tkinter as tk

window = tk.Tk()
window.title("Creating Radio Button")
window.geometry("400x400")

label1 = tk.Label(window, text="We can make a radio button as a way for user give input")
rad1 = tk.Radiobutton(window, text="1")
rad2 = tk.Radiobutton(window, text="2")

label1.pack()
rad1.pack()
rad2.pack()

window.mainloop()