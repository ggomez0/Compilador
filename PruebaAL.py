from AL import lexer

filename='ejAL_exito.txt'

try:
    f = open(filename)
    data = f.read()
    f.close()
    print('Contenido del archivo:\n',data,'\n')
except IndexError:
    print('Error en archivo:\n')
    data = ''

lexer.input(data)

print('Token - Lexema')
while True:
    tok = lexer.token()
    if not tok: break
    print('(',tok.type, ',',tok.value,')')