import ply.lex as lex

reserved = {
    'EMPEZAR': 'EMPEZAR',
    'TERMINAR': 'TERMINAR',
    'extend': 'extend',
    'DEF': 'DEF',
    'ADEL': 'ADEL',
    'ATR': 'ATR',
    'IZQ': 'IZQ',
    'DER': 'DER',
    'ESP': 'ESP',
    'FREN': 'FREN',
    'IF': 'IF',
    'ELSE': 'ELSE',
    'WHILE': 'WHILE',
    'PIN': 'PIN',
    'PININ': 'PININ',
    'PINOU': 'PINOU',
    'entero': 'palResInt',
    'texto': 'palResString',
    'decimal': 'palResFloat',
    'logico': 'palResBool',
    'RETORNO': 'RETORNO',
    'true': 'true',
    'false': 'false'
}

tokens = [
    'int',           # Changed from NUMBER
    'float',         # Changed from FLOAT_NUMBER
    'string',        # Added for string literals
    'NOM_LIB',
    'nomVar',
    'comp',
    'ASSIGN',
    'finLinea',
    'PTOCOMA',
    'LPAREN',   
    'RPAREN', 
    'LBRACE',  
    'RBRACE',  
    'DOSPTOS',    
    'comBloque',
    'comLinea'
] + list(reserved.values())

# Token rules
t_ASSIGN = r':='
t_finLinea = r'\.'
t_PTOCOMA = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOSPTOS = r':'
t_comBloque = r'//\*(.|\n)*\*//'
t_comLinea = r'/.*'
t_comp = r'(>|<|==|!=|<=|>=)'

def t_string(t):
    r'"[A-Za-z0-9_-]+"'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_float(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_int(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NOM_LIB(t):
    r'"[^"]*"'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_nomVar(t):
    r'[A-Za-z][A-Za-z0-9_-]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()