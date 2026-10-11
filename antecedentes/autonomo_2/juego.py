import tkinter as tk
from tkinter import simpledialog, messagebox
import random

ventana = tk.Tk()
ventana.withdraw()
seguir = True

# El bucle permite jugar varias veces.
while seguir:
    jugador = simpledialog.askstring(
        "Elige tu jugada", "1 = Piedra\n2 = Papel\n3 = Tijera"
    )

    if jugador is None:
        break

    # Si la opción es incorrecta, el bucle vuelve a pedirla.
    if jugador not in ["1", "2", "3"]:
        messagebox.showerror("Error", "Escribe 1, 2 o 3")
    else:
        computadora = random.choice(["1", "2", "3"])

        if jugador == computadora:
            resultado = "Empate"
        elif jugador == "1" and computadora == "3":
            resultado = "Ganaste"
        elif jugador == "2" and computadora == "1":
            resultado = "Ganaste"
        elif jugador == "3" and computadora == "2":
            resultado = "Ganaste"
        else:
            resultado = "Ganó la computadora"

        messagebox.showinfo(
            "Resultado",
            "1 = Piedra, 2 = Papel, 3 = Tijera\n" +
            "Tú: " + jugador + "\nComputadora: " + computadora +
            "\n" + resultado
        )
        seguir = messagebox.askyesno("Continuar", "¿Jugar de nuevo?")

ventana.destroy()
