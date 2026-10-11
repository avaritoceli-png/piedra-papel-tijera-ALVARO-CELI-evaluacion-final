"""Piedra, Papel o Tijera. Ejecutar con: python3 juego.py."""
import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from logica import es_opcion_valida, nombre_jugada, determinar_resultado

ventana = tk.Tk()
ventana.withdraw()
seguir = True

while seguir:
    # El diagrama del Autónomo 1 vuelve aquí después de un error
    # y al comenzar otra partida.
    messagebox.showinfo(
        "Piedra, Papel o Tijera",
        "1 = Piedra\n2 = Papel\n3 = Tijera\n\n"
        "Piedra vence a tijera. Papel vence a piedra. Tijera vence a papel.\n"
        "Si ambos eligen lo mismo, hay empate. Puedes cancelar para salir.",
        parent=ventana,
    )
    jugador = simpledialog.askstring(
        "Tu jugada", "Escribe una opción:\n1 = Piedra\n2 = Papel\n3 = Tijera",
        parent=ventana,
    )
    if jugador is None:
        break
    if not es_opcion_valida(jugador):
        messagebox.showerror("Opción inválida", "Escribe 1, 2 o 3.", parent=ventana)
        continue

    computadora = random.choice(["1", "2", "3"])
    resultado = determinar_resultado(jugador, computadora)
    # map aplica la misma función pura a las dos opciones, sin cambiarlas.
    nombre_jugador, nombre_computadora = map(nombre_jugada, (jugador, computadora))

    messagebox.showinfo(
        "Resultado",
        "Tú: " + nombre_jugador + "\nComputadora: " + nombre_computadora
        + "\n\n" + resultado,
        parent=ventana,
    )
    seguir = messagebox.askyesno("Otra partida", "¿Quieres jugar de nuevo?", parent=ventana)

ventana.destroy()
