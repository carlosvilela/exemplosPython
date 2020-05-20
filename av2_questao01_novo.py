import nltk

from nltk import CFG

gramaticaBNF = CFG.fromstring("""
    Lista -> Elemento | Elemento Lista
    Elemento -> Letra Digito
    Letra -> "A" | "B" | "C"
    Digito -> "1" | "2" | "3" | "4"
""")

print(gramaticaBNF.start())  # imprime o inicio da gramatica

print(gramaticaBNF.productions())  # imprime as regras de producao

print(gramaticaBNF.productions()[0].lhs())  # imprime o lado esquerdo da primeira regra de producao

# Inserir entradas
inserirEntrada = "A2B1"
# Gerar Lista de entradas
entrada = list(inserirEntrada)
processarEntrada = nltk.ChartParser(gramaticaBNF)

# testa se há erro na Entrada
try:
    for saidaGramatica in processarEntrada.parse(entrada):
        print(saidaGramatica) # imprime a saida da gramática
except ValueError as e:
    print(e)
