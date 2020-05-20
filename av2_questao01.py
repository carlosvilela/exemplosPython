#+-----------------------------------------------------------------+
#|                                                   questao_01.py |
#|                          Copyright 2020, Carlos Bezerra Vilela. |
#|                  https://github.com/carlosvilela/exemplosPython |
#+-----------------------------------------------------------------+

import re

# Inserir entradas
inserirEntrada = "A1 A2B1"
# Gerar Lista de entradas
entrada = re.split("\s", inserirEntrada)
# Verifica a quantidade de entradas
numeroEntradas = len(entrada)

print("=======//=======//=======//=======")


while (numeroEntradas>0):
    lerPosicaoEntrada = len(entrada) - numeroEntradas
    pcaracter = 0
    scaracter = pcaracter + 1

    # Gerar Lista de elementos
    element = list(entrada[lerPosicaoEntrada])
    # Verifica quantidade de elementos
    numeroElemento = len(element)
    tamanhoElemento = len(element)

    # Analisar entradas
    #fatorEntrada = ""
    #if numeroEntradas>1:
    #    fatorEntrada = "<list>"
    print("Entrada: ", entrada[lerPosicaoEntrada])
    print("<list>::= <element> <list>")

    numeroEntradas = numeroEntradas - 1
    resultadoElementos = ""

    while (numeroElemento>0):

        lerPosicaoElemento = len(element) - numeroElemento
        numeroElemento = numeroElemento - 1
        # Analisar elementos
        fatorElemento = " "
        if numeroElemento >=1:
            fatorElemento = "<element>"
        # Construir Fator Geral
        #fatorGeral = fatorElemento + fatorEntrada
        fatorGeral = fatorElemento
        # Verificar Elemento

        # Verificar Tipo de Elemento
        tipoElemento = ""
        # Verifica se são pares de elementos
        if (tamanhoElemento%2 != 0):
            print("ERRO: Não satisfaz as regras")
            break

        # verifica o primeiro e o segundo elemento conforme regra de negocio
        primeiroCaracter = re.match(r"[A-C]",element[pcaracter])
        segundoCaracter = re.match(r"[1-4]",element[scaracter])
        # Regra de negócio
        letra = re.match(r"[A-C]",element[lerPosicaoElemento])
        numero = re.match(r"[1-4]", element[lerPosicaoElemento])

        # Organiza quem é o primeiro e o segundo elemento
        if (tamanhoElemento > (pcaracter+2)):
            pcaracter = scaracter + 1
            scaracter = pcaracter + 1

        if (not primeiroCaracter):
            print("ERRO: Não satisfaz as regras")
            break
        else:
            if (not segundoCaracter):
                print("ERRO: Não satisfaz as regras")
                break
            else:
                if(letra):
                    tipoElemento = "<letter>"
                else:
                    if(numero):
                        tipoElemento = "<digit>"
                    else:
                        print("ERRO: Não satisfaz as regras")
                        break
        print(resultadoElementos+tipoElemento+fatorGeral)
        resultadoElementos = resultadoElementos + element[lerPosicaoElemento]
        print(resultadoElementos+fatorGeral)
    print ("=======//=======//=======//=======")
