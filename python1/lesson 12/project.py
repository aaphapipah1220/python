import tkinter as tk

def result():
    fname = fnameinput.get()
    lname = lnameinput.get()
    username = usernameinput.get()
    password = ""
    for i in range(0,len(passwordinput.get())):
        password = password + "*"
    email = emailinput.get()
    gender = gendervar.get()
    duration = durationspinner.get()
    text1 = "Thank you for signing up.\nyou are eligible to use the program for "+str(duration)+" days.\n"
    text2 = "The data you submitted are as follows: \n First Name : "+fname+".\nLast Name : "+lname+".\nUsername : "+username
    text3 = "\nPassword : "+password+".\nEmail : "+email+".\nGender : "+gender
    if fname != "" and lname != "" and username != "" and password != "" and email != "" and gender != "False":
        resultlbl.config(text = text1+text2+text3)
    else:
        resultlbl.config(text = "Fill all the input field with necessary information")

window = tk.Tk()
window.title("Sign Up Form")
window.geometry("400x600")

lbl1 = tk.Label(window, text="Welcome to All-Purpose Program", font=("Times New Roman", 20))
lbl2 = tk.Label(window, text="To use the program, please sign up first")
lbl3 = tk.Label(window, text="The sign up form is available below\n\n")
fnamelbl = tk.Label(window, text="First Name")
fnameinput = tk.Entry(window, width = 20)
lnamelbl = tk.Label(window, text="Last Name")
lnameinput = tk.Entry(window, width = 20)
usernamelbl = tk.Label(window, text="Username")
usernameinput = tk.Entry(window, width = 20)
passwordlbl = tk.Label(window, text="Password")
passwordinput = tk.Entry(window, show="*", width = 20)
emaillbl = tk.Label(window, text = "Email")
emailinput = tk.Entry(window, width = 20)
genderlbl = tk.Label(window, text = "Gender")

gendervar = tk.StringVar()
gendervar.set("False")
gender1 = tk.Radiobutton(window, value="Male", text="Male", variable = gendervar)
gender2 = tk.Radiobutton(window, value="Female", text="Female", variable = gendervar)

durationlbl = tk.Label(window, text="Duration of Usage(Maximum 30 days)")
durationspinner = tk.Spinbox(window, from_ = 1, to = 30, state = "readonly")
submitbtn = tk.Button(window, text="Submit Data", command = result)
resultlbl = tk.Label(window)

lbl1.pack()
lbl2.pack()
lbl3.pack()
fnamelbl.pack()
fnameinput.pack()
lnamelbl.pack()
lnameinput.pack()
usernamelbl.pack()
usernameinput.pack()
passwordlbl.pack()
passwordinput.pack()
emaillbl.pack()
emailinput.pack()
genderlbl.pack()
gender1.pack()
gender2.pack()
durationlbl.pack()
durationspinner.pack()
submitbtn.pack()
resultlbl.pack()

window.mainloop()