# Importing necessary classes
import tkinter as tk
import tkinter.messagebox as tkm
import wikipedia
from gtts import gTTS
import os

# creating and configuring the windows

window = tk.Tk()
window.title('Wikipedia Search')
window.geometry('600x600')


# Creating the search function

def wiki_search(text):
    try:
        result = wikipedia.summary(text, sentences=6)
        return result
    except wikipedia.exceptions.PageError:
        error_message = "Page not found."
        tkm.showerror(error_message)
        return None

# Creating the text to speech function
def convert_to_speech():
    search_text = entry.get()
    summary = wiki_search(search_text)

    if summary:
        result_label.config(text=summary)

        if voice_checkbox_var.get() == 1:
            language = 'en'
            myobj = gTTS(text=summary, lang=language, slow=False)
            myobj.save('voice.mp3')
            os.system('voice.mp3')
    else:
        result_label.config(text='Nothing to show')


# Creating the input serach field
entry = tk.Entry(window, show=None, font=('Arial', 14))
entry.pack()


# Creating the result label
result_label = tk.Label(window, text='', font=('Arial', 12), wraplength=400, justify='left')
result_label.pack()

# Creating the checkbox for the text to speech option
voice_checkbox_var = tk.IntVar()
voice_checkbox = tk.Checkbutton(window, text='Play Voice', variable=voice_checkbox_var)
voice_checkbox.pack()

# Creating the click button to convert from text to speech
search_button = tk.Button(window, text='Search', command=convert_to_speech)
search_button.pack()

window.mainloop()
