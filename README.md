## Estructura del Lenguaje

### Principio y Fin
El programa comienza con la palabra reservada `EMPEZAR` y termina con `TERMINAR`.

### Carácter de Fin de Línea
Cada línea de este lenguaje finaliza con el carácter `.`

### Librerías Externas
Este lenguaje permite incluir librerías externas. Se deben definir al inicio del archivo siguiendo la estructura:

```
extend("nombreDeLibreria.Extension")
```

Se pueden incluir varias librerías separadas por `;`.

### Tipos de Datos Admitidos
Solo se admiten los siguientes tipos de datos:
- **entero** (`int`)
- **texto** (`String`)
- **decimal** (`float`)
- **lógico** (`bool`)

### Definir Variables
Para definir variables se utiliza la estructura:

```
DEF tipo1 nombre1 := valor1
```

Donde `tipo` puede ser alguno de los tipos admitidos.

### Asignación de Valores
Para asignar valores a una variable se utiliza el símbolo `:=` seguido por una variable o un valor de alguno de los tipos admitidos.

### Funciones y Procedimientos
- Las funciones tienen la forma:

```
nombre(tipo1 arg1; tipo2 arg2; …; tipon argn) retorno.
```

- En el caso de los procedimientos:

```
nombre(tipo1 arg1; tipo2 arg2; …; tipon argn).
```

- El procedimiento que se utiliza para definir los pines es:

```
DEF PIN(tipo:número)
```

Donde `numero` indica el PIN que se va a utilizar y `tipo` puede ser:
- `PINOU`: salida
- `PININ`: entrada

### Comentarios
- Los comentarios de línea se inician con `/*`.
- Los comentarios de bloque se encierran entre `//*` y `*//`.

### Estructuras de Control
Este lenguaje admite las siguientes estructuras de control:

- **Condicional IF**:
  - `IF (condición) {}`
  - `IF (condición) {} ELSE {}`
- **Bucle WHILE**:
  - `WHILE (condición) {}`

### Palabras Reservadas y Funciones Predefinidas
Las palabras reservadas deben escribirse en **MAYÚSCULAS**. Además de las palabras mencionadas anteriormente, otras palabras reservadas son:

- **ADEL()**: El robot avanza.
- **ATR()**: El robot retrocede.
- **IZQ()**: El robot gira en sentido antihorario.
- **DER()**: El robot gira en sentido horario.
- **ESP(tiempo)**: El robot espera un tiempo determinado.
- **FREN()**: El robot se detiene.


## Ejemplo

## Pseudocódigo (lengFuente.txt)
```txt
EMPEZAR
extend("nombreDeLibreria.Extension;servo.h").
DEF entero MD1.
DEF entero MD2:=3./*INICIO DE LA SECCION SETUP
DEF PIN(PININ:MD1).
DEF PIN(PINOU:MD2).
/*FIN DE LA SECCION LOOP
ADEL().
ESP(10).
IZQ().
FREN().
TERMINAR
```

## Resultado (Salida.ino)
```cpp
#include <nombreDeLibreria.Extension>
#include <servo.h>

int MD1;
int MD2 = 3;

void setup() {
    pinMode(MD1, INPUT);
    pinMode(MD2, OUTPUT);
}

void loop() {
    avanzar();
    esperar(10);
    giro_izquierda();
    parar();
}
```


