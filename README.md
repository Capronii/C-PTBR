# Hacker_Language

## APS LÓGICA DA COMPUTAÇÃO

###Ideia:
A ideia por tras dessa linguagem é usala para facilitar a criação de payloads e micro codigos para realizar testes em aplicações, a principal função futura é atrelar com bibliotecas que executam ataques para automatizar e facilitar mais do que as ferramentas ja fazem hoje em dia.

EBNF:

PROGRAM = "hack", "\n", BLOCK ;

BLOCK = { STATEMENT } ;

STATEMENT = ( HACK_DECLARATION | ASSIGNMENT | EXFILTRATE | LOOPHOLE_WHILE | IF ), "\n" ;

HACK_DECLARATION = "hack", IDENTIFIER, ["set", BYPASS_EXP] ;

ASSIGNMENT = IDENTIFIER, "set", BYPASS_EXP ;

BYPASS_EXP = EXP ;

EXP = TERM, { ("buff" | "debuff"), TERM } ;

TERM = FACTOR, { ("increase" | "decrease"), FACTOR } ;

FACTOR = INTEGER | IDENTIFIER | "(" , EXP , ")" | UNARY_OP, FACTOR ;

EXFILTRATE = "exfiltrate", "(", BYPASS_EXP, ")" ;

LOOPHOLE_WHILE = "loophole", BYPASS_EXP, "until", "\n", { STATEMENT }, "end" ;

IF = "breach", BYPASS_EXP, "if", "\n", { STATEMENT }, "end" ;

TYPE = "loot" | "intel" | "payload" | "flag" ;

LOGIC_OP = "and/or" | "XOR" | "invert" ;


INTEGER = DIGIT, { DIGIT } ;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

UNARY_OP = "invert" | "-" ;

DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

LETTER = "A" | "B" | "C" | "D" | "E" | "F" | "G"
    | "H" | "I" | "J" | "K" | "L" | "M" | "N"
    | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
    | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
    | "c" | "d" | "e" | "f" | "g" | "h" | "i"
    | "j" | "k" | "l" | "m" | "n" | "o" | "p"
    | "q" | "r" | "s" | "t" | "u" | "v" | "w"
    | "x" | "y" | "z" ;
