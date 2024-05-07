%{
#include <stdio.h>
int yylex();
void yyerror(const char *s) { printf("ERRO: %s\n", s); }
%}

%token IDENTIFICADOR INT DOUBLE STRING
%token IGUAL MAIS MENOS VEZES DIVIDIDO
%token ABREPARENTESES FECHAPARENTESES PONTOEVIRGULA VIRGULA ABRECHAVES FECHACHAVES
%token IGUALIGUAL DIFERENTE MENORQUE MAIORQUE AND OR
%token IMPRIME SE SENAO ENQUANTO FUNCAO RETORNA

%start programa

%%

programa : comandos
         ;

comandos : comando
         | comandos comando
         ;

comando : atribuicao
        | declaracao_impressao
        | declaracao_se
        | declaracao_enquanto
        | declaracao_funcao
        | declaracao_retorna
        ;

atribuicao : IDENTIFICADOR IGUAL expressao PONTOEVIRGULA
           ;

declaracao_impressao : IMPRIME ABREPARENTESES expressao FECHAPARENTESES PONTOEVIRGULA
                     ;

declaracao_se : SE ABREPARENTESES condicao FECHAPARENTESES ABRECHAVES comandos FECHACHAVES
              | SE ABREPARENTESES condicao FECHAPARENTESES ABRECHAVES comandos FECHACHAVES SENAO ABRECHAVES comandos FECHACHAVES
              ;

declaracao_enquanto : ENQUANTO ABREPARENTESES condicao FECHAPARENTESES ABRECHAVES comandos FECHACHAVES
                    ;

lista_parametros : IDENTIFICADOR
                 | lista_parametros VIRGULA IDENTIFICADOR
                 | /* vazio */
                 ;

expressao : expressao MAIS termo
          | expressao MENOS termo
          | termo
          ;

termo : termo VEZES fator
      | termo DIVIDIDO fator
      | fator
      ;

fator : INT
      | DOUBLE
      | STRING
      | IDENTIFICADOR
      | ABREPARENTESES expressao FECHAPARENTESES
      | chamada_funcao
      ;

declaracao_funcao : FUNCAO IDENTIFICADOR ABREPARENTESES lista_parametros FECHAPARENTESES ABRECHAVES comandos FECHACHAVES
                  ;

declaracao_retorna : RETORNA expressao PONTOEVIRGULA
                   | RETORNA PONTOEVIRGULA
                   ;

chamada_funcao : IDENTIFICADOR ABREPARENTESES lista_expressoes FECHAPARENTESES
                ;

lista_expressoes : expressao
                 | lista_expressoes VIRGULA expressao
                 | /* vazio */
                 ;

condicao : condicao_logica
         | condicao AND condicao_logica
         | condicao OR condicao_logica
         ;

condicao_logica : expressao IGUALIGUAL expressao
                | expressao DIFERENTE expressao
                | expressao MENORQUE expressao
                | expressao MAIORQUE expressao
                ;

%%

int main(){
     int result= yyparse();
     printf("yyparse() returned", result);
}