#Traductor.py

# Función principal para traducir código a Arduino
def traductor(p,funcion,primer_pin=False,pin=False,primer_mov=False,mov=False):
  # Abrir el archivo de salida en modo lectura
  with open("salida.ino","r") as fileRead:
    # Leer el contenido del archivo
    file_content=fileRead.readlines()
  # Abrir el archivo de salida en modo escritura
  with open("salida.ino","w") as fileWrite:
    # Si se proporciona un parámetro p
    if (p):
      # Si se solicita la configuración de un pin
      if(pin):
        # Si es el primer pin, agregar la función setup
        if(primer_pin):
          file_content+=['void setup(){\n'] + ['\n'] +['}\n']
        # Insertar la configuración del pin en el contenido del archivo
        index = file_content.index('\n')
        file_content.insert(index, funcion(p))
        # Escribir el contenido modificado en el archivo
        fileWrite.write("".join(file_content))
        return
      # Si se solicita un movimiento
      if(mov):
        # Si es el primer movimiento, agregar la función loop
        if(primer_mov):
          file_content+=['void loop(){\n'] + ['\n'] +['}\n']
        # Insertar el movimiento en el contenido del archivo
        index = file_content.index('\n',file_content.index('\n')+1)
        file_content.insert(index, funcion(p))
        # Escribir el contenido modificado en el archivo
        fileWrite.write("".join(file_content))
        return
      # Si no se solicita pin ni movimiento, simplemente agregar el contenido
      file_content.append(funcion(p))
      # Escribir el contenido modificado en el archivo
      fileWrite.write("".join(file_content))

# Función para traducir la inclusión de librerías
def trad_librerias(p):
    # Convertir el parámetro a una lista para acceder a sus caracteres
    list_p = list(p)
    # Retorna la inclusión de la librería formateada
    return "".join(["#include <"]+list_p[3:4]+[">"]+["\n"])

# Función para traducir la declaración de variables
def trad_def(p):
    # Convertir el parámetro a una lista para acceder a sus caracteres
    list_p = list(p)
    # Determinar el tipo de variable y retornar la declaración formateada
    if list_p[2] == 'entero':
      return 'int  'f'{list_p[4]};'+"\n"
    elif list_p[2] == 'texto':
      return 'string  'f'{list_p[4]};'+"\n"
    elif list_p[2] == 'logico':
      return 'bool  'f'{list_p[4]};'+"\n"
    elif list_p[2] == 'decimal':
      return 'float  'f'{list_p[4]};'+"\n"

# Función para traducir la asignación de valores a variables
def trad_asign(p):
    # Convertir el parámetro a una lista para acceder a sus caracteres
    list_p = list(p)
    # Retorna la asignación formateada
    return f'{list_p[1]}:{list_p[2]}{list_p[3]};'+"\n"

# Función para traducir la configuración de pines
def trad_pin(p):
    # Convertir el parámetro a una lista para acceder a sus caracteres
    list_p = list(p)
    print ('###72', list_p)
    # Determinar el tipo de configuración del pin y retornar la configuración formateada
    if list_p[3] == 'SAL':
      return f'pinMode({list_p[5]}, OUTPUT);'+"\n"
    elif list_p[3] == 'ENT':
      return f'pinMode({list_p[5]}, INPUT);'+"\n"

# Función para traducir los movimientos del robot
def trad_mov(p):
    # Convertir el parámetro a una lista para acceder a sus caracteres
    list_p = list(p)
    # Determinar el tipo de movimiento y retornar el movimiento formateado
    if list_p[1] == 'ADEL':
      return 'avanzar();'+"\n"
    elif list_p[1] == 'ATRAS':
      return 'retroceder();'+"\n"
    elif list_p[1] == 'IZQUIERDA':
      return 'giro_izquierda();'+"\n"
    elif list_p[1] == 'DER':
      return 'giro_derecha();'+"\n"
    elif list_p[1] == 'STOP':
      return 'parar();'+"\n"
    elif list_p[1] == 'ESP':
      return f'esperar({list_p[3]});'+"\n"

# Función para traducir la definición de funciones
def trad_func(p):
    # Convertir el parámetro a una lista para acceder a sus caracteres
    list_p = list(p)
    # Retorna la definición de la función formateada
    result = "".join([list_p[2]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
    if(list_p[6]==":"):
      if(list_p[4]==None and list_p[9]==None):
        result = "".join([list_p[7]]+[list_p[2]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
    return result

# Función para traducir estructuras de control if
def trad_if(p):
    # Retorna la estructura if formateada
    result = "".join(["if ("]+[") "] + ["{"]+["\n"]+["}"]+["\n"])
    return result