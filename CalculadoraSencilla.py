"Cristian Gonzalez C.I: 24420446"
"Emmanuel Franquiz C.I: 25443711"
"Abdel Penagos C.I: 22522609"
import ply.lex as lex

tokens = (
    
    'STRING',
    'INTEGER',
    'FLOAT',
)

literals = ['=', '+', '-', '*', '/', '(', ')']




def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor incorrecto")
        t.value = 0
    return t

t_ignore = " \t"

def t_FLOAT(t):
    r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
    try:
        t.value = float(t.value)
    except ValueError:
        print("valor incorrecto")
        t.value = 0
    return t


def t_STRING(t):
    r'\'.*?\' | \"".*?\"'
    t.value = str(t.value)
    return t

def t_error(t):
    print (("Tipo de caracter no permitido '%s'" % t.value[0]))
    t.lexer.skip(1)

lex.lex()

#------------------------------------------------------------------------------

import ply.yacc as yacc

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
    )



def p_statement_expr(p):
    'statement : expression'
    print ('R = '), p[1]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_op(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+' : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_number(p):
    """expression : INTEGER
                | FLOAT"""
    p[0] = float(p[1])


def p_expression_string(p):
    "expression : STRING"
    p[0] = str(p[1])

def p_error(p):
    print (("Error de Sintaxis en '%s'" % p.value))

yacc.yacc()

print(""" Calculadora de datos sencillos """)

while 1:
    try:
        s = (raw_input("Calculadora -> "))
    except EOFError:
        break
    if not s: continue
    elif(s == "exit" or s == "salir"):
        print("Cerrar")
        break
    yacc.parse(s)
