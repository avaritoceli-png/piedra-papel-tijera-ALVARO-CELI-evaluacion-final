import tkinter as tk
from tkinter import simpledialog, messagebox
import random

ventana = tk.Tk()
ventana.withdraw()

# Primera etapa: pedir la opción y mostrar ambas jugadas.
jugador = simpledialog.askstring(
    "Piedra, papel y tijera", "1 = Piedra\n2 = Papel\n3 = Tijera"
)

if jugador is None:
    messagebox.showinfo("Salir", "Juego cancelado")
elif jugador not in ["1", "2", "3"]:
    messagebox.showerror("Error", "Escribe 1, 2 o 3")
else:
    computadora = random.choice(["1", "2", "3"])
    messagebox.showinfo(
        "Jugadas", "Tu opción: " + jugador + "\nComputadora: " + computadora
    )

ventana.destroy()
