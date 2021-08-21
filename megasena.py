# Este programa gera uma serie de numeros da mega sena com no maximo tres numeros em comum entre todos
# TODO: Traduzir para ingles e separar em funcoes

from random import randint

todasAsSenas = []
quant = int(input('Quantos jogos você quer sortear? '))

while len(todasAsSenas) < quant:
    sena = []
    while len(sena) < 6:
        num = randint(1, 60)
        if num not in sena:
            sena.append(num)
    sena.sort()
    if len(todasAsSenas) == 0:
        todasAsSenas.append(sena)
    else:
        for cada_sena in todasAsSenas:
            repetidos = 0
            for index, value in enumerate(cada_sena):
                if sena[index] == value:
                    repetidos += 1
        if repetidos <= 3:
            todasAsSenas.append(sena)

todasAsSenas.sort()
print(*todasAsSenas, sep='\n')