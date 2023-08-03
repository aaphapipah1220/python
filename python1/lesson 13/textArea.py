import tkinter as tk

window = tk.Tk()
window.title("Text area")
window.geometry("500x400")

#function to get text area
def getText():
    inputText1 = textArea.get("1.0","end-1c")
    inputText2 = textArea2.get("1.0","end-1c")
    label3.config(text=inputText1 + " " + inputText2)

label = tk.Label(window, text="Dibawah ini merupakan text area")
textArea = tk.Text(window, height=5, width=30)
textArea.insert(tk.END, "You can type here")
labelKosong1 = tk.Label(window)

label.pack()
textArea.pack()
labelKosong1.pack()

label2 = tk.Label(window, text="You can get the value from your text area")
textArea2 = tk.Text(window, height=5, width=30)
textArea2.insert(tk.END, "You can type here")
labelKosong2 = tk.Label(window)

label2.pack()
textArea2.pack()
labelKosong2.pack()

button = tk.Button(window, text="Get Text", command= getText)
label3 = tk.Label(window)
labelKosong3 = tk.Label(window)

button.pack()
label3.pack()
labelKosong3.pack()


window.mainloop()