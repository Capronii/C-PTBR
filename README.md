# C-PTBR

## APS LÓGICA DA COMPUTAÇÃO

### Ideia:
A linguagem de programação desenvolvida foi pensada como uma ferramenta didática e fácil de aprender para novos programadores brasileiros, com palavras reservadas em português. Ela é fracamente tipada, permitindo que você aprenda lógica de programação sem se preocupar muito com a sintaxe.

O principal objetivo é trazer a programação o mais cedo possível para crianças e adolescentes. Com a linguagem criada, é possível desenvolver funções para resolver problemas matemáticos simples e despertar o interesse em programação, como demonstrado nos exemplos abaixo.

Além disso, a linguagem oferece suporte para uso de estruturas condicionais (if) para realizar operações lógicas.




## EBNF
```` py

BLOCO          =  {COMANDO} ;

COMANDO        =  (λ | ATRIBUICAO | IMPRESSAO | SE), ";", "\n" ;

ATRIBUICAO     =  IDENTIFICADOR, "=", RELEXPR ;

IMPRESSAO      =  "imprime", "(", RELEXPR, ")" ;

SE             =  "se", "(", RELEXPR, ")", "{", BLOCO, "}", ["senao", "{", BLOCO, "}"] ;

RELEXPR        =  EXPRESSAO, { ("<" | ">" | "=="), EXPRESSAO } ;

EXPRESSAO      =  TERMO, { ("+" | "-" | "ou"), TERMO } ;

TERMO          =  FATOR, { ("*" | "/" | "e"), FATOR } ;

FATOR          =  (NÚMERO | STRING | IDENTIFICADOR | ("+" | "-" | "!"), FATOR | "(", RELEXPR, ")" ) ;

IDENTIFICADOR  =  LETRA, {LETRA | DIGITO | "_"} ;

NÚMERO         =  DIGITO, {DIGITO} ;

STRING         =  '"', {LETRA}, '"' ;

LETRA          =  ( a | ... | z | A | ... | Z ) ;
 
DIGITO         =  ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

````
