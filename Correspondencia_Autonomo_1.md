# El diagrama del Autónomo 1 es la base del proyecto

Fuente: diagrama de flujo de la página 4 del primer aprendizaje autónomo.
La imagen original está en `diagramas/Diagrama_original_Autonomo_1.png`.
Se conserva sin modificar. La versión Mermaid documenta la misma lógica.

| Paso del diagrama original | Implementación en juego.py |
| --- | --- |
| Inicio | Importar módulos y crear la ventana raíz. |
| Mostrar instrucciones: 1, 2 y 3 | `messagebox.showinfo` dentro de `while seguir`. |
| Solicitar opción al jugador | Llamar a `simpledialog.askstring`. |
| Ingresar opción del jugador | Guardar el texto en `jugador`. |
| ¿Es 1, 2 o 3? | `es_opcion_valida(jugador)` en `logica.py`. |
| No: mostrar error y volver a instrucciones | `showerror` y `continue`. |
| Sí: el sistema selecciona aleatoriamente | `random.choice(["1", "2", "3"])`. |
| Comparar elecciones | Comparar los valores del jugador y de la computadora. |
| ¿Empate? | `if jugador == computadora` en `determinar_resultado`, dentro de `logica.py`. |
| Sí: empate | Mostrar resultado de empate. |
| No: determinar ganador | `determinar_resultado` comprueba 1 contra 3, 2 contra 1 y 3 contra 2. |
| Mostrar resultado | `messagebox.showinfo("Resultado", ...)`. |
| Jugar de nuevo | `messagebox.askyesno` actualiza `seguir`. |
| Sí: nueva partida | Volver a instrucciones mediante `while seguir`. |
| No: salida | Terminar el bucle y ejecutar `ventana.destroy()`. |

## Aclaraciones del dibujo original

- El último óvalo dice «Inicio», pero recibe la rama No de jugar de nuevo.
  Se interpreta como Fin, como ya explica el Autónomo 2.
- La salida Sí de «Jugar de nuevo» no tiene una flecha dibujada en la imagen.
  La función de repetir está especificada en el texto de ambos deberes.
  El bucle vuelve al bloque de instrucciones para comenzar otra partida.
- La rama de empate muestra el empate y llega a la pregunta de repetir.
  El código usa un mismo cuadro de resultado para mostrar empate o ganador.

## Complementos del Autónomo 2 y presentación de resultados

Cancelar la entrada permite salir, como ya se documentó en el segundo deber.
Mostrar los nombres y la regla de victoria aporta información al resultado,
sin modificar las condiciones ni el orden del diagrama original.

La validación exige exactamente «1», «2» o «3». Se retiró la eliminación
de espacios para conservar la decisión del diagrama sin añadir pasos.

## Qué se corrigió tras la revisión visual

El código anterior mostraba las instrucciones solo al iniciar y admitía
espacios externos. Ahora muestra instrucciones también después de un error
y al repetir, y comprueba literalmente 1, 2 o 3. Las pruebas verifican ambos
retornos al bloque de instrucciones.

## Integración de la Unidad 4 de las instrucciones

La validación y comparación se organizan ahora en funciones puras de logica.py.
Los mensajes, el azar y la repetición permanecen en juego.py. map aplica
nombre_jugada a las dos opciones. Esto añade técnicas funcionales sin cambiar
las reglas ni las ramas del diagrama original.

## Informe del Autónomo 2 cotejado con su ZIP
El PDF describe la etapa secuencial sin funciones propias, con Python, Tkinter,
validación, condicionales y while. Esa descripción coincide con el juego.py
del ZIP. Las funciones puras y map pertenecen a la integración de la Unidad 4,
no a una alteración retroactiva de los deberes originales.
