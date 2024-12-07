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
    '''LIBRERIASP : EXTEND LPAREN COMILLA LIBRERIASLIST COMILLA RPAREN PTO'''
    p[0] = p[4]
    traductor(p, trad_librerias)
    pass

def p_LIBRERIASLIST(p):
    '''LIBRERIASLIST : PALABRA PTO PALABRA
                     | PALABRA PTO PALABRA PTOCOMA LIBRERIASLIST'''
    if len(p) == 4:
        p[0] = [p[1]+p[2]+p[3]]
    elif len(p) > 4:
        p[0] = [p[1]+p[2]+p[3]] + p[5]
    else:
        p[0] = []
    pass

def p_CUERPO(p):
    '''CUERPO : INSTRUCCION CUERPO 
              | INSTRUCCION
              | EMPTY'''
    if len(p) == 3:
        if p[1] and p[2]:
            p[0] = [p[1]] + (p[2] if isinstance(p[2], list) else [p[2]])
        elif p[1]:
            p[0] = [p[1]]
        else:
            p[0] = p[2] if p[2] else []
    elif len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = []

def p_INSTRUCCION(p):
    '''INSTRUCCION : DEF_rule
                   | FUNC 
                   | ASSIGN_rule
                   | COMENTARIO
                   | IF_rule
                   | WHILE_rule
                   | PIN_rule
                   | MOV
                   | EMPTY '''
    p[0]=p[1]
    pass

def p_DEF_rule(p):
    '''DEF_rule : DEF TIPODATO PALABRA ASSIGN VALORVAR PTO
              | DEF TIPODATO PALABRA PTO'''
    if len(p) == 7:
        p[0] = [p[2], p[3], p[5]]
    elif len(p) == 5:
        p[0] = [p[2], p[3]]
    traductor(p, trad_def)
    pass

def p_TIPODATO(p):
    '''TIPODATO : ENTERO
                | TEXTO
                | DECIMAL
                | LOGICO
                '''
    p[0] = p[1]
    pass

def p_ASSIGN_rule(p):
    '''ASSIGN_rule : PALABRA ASSIGN VALORVAR PTO'''
    p[0] = f"{p[1]} = {p[3]};"
    pass

def p_VALORVAR(p):
    '''VALORVAR : PALABRA
                | TRUE
                | FALSE
                | INT
                | FLOAT
                '''
    if p.slice[1].type in ['INT', 'FLOAT']:
        p[0] = str(p[1])
    else:
        p[0] = p[1]
    pass

def p_FUNC(p):
    '''FUNC : PALABRA LPAREN PARAM_LIST RPAREN LBRACE CUERPO RETORNO PALABRA PTO RBRACE PTO
            | PALABRA LPAREN PARAM_LIST RPAREN LBRACE CUERPO RBRACE PTO'''
    traductor(p, trad_func)
    pass

def p_PARAM_LIST(p):
    '''PARAM_LIST : TIPODATO PALABRA
                 | TIPODATO PALABRA PTOCOMA PARAM_LIST'''
    if len(p) == 3:
        p[0] = [(p[1], p[2])]
    elif len(p) > 2:
        p[0] = [(p[1], p[2])] + p[4]
    pass

def p_COMENTARIO(p):
    '''COMENTARIO : COMBLOQUE
                 | COMLINEA'''
    pass

def p_IF_rule(p):
    '''IF_rule : IF LPAREN COMPARA RPAREN LBRACE CUERPO RBRACE ELSE LBRACE CUERPO RBRACE
                | IF LPAREN COMPARA RPAREN LBRACE CUERPO RBRACE'''
    traductor(p, trad_if)
    pass


def p_WHILE_rule(p):
    '''WHILE_rule : WHILE LPAREN COMPARA RPAREN LBRACE CUERPO RBRACE'''
    traductor(p, trad_while)
    pass

def p_COMPARA(p):
    '''COMPARA : VALORVAR COMPARACION VALORVAR
               | VALORVAR'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    pass

def p_PIN_rule(p):
    '''PIN_rule : DEF PIN LPAREN PININ DOSPTOS PALABRA RPAREN PTO
                | DEF PIN LPAREN PINOU DOSPTOS PALABRA RPAREN PTO'''
    global primer_pin
    primer_pin = True if not hasattr(p_PIN_rule, 'called') else False
    p_PIN_rule.called = True
    traductor(p, trad_pin, primer_pin=primer_pin, pin=True)
    pass

def p_MOV(p):
    '''MOV : ADEL LPAREN RPAREN PTO
           | ATR LPAREN RPAREN PTO
           | IZQ LPAREN RPAREN PTO
           | DER LPAREN RPAREN PTO
           | FREN LPAREN RPAREN PTO
           | ESP LPAREN INT RPAREN PTO
           | ESP LPAREN FLOAT RPAREN PTO'''
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
        print(f"Token actual: {p.value}")
        print(f"Esperado: {parser.tokens}")
    else:
        print("Error sintáctico: fin inesperado de entrada")
    raise Exception('syntax', 'error')

parser = yacc.yacc()
AL.lexer.lineno=0