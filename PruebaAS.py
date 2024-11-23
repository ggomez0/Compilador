from AS import parser

filename='lengFuente.txt'

f = open('salida.ino', 'r+')
f.truncate(0)

try:
    f = open(filename)
    data = f.read()
    f.close()
    print('Contenido del archivo:\n',data,'\n')
except IndexError:
    print('Error en archivo:\n')
    data = ''

try:
        resultado = parser.parse(data)
        print('¡Analisis sintáctico correcto! ✅')         
except:
        print('Analisis sintáctico incorrecto ❎')