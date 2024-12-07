from AS import parser

filename='lengFuente.txt'

f = open('salida.ino', 'r+')
f.truncate(0)

try:
    f = open(filename)
    data = f.read()
    f.close()
except IndexError:
    print('Error en archivo:\n')
    data = ''

try:
    resultado = parser.parse(data)
    print('¡Análisis sintáctico correcto! ✅')         
except Exception as e:
    print(f'Análisis sintáctico incorrecto ❎: {e}')