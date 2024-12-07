import ply.lex as lex

tokens = [
    'EMPEZAR','TERMINAR',
    'EXTEND','DEF',
    'ADEL', 'ATR','IZQ','DER','ESP', 'FREN',
    'IF', 'ELSE',
    'WHILE',
    'PIN', 'PININ', 'PINOU',
    'ENTERO', 'TEXTO', 'DECIMAL', 'LOGICO',
    'RETORNO',
    'TRUE', 'FALSE',
    'PALABRA',
    'INT', 'FLOAT',
    'COMILLA',
    'COMPARACION',
    'ASSIGN', 'DOSPTOS', 'PTO', 'PTOCOMA',
    'LPAREN','RPAREN', 
    'LBRACE','RBRACE',  
    'COMBLOQUE','COMLINEA'
]

t_ASSIGN = r':='
t_PTO = r'\.'
t_PTOCOMA = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOSPTOS = r':'
t_COMPARACION  = r'(>|<|==|!=|<=|>=)'
t_COMBLOQUE = r'//\*(.|\n)*\*//'
t_COMLINEA = r'/.*'
t_ignore = ' \t'
t_COMILLA = r'\'|\"'
t_PALABRA = r'[a-zA-Z][a-zA-Z0-9_]*'

def t_EMPEZAR(t):
    r'\bEMPEZAR\b'
    return t

def t_TERMINAR(t):
    r'\bTERMINAR\b'
    return t

def t_RETORNO(t):
    r'\bretorno\b'
    return t

def t_EXTEND(t):
    r'\bextend\b'
    return t

def t_DEF(t):
    r'\bDEF\b'
    return t

def t_ADEL(t):
    r'\bADEL\b'
    return t

def t_ATR(t):
    r'\bATR\b'
    return t

def t_IZQ(t):
    r'\bIZQ\b'
    return t

def t_DER(t):
    r'\bDER\b'
    return t

def t_ESP(t):
    r'\bESP\b'
    return t

def t_FREN(t):
    r'\bFREN\b'
    return t

def t_IF(t):
    r'\bIF\b'
    return t

def t_ELSE(t):
    r'\bELSE\b'
    return t

def t_WHILE(t):
    r'\bWHILE\b'
    return t

def t_PIN(t):
    r'\bPIN\b'
    return t

def t_PININ(t):
    r'\bPININ\b'
    return t

def t_PINOU(t):
    r'\bPINOU\b'
    return t

def t_ENTERO(t):
    r'\bentero\b'
    return t

def t_TEXTO(t):
    r'\btexto\b'
    return t

def t_DECIMAL(t):
    r'\bdecimal\b'
    return t

def t_LOGICO(t):
    r'\blogico\b'
    return t

def t_FALSE(t):
    r'\bFALSE\b'
    return t

def t_TRUE(t):
    r'\bTRUE\b'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"No se reconoce el caracter '{t.value[0]}' en la linea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
