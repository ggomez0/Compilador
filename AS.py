from ply import yacc
from AL import *
import AL
from Traductor import *

primer_pin = False
primer_mov = False

def p_INICIO(p):
    '''INICIO : EMPEZAR LIBRERIAS CUERPO TERMINAR'''
    pass

def p_LIBRERIAS(p):
    '''LIBRERIAS : LIBRERIASP
                | empty'''
    if len(p) > 1:
        p[0] = p[1]
    else:
        p[0] = None

def p_LIBRERIASP(p):
    '''LIBRERIASP : extend LPAREN NOM_LIB RPAREN finLinea'''
    p[0] = {'type': 'libraries', 'libs': p[3]}
    traductor(p, trad_librerias)

def p_CUERPO(p):
    '''CUERPO : INSTRUCCION CUERPO
              | empty'''
    pass

def p_INSTRUCCION(p):
    '''INSTRUCCION : DEF_rule
                  | PIN_rule
                  | MOV
                  | COMENTARIO'''
    pass

def p_DEF_rule(p):
    '''DEF_rule : DEF TIPODATO nomVar finLinea
               | DEF TIPODATO nomVar ASSIGN VALORVAR finLinea'''
    traductor(p, trad_def)
    pass

def p_TIPODATO(p):
    '''TIPODATO : palResInt
               | palResString
               | palResFloat
               | palResBool'''
    p[0] = p[1]

def p_PIN_rule(p):
    '''PIN_rule : DEF PIN LPAREN PINOU DOSPTOS nomVar RPAREN finLinea
               | DEF PIN LPAREN PININ DOSPTOS nomVar RPAREN finLinea'''
    global primer_pin
    primer_pin = True if not hasattr(p_PIN_rule, 'called') else False
    p_PIN_rule.called = True
    traductor(p, trad_pin, primer_pin=primer_pin, pin=True)

def p_MOV(p):
    '''MOV : ADEL LPAREN RPAREN finLinea
           | ATR LPAREN RPAREN finLinea
           | IZQ LPAREN RPAREN finLinea
           | DER LPAREN RPAREN finLinea
           | FREN LPAREN RPAREN finLinea
           | ESP LPAREN int RPAREN finLinea
           | ESP LPAREN float RPAREN finLinea'''
    global primer_mov
    primer_mov = True if not hasattr(p_MOV, 'called') else False
    p_MOV.called = True
    traductor(p, trad_mov, primer_mov=primer_mov, mov=True)

def p_COMENTARIO(p):
    '''COMENTARIO : comBloque
                 | comLinea'''
    pass

def p_VALORVAR(p):
    '''VALORVAR : string
               | true
               | false
               | int
               | float
               | nomVar'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print(f"Error sintáctico en la línea {p.lineno}. Token inesperado: '{p.value}'")
    else:
        print("Error sintáctico: fin inesperado de entrada")

# Construir el parser
parser = yacc.yacc()
AL.lexer.lineno=0