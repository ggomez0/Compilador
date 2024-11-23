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
  pass

def p_LIBRERIASP(p):
  '''LIBRERIASP : extend LPAREN NOM_LIB RPAREN PTOCOMA LIBRERIAS
                | extend LPAREN NOM_LIB RPAREN finLinea'''
  traductor(p,trad_librerias)
  pass

def p_CUERPO(p):
  '''CUERPO : DEF_rule CUERPO
        | ASSIGN_rule CUERPO
        | FUNC CUERPO
        | COMENTARIO CUERPO
        | IF_rule CUERPO
        | ELSE_rule CUERPO
        | WHILE_rule CUERPO
        | PIN_rule CUERPO
        | MOV CUERPO
        | EMPTY'''
  pass

def p_DEF_rule(p):
  '''DEF_rule : DEF TIPODATO nomVar ASSIGN VALORVAR finLinea'''
  traductor(p,trad_def)
  pass

def p_TIPODATO(p):
  '''TIPODATO : palResInt
        | palResString
        | palResFloat
        | palResBool'''
  pass

def p_ASSIGN_rule(p):
  '''ASSIGN_rule : nomVar ASSIGN string finLinea
        | nomVar ASSIGN int finLinea
        | nomVar ASSIGN float finLinea
        | nomVar ASSIGN true finLinea
        | nomVar ASSIGN false finLinea
        | nomVar ASSIGN nomVar finLinea'''
  traductor(p,trad_asign)
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
  traductor(p,trad_if)
  pass

def p_ELSE_rule(p):
  '''ELSE_rule : ELSE LPAREN COMPARACION RPAREN LBRACE CUERPO RBRACE finLinea'''
  pass

def p_WHILE_rule(p):
  '''WHILE_rule : WHILE LPAREN COMPARACION RPAREN LBRACE CUERPO RBRACE finLinea'''
  pass

def p_COMPARACION(p):
  '''COMPARACION : VALORVAR comp VALORVAR
        | nomVar comp VALORVAR
        | nomVar comp nomVar
        | false
        | true
        | nomVar'''
  pass

def p_VALORVAR(p):
  '''VALORVAR : string
        | true
        | false
        | int
        | float'''
  pass


def p_PIN_rule(p):
  '''PIN_rule : DEF PIN LPAREN PININ DOSPTOS INT RPAREN finLinea
        | DEF PIN LPAREN PINOU DOSPTOS INT RPAREN finLinea'''
  pass
        
  primer_pin = True if p_PIN_rule.counter <= 0 else False
  p_PIN_rule.counter += 1
  traductor(p, trad_pin, primer_pin=primer_pin, pin=True)
  pass

p_PIN_rule.counter = 0


def p_MOV(p):
  '''MOV : ADEL LPAREN RPAREN finLinea
        | ATR LPAREN RPAREN finLinea
        | IZQ LPAREN RPAREN finLinea
        | DER LPAREN RPAREN finLinea
        | FREN LPAREN RPAREN finLinea
        | ESP LPAREN int RPAREN finLinea
        | ESP LPAREN float RPAREN finLinea'''
  primer_mov = True if p_MOV.counter <= 0 else False
  p_MOV.counter += 1
  traductor(p,trad_mov,primer_mov=primer_mov, mov=True)
  pass

p_MOV.counter=0

def p_EMPTY(p):
  '''EMPTY : '''
  pass

def p_error(p):
  print("Error sintáctico en la línea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))        
  raise Exception('syntax', 'error') 
    
parser = yacc.yacc()
AL.lexer.lineno=0