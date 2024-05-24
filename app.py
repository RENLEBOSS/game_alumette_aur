import tkinter as tk
from tkinter import ttk, messagebox
import random


def run_simulation():

    try:
        essai = int(entry.get())
        if essai <= 0:
            raise ValueError("Le nombre d'essais doit être positif.")
    except ValueError as e:
        messagebox.showerror("Erreur", f"Entrée invalide: {e}")
        return

    moy = 0

    progress_bar['value'] = 0
    progress_bar['maximum'] = essai

    for i in range(essai):

        l = 1000000000
        i2 = 0
        while l > 0:
            result = random.randrange(0, l, 1)
            i2 += 1
            l = result
            if result == 0:
                moy += i2
        progress_bar['value'] = i + 1
        root.update_idletasks()  

    moyenne = moy / essai
    messagebox.showinfo("Résultat", f"Moyenne : {moyenne}")


root = tk.Tk()
root.title("Simulation Moyenne")

title_label = tk.Label(root, text="Simulation Moyenne", font=("Helvetica", 16))
title_label.pack(pady=10)


description_label = tk.Label(root, text="Entrez le nombre d'essais et cliquez sur le bouton pour lancer la simulation.")
description_label.pack(pady=5)

entry_label = tk.Label(root, text="Nombre d'essais :")
entry_label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

run_button = tk.Button(root, text="Lancer la simulation", command=run_simulation, bg="blue", fg="white")
run_button.pack(pady=10)


root.mainloop()
