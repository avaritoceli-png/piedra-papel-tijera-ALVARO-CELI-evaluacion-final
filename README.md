# Piedra, Papel o Tijera

## Datos del proyecto

- **Universidad:** Universidad Internacional del Ecuador (UIDE).
- **Carrera:** Ingeniería en Inteligencia Artificial.
- **Asignatura:** Lógica de Programación.
- **Integrante:** Alvaro Ivan Celi Paladines.
- **Fecha:** 11 de octubre de 2026.

## Objetivo del sistema

Desarrollar un juego local en Python y Tkinter que aplique lógica de programación y explique el resultado de cada partida, integrando el análisis, el diseño y la implementación trabajados en la asignatura.

## Descripción del proyecto

El programa permite jugar Piedra, Papel o Tijera contra la computadora. El jugador escribe una opción y la computadora elige su jugada al azar. Luego se comparan las dos jugadas y se muestra quién ganó o si hubo empate, junto con la regla aplicada.

El proyecto parte del diagrama del Aprendizaje Autónomo 1 y continúa el programa desarrollado en el Aprendizaje Autónomo 2.

## Funcionalidades

- Mostrar las instrucciones del juego.
- Pedir al jugador una opción: 1 para Piedra, 2 para Papel o 3 para Tijera.
- Mostrar un mensaje de error si la opción no es válida y permitir corregirla.
- Elegir la jugada de la computadora al azar.
- Mostrar ambas jugadas y el resultado de la partida.
- Explicar la regla que determina al ganador.
- Permitir jugar otra partida o salir voluntariamente.
- Permitir salir al pulsar Cancelar en la entrada de la jugada.

## Reglas del juego

- Piedra vence a Tijera.
- Papel vence a Piedra.
- Tijera vence a Papel.
- Si ambas jugadas son iguales, hay empate.

## Cómo ejecutar el juego

Se necesita una computadora con Python 3 y Tkinter. No se necesitan paquetes adicionales ni conexión a Internet durante la partida.

1. Descargar los archivos del repositorio y descomprimirlos si están en un ZIP.
2. Mantener `juego.py` y `logica.py` en la misma carpeta.
3. Abrir una terminal en esa carpeta.
4. Ejecutar:

```bash
python3 juego.py
```

En Windows también se puede usar:

```bash
py juego.py
```

Para comprobar que Tkinter esté disponible, se puede ejecutar `python3 -m tkinter`.

## Archivos del proyecto

| Archivo o carpeta | Contenido |
| --- | --- |
| `juego.py` | Muestra las ventanas, elige la jugada de la computadora y permite repetir. |
| `logica.py` | Revisa las opciones y determina el resultado. |
| `verificar_juego.py` | Comprueba las reglas y otros pasos del juego. |
| `diagramas/` | Contiene el diagrama original, los diagramas de funcionalidad y arquitectura y sus archivos editables. |
| `antecedentes/autonomo_2/` | Conserva el código del trabajo anterior. |
| `README.md` | Explica el objetivo, las funciones y cómo ejecutar el proyecto. |

## Relación con las cuatro unidades

- **Unidad 1:** definición del problema y preparación de los diagramas.
- **Unidad 2:** preparación del entorno y desarrollo del primer avance.
- **Unidad 3:** uso de condiciones para decidir el resultado y de repetición para jugar nuevamente.
- **Unidad 4:** organización de tareas en funciones que reciben datos y devuelven una respuesta. La función que compara devuelve el mismo resultado cuando recibe las mismas jugadas.

## Pruebas

Para ejecutar las comprobaciones:

```bash
python3 verificar_juego.py
```

Se comprobaron las nueve combinaciones posibles: tres empates, tres victorias del jugador y tres victorias de la computadora. También se revisaron entradas incorrectas, cancelar, repetir y salir. Los ganadores coinciden con los del programa del Autónomo 2.

Estas comprobaciones revisan la lógica con respuestas preparadas. Para revisar las ventanas y la interacción, se debe abrir el juego en la computadora.

## Limitaciones y posibles mejoras

El juego no guarda partidas ni tiene marcador. En una futura versión se podrían agregar botones para elegir y un contador de victorias. No se ha comprobado con un grupo de estudiantes si mejora su aprendizaje.

## Fuentes de apoyo

- Celi Paladines, A. I. (2026). Aprendizaje Autónomo 1 y Aprendizaje Autónomo 2. Trabajos de la asignatura Lógica de Programación, UIDE.
- [Documentación de Tkinter](https://docs.python.org/es/3/library/tkinter.html).
- [Selección aleatoria en Python](https://docs.python.org/es/3/library/random.html#random.choice).
- [Funciones en Python](https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions).
- [Inicio rápido para repositorios en GitHub](https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories).
