import tkinter as tk
import googletrans
import textblob
from tkinter import ttk, messagebox


window = tk.Tk()
window.title("Kodingnext -  Translator")
window.geometry("880x400")

#function
def translate_it():
	# Delete Any Previous Translations
	translated_text.delete("1.0", "end-1c")

	try:
		# Get Languages From Dictionary Keys
		# Get the From Langauage Key
		for key, value in languages.items():
			if (value == original_combo.get()):
				from_language_key = key

		# Get the To Language Key
		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key

		# Turn Original Text into a TextBlob
		words = textblob.TextBlob(original_text.get("1.0", "end-1c"))

		# Translate Text
		words = words.translate(from_lang=from_language_key , to=to_language_key)

		# Output translated text to screen
		translated_text.insert(1.0, words)

	except:
		messagebox.showerror("Translator", "Please fill the entry fields or combobox")


def clear():
	# Clear the text boxes
	original_text.delete("1.0", "end-1c")
	translated_text.delete("1.0", "end-1c")

#widget

lbl1 = tk.Label(window, text = "Your Translator" ,font = ("calbiri",20) )
original_text = tk.Text(window, height=10, width=40)
translated_text = tk.Text(window, height=10, width=40)


# Grab Language List From GoogleTrans
languages = googletrans.LANGUAGES

# Convert to list
language_list = list(languages.values())
# Combo boxes
original_combo = ttk.Combobox(window, width=50,state = "readonly", value=language_list )
# original_combo.current(21)


translated_combo = ttk.Combobox(window, width=50,state = "readonly",value=language_list)
# translated_combo.current(26)


translate_button = tk.Button(window, text="Translate!", font=("Helvetica", 24), command=translate_it)
clear_button = tk.Button(window, text="Clear", font=("Helvetica", 24), command=clear)
#placement
lbl1.grid(row=0, column= 1)
original_text.grid(row= 2, column=0, pady=20, padx=10)
translated_text.grid(row=2, column=2, pady=20, padx=10)
translated_combo.grid(row=1, column=2)
original_combo.grid(row=1, column=0)
translate_button.grid(row=3, column=0, padx=10)
clear_button.grid(row=3, column=1, rowspan = 100,columnspan = 20)
window.mainloop()