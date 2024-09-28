# Exercício 1:

def fibonacci(n):

    # Verificação do valor n
    if n <= 0:
        return "O valor inserido deve ser maior que 0. "
    
    # Definição da sequência inicial
    sequencia = [0, 1]

    # Estrutura de repetição para calcular o proximo número
    for i in range(2, n):
        proxNum = sequencia[i-1] + sequencia[i-2]
        sequencia.append(proxNum)
    
    # Retorna a sequência com N números
    return sequencia[:n]

n = int(input("Exercício 1: Digite um número: "))
print(f"Exercício 1: A sequência fibonacci do número digitado é {fibonacci(n)}.")




# Exercício 2:

def verificacaoA(texto):
    
    # Deixa o texto com letras minusculas para facilitar a verificação:
    texto = texto.lower()

    # Conta quantas vezes a letra 'a' aparece
    quant = texto.count('a')

    # Verifica se aparece a letra 'a' e printa na tela
    if quant >= 1:
        return (f"Exercício 2: A letra 'a' aparece {quant} vezes na string digitada. ")
    else:
        return ("Exercício 2: A letra 'a' não aparece nenhuma vez na string. ")

texto = str(input("Exercício 2: Digite uma string: "))
print(verificacaoA(texto))




# Exercício 3:
def exercicio3():
    indice = 12
    soma = 0
    k = 1

    while k < indice:
        k = k + 1
        soma = soma + k
    return (f"Exercício 3: O valor de soma é igual à: {soma}")

print(exercicio3())




# Exercício 4:

# A:
listaA = [1, 3, 5, 7]
for proxNum in range(4, 7):     # Serão adicionados números apartir da quinta até a sétima posição da lista;
    proxNum = listaA[-1] + 2    # O próximo número será igual ao último elemento da lista + 2;
    listaA.append(proxNum)      # Só adiciona os números do loop à lista
print(f"Exercício 4 - A: Os elemetos da lista 'A' são: {listaA}")    # Printa a lista

#B:
listaB = [2, 4, 8, 16, 32, 64]
for proxNum in range(6, 10):
    proxNum = listaB[-1] * 2
    listaB.append(proxNum)
print(f"Exercício 4 - B: Os elementos da lista 'B' são: {listaB}")

#C:
listaC = [0, 1, 4, 9, 16, 25, 36]
for i in range(7, 11):     # Pega o número de posições que tem a lista (no caso 7)
    proxNum = i ** 2  # Eleva o número de posições ao quadrado (7 ** 2 = 49, que é o próximo elemento)
    listaC.append(proxNum)
print(f"Exercício 4 - C: Os elementos da lista 'C' são: {listaC}")

#D:
listaD = [4, 16, 36, 64]
for proxNum in range(4, 8):
    posicao = listaD[-1]    # Pega o ultimo número da ultima posição (no caso o 64)
    raizUltimoNumero = (posicao ** 0.5) + 2 # Realiza a raiz quadrada desse número e soma mais 2 (8 + 2 = 10)
    proxNum = raizUltimoNumero ** 2     # proxNum recebe essa variavel ao quadrado (10 * 10 = 100)
    proxNum = round(proxNum)    # Retira as casas decimais
    listaD.append(proxNum)
print(f"Exercício 4 - D: Os elementos da lista 'D' são: {listaD}")

#E: 
listaE = [1, 1, 2, 3, 5, 8]
for i in range(6, 10):
    proxNum = listaE[i-1] + listaE[i-2]
    listaE.append(proxNum)
print(f"Exercício 4 - E: Os elementos da lista 'E' são: {listaE}")

#F:
listaF = [2, 10, 12, 16, 17, 18, 19]    # A lógica que encontrei foi na escrita desses números, pois todos eles começam com a letra 'D', e os proximos 4 números que comçam com a letra 'd' são: Duzentos, Dois mil, Dez  mil e Doze mil
proxNum = [200, 2000, 10000, 12000]
listaF.extend(proxNum)
print(f"Exercício 5 - F: Os elementos da lista 'E' são: {listaF}")





