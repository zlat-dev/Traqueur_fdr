import tkinter as tk
import random

def generate_numbers():
    numbers = random.sample(range(1, 51), 7)
    result_label.config(text=", ".join(map(str, numbers)))

# Créer la fenêtre principale
root = tk.Tk()
root.title("Générateur de 7 Chiffres aléatoires")

# Créer un label pour afficher les résultats
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Créer un bouton pour générer les chiffres
generate_button = tk.Button(root, text="Générer les chiffres", command=generate_numbers)
generate_button.pack(pady=10)

# Lancer la boucle principale de l'application
root.mainloop()