import nltk
from nltk import CFG

gramaticaBNF = CFG.fromstring("""
    Lista -> Elemento | Elemento Lista
    Elemento -> Letra Digito
    Letra -> "A" | "B"
    Digito -> "1" | "2"
""")

print(gramaticaBNF.start())  # imprime o inicio da gramatica

print(gramaticaBNF.productions())  # imprime as regras de producao

print(gramaticaBNF.productions()[0].lhs())  # imprime o lado esquerdo da primeira regra de producao

entrada = "A 1 B 2".split()
processarEntrada = nltk.ChartParser(gramaticaBNF)

# testa se há erro na Entrada
try:
    for saidaGramatica in processarEntrada.parse(entrada):
        print(saidaGramatica) # imprime a saida da gramática
except ValueError as e:
    print(e)
