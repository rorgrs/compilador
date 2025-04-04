class Token(enumerate):
    EOF = 0
    WHILE = 1
    VAR = 2
    TO = 3
    THEN = 4
    STRING = 5
    REAL = 6
    READ = 7
    PROGRAM = 8
    PROCEDURE = 9
    PRINT = 10
    NREAL = 11
    NINT = 12
    LITERAL = 13
    INTEGER = 14
    IF = 15
    IDENT = 16
    FOR = 17
    END = 18
    ELSE = 19
    DO = 20
    CONST = 21
    BEGIN = 22
    VSTRING = 23
    GTE = 24
    GT = 25
    EQ = 26
    DIFF = 27
    LTE = 28
    LT = 29
    MAIS = 30
    PVIRG = 31
    ATTRIB = 32
    DPONTO = 33
    FSLASH = 34
    PONTO = 35
    VIRG = 36
    ASTK = 37
    APARNT = 38
    FPARNT = 39
    ACHAVE = 40
    FCHAVE = 41
    MENOS = 42


RESERVADAS = {
    'while': Token.WHILE,
    'var': Token.VAR,
    'to': Token.TO,
    'then': Token.THEN,
    'string': Token.STRING,
    'real': Token.REAL,
    'read': Token.READ,
    'program': Token.PROGRAM,
    'procedure': Token.PROCEDURE,
    'print': Token.PRINT,
    'nreal': Token.NREAL,
    'nint': Token.NINT,
    'literal': Token.LITERAL,
    'integer': Token.INTEGER,
    'if': Token.IF,
    'for': Token.FOR,
    'end': Token.END,
    'else': Token.ELSE,
    'do': Token.DO,
    'const': Token.CONST,
    'begin': Token.BEGIN,
    'vstring': Token.VSTRING
}

SIMBOLOS = {
    '>=': Token.GTE,
    '<>': Token.DIFF,
    '<=': Token.LTE,
    ':=': Token.ATTRIB,
    '=': Token.EQ,
    '<': Token.LT,
    '>': Token.GT,
    '+': Token.MAIS,
    ';': Token.PVIRG,
    ':': Token.DPONTO,
    '/': Token.FSLASH,
    '.': Token.PONTO,
    ',': Token.VIRG,
    '*': Token.ASTK,
    ')': Token.FPARNT,
    '(': Token.APARNT,
    '{': Token.ACHAVE,
    '}': Token.FCHAVE,
    '-': Token.MENOS,
}
