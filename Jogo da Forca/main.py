import tkinter as tk
from tkinter import messagebox
import random
animais = ["ovelha", "pato", "ganso", "lula", "formiga", "coelho", "pavão", "baiacu", "carpa", "jiboia"]
frutas = ["manga", "morango", "caqui", "goiaba", "mexerica", "coco", "kiwi", "cereja", "limão", "framboesa"]

window = tk.Tk()
window.title("Jogo da Forca")
window.geometry("400x400")
label = tk.Label(window, text= "Adivinhe a palavra", font = ("Helvetica", 16))
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Chutar", command= lambda: check_animais())
button.pack()

lives_label = tk.Label(window, text= "Vidas sobrando: 6", font=("Helvetica"))

canvas = tk.Canvas(window, width = 200, height=200)
canvas.pack()

canvas.create_line(50, 50, 150, 50)  # Topo da forca
canvas.create_line(100, 50, 100, 100)  # Tronco da forca

def draw_hangman(lives):
    if lives == 5:
        canvas.create_oval(90, 100, 110, 120)  # Cabeça
    elif lives == 4:
        canvas.create_line(100, 120, 100, 170)  # Corpo
    elif lives == 3:
        canvas.create_line(100, 120, 130, 150)  # Braço direito
    elif lives == 2:
        canvas.create_line(100, 120, 70, 150)  # Braço esquerdo
    elif lives == 1:
        canvas.create_line(100, 170, 130, 200)  # Perna direita
    elif lives == 0:
        canvas.create_line(100, 170, 70, 200)  # Perna esquerda

palavra_animais = random.choice(animais)
palavra_frutas = random.choice(frutas)

adivinhar_animais = ["_"] * len(palavra_frutas)
adivinhar_frutas = ["_"] * len(palavra_animais)
lives = 6

def check_animais():
    global lives
    chute = entry.get()
    entry.delete(0, "end")

    if chute in palavra_animais:
        for i in range(len(palavra_animais)):
            if palavra_animais[i] == chute:
                adivinhar_animais[i] = chute
        label.config(text=" ".join(adivinhar_animais))

        if "".join(adivinhar_animais) == palavra_animais:
            messagebox.showinfo("Você venceu!", f"A palavra era: {palavra_animais}!")
        else:
            lives -= 1
            lives_label.config(text=f"Lives remaining: {lives}.")
            draw_hangman(lives)
        if lives == 0:
            messagebox.showinfo("Você perdeu!", f"A palavra era: {palavra_animais}!")


def check_frutas():
    global lives
    chute = entry.get()
    entry.delete(0, "end")

    if chute in palavra_frutas:
        for i in range(len(palavra_frutas)):
            if palavra_frutas[i] == chute:
                adivinhar_frutas[i] = chute
        label.config(text=" ".join(adivinhar_frutas))

        if "".join(adivinhar_frutas) == palavra_frutas:
            messagebox.showinfo("Você venceu!", f"A palavra era: {palavra_frutas}!")
        else:
            lives -=1
            lives_label.config(text=f"Lives remaining: {lives}.")
            draw_hangman(lives)
        if lives == 0:
            messagebox.showinfo("Você perdeu!", f"A palavra era: {palavra_frutas}!")

window.mainloop()