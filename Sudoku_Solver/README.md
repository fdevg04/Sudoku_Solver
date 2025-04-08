# Solucionador de Sudoku NxN

Este proyecto implementa un solucionador de sudokus de tamaño NxN utilizando la metodología **backtracking**. El código está escrito en Python y diseñado para ejecutarse desde la **terminal**, permitiendo al usuario ingresar un tablero personalizado directamente en consola.

## Características principales

- Soporta sudokus de tamaño **NxN** (cuadrados), como 4x4, 9x9, 16x16, etc.
- Utiliza el algoritmo **backtracking** para encontrar una solución válida al tablero.
- Entrada del usuario a través de la **terminal** en formato texto.
- El tablero debe introducirse línea por línea, separando cada número con un espacio.
- Las **celdas vacías** deben representarse con un `0`.
- Si no existe una solución válida para el tablero ingresado, el programa no devuelve ningún resultado.

## Ejemplo de uso

Tablero inicial (Sudoku 4x4):

```
0 0 0 3
0 4 0 0
0 0 3 2
0 0 0 0
```

Este tablero se introduce manualmente en la terminal al ejecutar el programa. Luego, el solucionador muestra la siguiente solución:

```
1 2 4 3
3 4 2 1
4 1 3 2
2 3 1 4
```

## Cómo ejecutar el programa

1. Abre una terminal en el directorio del proyecto.
2. Ejecuta el script principal con:

```bash
python main.py
```

3. Ingresa las filas del tablero una por una. Recuerda:
   - Separa los números con espacios.
   - Usa `0` para indicar las casillas vacías.

## Requisitos

- Python 3.x

No se requiere ninguna librería externa.

## Consideraciones

- Este programa no incluye una interfaz gráfica.
- Toda la interacción con el usuario se realiza a través de la terminal.
- En caso de que el tablero no tenga solución, no se mostrará ningún resultado.

## Autor

- Fernando González
- Ana Laura Mora
- Pablo Sandí
