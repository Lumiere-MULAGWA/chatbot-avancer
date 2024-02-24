import tkinter as tk
import customtkinter as ctk 
from tkinter import scrolledtext
import openai

# Remplacez 'YOUR_API_KEY' par votre clé d'API OpenAI
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

app = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


def ask_question(question):
    response = openai.Completion.create(
        #engine="text-davinci-002",
        model="gpt-3.5-turbo-instruct",
        prompt=question,
        max_tokens=1000
    )
    return response.choices[0].text.strip()

def send_message():
    user_input = entry.get()
    chat_history.insert(tk.END, "Vous: " + user_input + "\n")
    entry.delete(0, tk.END)
    
    response = ask_question(user_input)
    chat_history.insert(tk.END, "Chatbot: " + response + "\n")

# Créer la fenêtre principale
#root = tk.Tk()
app.title("Chatbot avec OpenAI")


# Zone de chat
chat_history = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=50, height=20)
chat_history.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
#

# Champ de saisie pour l'utilisateur
entry = ctk.CTkEntry(app, width=300,height=300)
entry.grid(row = 1, column = 0,padx=10,pady=10)

# Bouton pour envoyer le message
send_button = ctk.CTkButton(app, text="Envoyer", command=send_message)
send_button.grid(row=2, column=0,padx=10,pady=10)

app.mainloop()
