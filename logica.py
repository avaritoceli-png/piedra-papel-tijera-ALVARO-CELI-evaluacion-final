"""Funciones puras del juego: reciben datos y devuelven resultados.

No abren ventanas, no generan azar y no modifican variables externas.
La lógica procede del diagrama del Aprendizaje Autónomo 1.
"""


def es_opcion_valida(opcion):
    """Acepta exactamente las opciones 1, 2 y 3 del diagrama."""
    return opcion in ("1", "2", "3")


def nombre_jugada(opcion):
    """Transforma una opción válida en el nombre de la jugada."""
    nombres = {"1": "Piedra", "2": "Papel", "3": "Tijera"}
    return nombres[opcion]


def determinar_resultado(jugador, computadora):
    """Las mismas jugadas siempre producen el mismo mensaje."""
    if not es_opcion_valida(jugador) or not es_opcion_valida(computadora):
        raise ValueError("Las jugadas deben ser 1, 2 o 3.")

    if jugador == computadora:
        return "Empate. Ambos eligieron la misma jugada."
    elif jugador == "1" and computadora == "3":
        return "Ganaste. Piedra vence a tijera."
    elif jugador == "2" and computadora == "1":
        return "Ganaste. Papel vence a piedra."
    elif jugador == "3" and computadora == "2":
        return "Ganaste. Tijera vence a papel."
    else:
        if computadora == "1":
            regla = "Piedra vence a tijera."
        elif computadora == "2":
            regla = "Papel vence a piedra."
        else:
            regla = "Tijera vence a papel."
        return "Ganó la computadora. " + regla
