def traductor(p, funcion, primer_pin=False, pin=False, primer_mov=False, mov=False):
    with open("salida.ino", "r") as fileRead:
        file_content = fileRead.readlines()
    with open("salida.ino", "w") as fileWrite:
        if p:
            if pin:
                if primer_pin:
                    if "void setup()" not in "".join(file_content):
                        file_content += ['void setup(){\n'] + ['\n'] + ['}\n']
                index = file_content.index('\n')
                file_content.insert(index, funcion(p))
                fileWrite.write("".join(file_content))
                return
            
            if mov:
                if primer_mov:
                    if "void loop()" not in "".join(file_content):
                        file_content += ['void loop(){\n'] + ['\n'] + ['}\n']
                index = file_content.index('\n', file_content.index('\n') + 1)
                file_content.insert(index, funcion(p))
                fileWrite.write("".join(file_content))
                return
            
            file_content.append(funcion(p))
            fileWrite.write("".join(file_content))

def trad_librerias(p):
    librerias = ""
    for lib in p[4]:
        librerias += f"#include <{lib}>\n"
    return librerias

def trad_def(p):
    tipo = p[2]
    nombre = p[3]
    valor = p[5] if len(p) > 5 else None
    tipo_map = {'entero': 'int', 'texto': 'string', 'decimal': 'float', 'logico': 'bool'}
    tipo_traducido = tipo_map.get(tipo, tipo)
    if valor:
        return f"{tipo_traducido} {nombre};\n{nombre} = {valor};\n"
    else:
        return f"{tipo_traducido} {nombre};\n"

def trad_pin(p):
    if p[4] == "PINOU":
        return f"pinMode({p[6]}, OUTPUT);\n"
    elif p[4] == "PININ":
        return f"pinMode({p[6]}, INPUT);\n"

def trad_assign(p):
    return f"{p[1]} = {p[3]};\n"

def trad_mov(p):
    movimientos = {
        "ADEL": "avanzar();",
        "ATR": "retroceder();",
        "IZQ": "giro_izquierda();",
        "DER": "giro_derecha();",
        "ESP": f"esperar({p[3]});",
        "FREN": "parar();"
    }
    return movimientos.get(p[1], "") + "\n"

def trad_func(p):
    nombre = p[1]
    parametros = p[3] if p[3] else []
    params = ", ".join([f"{t} {n}" for t, n in parametros])
    
    cuerpo = ""
    if isinstance(p[6], list):
        for instruccion in p[6]:
            if instruccion:
                cuerpo += f"    {instruccion}\n"
    else:
        cuerpo = f"    {p[6]}\n" if p[6] else ""

    if (len(p) == 12):
        return f"{nombre}({params}) {{\n{cuerpo}return {p[8]};\n}}\n"
    elif (len(p) == 9):
        return f"void {nombre}({params}) {{\n{cuerpo}}}\n"
    
def trad_if(p):
    cuerpoif = ""
    if isinstance(p[6], list):
        for instruccion in p[6]:
            if instruccion:
                cuerpoif += f"    {instruccion}\n"
    else:
        cuerpoif = f"    {p[6]}\n" if p[6] else ""

    cuerpoelse = ""
    if len(p) > 10 and p[10]:
        if isinstance(p[10], list):
            for instruccion in p[10]:
                if instruccion:
                    cuerpoelse += f"    {instruccion}\n"
        else:
            cuerpoelse = f"    {p[10]}\n"

    if len(p) == 8:
        return f"if ({p[3]}) {{\n{cuerpoif}}}\n"
    elif len(p) > 8:
        return f"if ({p[3]}) {{\n{cuerpoif}}} else {{\n{cuerpoelse}}}\n"
    
def trad_while(p):
    cuerpo = ""
    if isinstance(p[6], list):
        for instruccion in p[6]:
            if instruccion:
                cuerpo += f"    {instruccion}\n"
    else:
        cuerpo = f"    {p[6]}\n" if p[6] else ""

    return f"while ({p[3]}) {{\n{cuerpo}}}\n"