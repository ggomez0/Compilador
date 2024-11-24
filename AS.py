from ply import yacc
from AL import *
import AL
from Traductor import *

primer_pin=False
primer_mov=False


def p_INICIO(p):
    '''INICIO : EMPEZAR LIBRERIAS CUERPO TERMINAR'''
    pass

def p_LIBRERIAS(p):
    '''LIBRERIAS : LIBRERIASP
                 | EMPTY'''
    if len(p) > 1:
        p[0] = p[1]
    else:
        p[0] = None
    pass

def p_LIBRERIASP(p):
    '''LIBRERIASP : extend LPAREN LIBRERIASLIST RPAREN finLinea'''
    p[0] = {'type': 'libraries', 'libs': p[3]}
    traductor(p, trad_librerias)
    pass

def p_LIBRERIASLIST(p):
    '''LIBRERIASLIST : NOM_LIB
                     | NOM_LIB PTOCOMA LIBRERIASLIST'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
    pass

def p_CUERPO(p):
    '''CUERPO : INSTRUCCION CUERPO
              | EMPTY'''
    pass

def p_INSTRUCCION(p):
    '''INSTRUCCION : DEF_rule
                   | ASSIGN_rule
                   | FUNC
                   | COMENTARIO
                   | IF_rule
                   | ELSE_rule
                   | WHILE_rule
                   | PIN_rule
                   | MOV'''
    pass

def p_DEF_rule(p):
    '''DEF_rule : DEF TIPODATO nomVar ASSIGN VALORVAR finLinea
              | DEF TIPODATO nomVar finLinea'''
    traductor(p, trad_def)
    pass

def p_TIPODATO(p):
    '''TIPODATO : palResInt
                | palResString
                | palResFloat
                | palResBool'''
    pass

def p_ASSIGN_rule(p):
    '''ASSIGN_rule : nomVar ASSIGN VALORVAR finLinea'''
    traductor(p, trad_asign)
    pass

def p_VALORVAR(p):
    '''VALORVAR : string
                | true
                | false
                | int
                | float
                | nomVar'''
    pass

def p_FUNC(p):
    '''FUNC : nomVar LPAREN PARAM_LIST RPAREN RETORNO finLinea
           | nomVar LPAREN PARAM_LIST RPAREN finLinea'''
    traductor(p, trad_func)
    pass

def p_PARAM_LIST(p):
    '''PARAM_LIST : TIPODATO nomVar
                 | TIPODATO nomVar PTOCOMA PARAM_LIST
                 | EMPTY'''
    pass

def p_COMENTARIO(p):
    '''COMENTARIO : comBloque
                 | comLinea'''
    pass

def p_IF_rule(p):
    '''IF_rule : IF LPAREN COMPARACION RPAREN LBRACE CUERPO RBRACE finLinea'''
    traductor(p, trad_if)
    pass

def p_ELSE_rule(p):
    '''ELSE_rule : ELSE LPAREN COMPARACION RPAREN LBRACE CUERPO RBRACE finLinea'''
    pass

def p_WHILE_rule(p):
    '''WHILE_rule : WHILE LPAREN COMPARACION RPAREN LBRACE CUERPO RBRACE finLinea'''
    pass

def p_COMPARACION(p):
    '''COMPARACION : VALORVAR comp VALORVAR'''
    pass

def p_PIN_rule(p):
    '''PIN_rule : DEF PIN LPAREN PININ DOSPTOS int RPAREN finLinea
                | DEF PIN LPAREN PINOU DOSPTOS int RPAREN finLinea'''
    global primer_pin
    primer_pin = True if not hasattr(p_PIN_rule, 'called') else False
    p_PIN_rule.called = True
    traductor(p, trad_pin, primer_pin=primer_pin, pin=True)
    pass

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
    pass

def p_EMPTY(p):
    '''EMPTY : '''
    pass

def p_error(p):
    if p:
        print(f"Error sintáctico en la línea: {p.lineno}. No se esperaba el token: '{p.value}'")
        print(f"Esperado: {parser.tokens}")  # Show expected tokens
    else:
        print("Error sintáctico: fin inesperado de entrada")
    raise Exception('syntax', 'error')

parser = yacc.yacc()
AL.lexer.lineno=0