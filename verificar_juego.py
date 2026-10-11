"""Pruebas del archivo real con diálogos y azar controlados, sin abrir ventanas."""
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch, MagicMock
from logica import determinar_resultado, es_opcion_valida, nombre_jugada

JUEGO = Path(__file__).with_name("juego.py")

def ejecutar(entradas, elecciones, respuestas, archivo=JUEGO):
    raiz = MagicMock()
    with patch("tkinter.Tk", return_value=raiz), \
         patch("tkinter.simpledialog.askstring", side_effect=entradas), \
         patch("random.choice", side_effect=elecciones) as azar, \
         patch("tkinter.messagebox.showinfo") as info, \
         patch("tkinter.messagebox.showerror") as error, \
         patch("tkinter.messagebox.askyesno", side_effect=respuestas):
        runpy.run_path(str(archivo))
    return raiz, azar, info, error

class PruebasJuego(unittest.TestCase):
    def test_conserva_resultados_del_autonomo_2(self):
        original = JUEGO.parent / "antecedentes" / "autonomo_2" / "juego.py"
        for jugador in ("1", "2", "3"):
            for computadora in ("1", "2", "3"):
                with self.subTest(jugador=jugador, computadora=computadora):
                    _, _, info_original, _ = ejecutar([jugador], [computadora], [False], original)
                    _, _, info_final, _ = ejecutar([jugador], [computadora], [False])
                    resultado_original = info_original.call_args.args[1].splitlines()[-1]
                    self.assertIn(resultado_original, info_final.call_args.args[1])

    def test_logica_independiente_de_interfaz_y_azar(self):
        # Las mismas entradas conservan el resultado en llamadas repetidas.
        # La función no debe llamar al azar ni mostrar ventanas.
        with patch("random.choice", side_effect=AssertionError("La lógica no usa azar")), \
             patch("tkinter.messagebox.showinfo", side_effect=AssertionError("La lógica no usa ventanas")):
            for _ in range(3):
                self.assertEqual(determinar_resultado("1", "3"), "Ganaste. Piedra vence a tijera.")
            self.assertTrue(es_opcion_valida("1"))
            self.assertFalse(es_opcion_valida(" 1 "))
            self.assertEqual(list(map(nombre_jugada, ("1", "3"))), ["Piedra", "Tijera"])
            with self.assertRaises(ValueError):
                determinar_resultado("4", "1")

    def test_nueve_combinaciones(self):
        esperados = {("1","1"):"Empate", ("1","2"):"Ganó la computadora",
                     ("1","3"):"Ganaste", ("2","1"):"Ganaste",
                     ("2","2"):"Empate", ("2","3"):"Ganó la computadora",
                     ("3","1"):"Ganó la computadora", ("3","2"):"Ganaste",
                     ("3","3"):"Empate"}
        for (jugador, pc), resultado in esperados.items():
            with self.subTest(jugador=jugador, computadora=pc):
                raiz, azar, info, error = ejecutar([jugador], [pc], [False])
                self.assertIn(resultado, info.call_args.args[1])
                self.assertIn("Tú:", info.call_args.args[1])
                error.assert_not_called()
                raiz.destroy.assert_called_once()

    def test_invalidos(self):
        for invalido in ["4", "letras", "", "   "]:
            with self.subTest(entrada=invalido):
                raiz, azar, info, error = ejecutar([invalido, None], [], [])
                error.assert_called_once()
                azar.assert_not_called()
                self.assertEqual(info.call_count, 2)
                raiz.destroy.assert_called_once()

    def test_cancelar(self):
        raiz, azar, info, error = ejecutar([None], [], [])
        azar.assert_not_called()
        raiz.destroy.assert_called_once()

    def test_repetir_y_salir(self):
        raiz, azar, info, error = ejecutar(["1", "2"], ["3", "2"], [True, False])
        self.assertEqual(azar.call_count, 2)
        self.assertEqual(info.call_count, 4)
        self.assertEqual(info.call_args_list[0].args[0], "Piedra, Papel o Tijera")
        self.assertEqual(info.call_args_list[2].args[0], "Piedra, Papel o Tijera")
        self.assertIn("Empate", info.call_args.args[1])
        raiz.destroy.assert_called_once()

    def test_espacios_no_son_opcion_del_diagrama(self):
        raiz, azar, info, error = ejecutar([" 1 ", None], [], [])
        error.assert_called_once()
        azar.assert_not_called()
        self.assertEqual(info.call_count, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
