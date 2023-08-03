import tkinter as tk

# window
window = tk.Tk()
window.geometry("500x400")
window.title("Creating Entry")

# windgets
label1 = tk.Label(window, text="Creating Entry", font=("Calibri", 20))
entry1 = tk.Entry(window, width=50)


# placements
label1.pack()
tk.Label(window).pack() #cara menambahkan jarak dengan membuat label kosong
entry1.pack()
tk.Label(window).pack() #cara menambahkan jarak dengan membuat label kosong


window.mainloop()