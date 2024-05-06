# C-PTBR

## APS LÓGICA DA COMPUTAÇÃO

###Ideia:
A linguagem de programação desenvolvida foi pensada para ser uma ferramenta didática e fácil de aprender para novos programadores brasileiros, com palavras reservadas em português. Ela é pouco tipada, então você pode aprender lógica de programação sem se preocupar muito com a sintaxe.
O principal objetivo é conseguir trazer programação o mais cedo possivel para as crianças/adolecentes, com a linguagem criada é possivél criar funções para resolver problemas matematicos faceis e despertar o interesse em programação, como pode ser visto nos exemplos abaixo.
Além de apresentar possibilidade de uso de if/while para realizar condições lógicas.


```` py
// Função que calcula a área de um retângulo
funcao areaRetangulo(largura, altura) {
    retorna largura * altura;
}
l = 5;
h = 10;
resultado = areaRetangulo(l, h);
imprime(resultado);

// Função que verifica se um número é par
funcao ePar(n) {
    se (n / 2 * 2 == n) {
        resultado = 1;
    } senao {
        resultado = 0;
    }
    retorna resultado;
}

````


## EBNF
```` py

BLOCO          =  {COMANDO} ;
 
COMANDO        =  ( λ | ATRIBUICAO | IMPRESSAO | ENQUANTO | SE | FUNCAO | RETORNA | CHAMADA), ";", "\n" ;
 
ATRIBUICAO     =  IDENTIFICADOR,(["=",RELEXPR] |"=", RELEXPR );

IMPRESSAO      =  "imprime", "(" RELEXPR ")" ;
 
SE             =  "se", "(", RELEXPR, ")", "{", COMANDO, "}", ["senao", "{", COMANDO, "}"] ;
 
ENQUANTO       =  "enquanto", "(", RELEXPR, ")", "{", COMANDO,"}" ;
  
FUNCAO         =  "funcao", IDENTIFICADOR, "(", [PARAMETRO], ")", "{", "\n", {BLOCO}, "}" ;

PARAMETRO      =  IDENTIFICADOR, {",", IDENTIFICADOR} ;

CHAMADA        = IDENTIFICADOR, "(", [RELEXPR, {",", RELEXPR}] ,")";
 
RETORNA        =  "retorna", RELEXPR;

RELEXPR        =  EXPRESSAO, { ("<" | ">" | "==" ), EXPRESSAO } ;
 
EXPRESSAO      =  TERMO {("+" | "-", "ou") TERMO} ;
 
TERMO          =  FATOR {("*" | "/" | "e"), FATOR} ;
 
FATOR          = (NÚMERO | STRING | IDENTIFICADOR, ["(", [RELEXPR, {",", RELEXPR}] ,")"] | ("+" | "-" | "!"), FACTOR) | "(", RELEXPR, ")" ;
 
CHAMADAFUNCAO  =  IDENTIFICADOR "(" [EXPRESSAO {"," EXPRESSAO}] ")" ;
 
IDENTIFICADOR  =  LETRA, {LETRA | DIGITO | "_"} ;
 
NÚMERO         =  DIGITO, { DIGITO } ;
 
STRING         =  '"' {LETRA} '"' ;

LETRA          =  ( a | ... | z | A | ... | Z ) ;
 
DIGITO         =  ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

````
