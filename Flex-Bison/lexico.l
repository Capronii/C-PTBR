%{
#include <stdio.h>
#include <string.h>
#include "parse.h"
%}

%option noyywrap

%%

[ \t\n]                 ;

\"[^"]*\"               return STRING;

"e"                     return AND;
"ou"                    return OR;
"imprime"               return IMPRIME;
"se"                    return SE;
"senao"                 return SENAO;
"enquanto"              return ENQUANTO;
"funcao"                return FUNCAO;
"retorna"               return RETORNA;

[a-zA-Z][a-zA-Z0-9_]*   return IDENTIFICADOR;
"[a-zA-Z][a-zA-Z0-9_]"  return STRING;
[0-9]+"."[0-9]+         return DOUBLE;
[0-9]+                  return INT;

"="                     return IGUAL;
"+"                     return MAIS;
"-"                     return MENOS;
"*"                     return VEZES;
"/"                     return DIVIDIDO;
"("                     return ABREPARENTESES;
")"                     return FECHAPARENTESES;
";"                     return PONTOEVIRGULA;
","                     return VIRGULA;
"{"                     return ABRECHAVES;
"}"                     return FECHACHAVES;
"=="                    return IGUALIGUAL;
"!="                    return DIFERENTE;
"<"                     return MENORQUE;
">"                     return MAIORQUE;
"//".*                  ;

.                       printf("Token desconhecido\n"); yyterminate();

%%

