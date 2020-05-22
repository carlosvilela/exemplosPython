#+-----------------------------------------------------------------+
#|                                                av2_questao04.py |
#|                          Copyright 2020, Carlos Bezerra Vilela. |
#|                  https://github.com/carlosvilela/exemplosPython |
#+-----------------------------------------------------------------+

import nltk

from nltk import CFG

gramaticaBNF = CFG.fromstring("""
    Expressao -> Expressao "+" Expressao | Termo
    Termo -> Termo "*" Termo | Fator
    Fator -> "(" Expressao ")" | Digito
    Digito -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
""")

print(gramaticaBNF.start())  # imprime o inicio da gramatica

print(gramaticaBNF.productions())  # imprime as regras de producao

print(gramaticaBNF.productions()[0].lhs())  # imprime o lado esquerdo da primeira regra de producao

# Inserir entradas
inserirEntrada = "1+3*5"
# Gerar Lista de entradas
entrada = list(inserirEntrada)
processarEntrada = nltk.ChartParser(gramaticaBNF)

# testa se há erro na Entrada
try:
    for saidaGramatica in processarEntrada.parse(entrada):
        print(saidaGramatica) # imprime a saida da gramática
except ValueError as e:
    print(e)
