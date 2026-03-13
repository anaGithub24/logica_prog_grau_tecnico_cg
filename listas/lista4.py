 
#1. Contagem de Pares (for + if) 
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
        
#2. Soma dos Pares (Acumulador)
soma = 0
for _ in range(6):
    n = int(input("Número: "))
    if n % 2 == 0:
        soma = soma + n
print(f"Soma dos pares: {soma}")

#3. Jogo da Adivinhação (while + if/elif) 

from random import randint

pc = randint(0, 10)
tent = 0
nao_acertou_numero = True
while nao_acertou_numero:
    chute = int(input("Adivinhe (0-10): "))
    tent += 1
    if chute == pc:
        print(f"Acertou em {tent} tentativas!")
        nao_acertou_numero = False
    elif chute < pc:
        print("Mais alto...")
    else:
        print("Mais baixo...")

# 4. Flag de parada (999)

soma = 0
cont = 0
while True: # loop infinito
    n = int(input("Número (999 para): "))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f"Digitados {cont} números, soma = {soma}")

#5. Tabuada Personalizada (Loop Infinito + Break)

while True: # loop infinito
    n = int(input("Tabuada do : "))
    if n < 0: # se numero for negativo
        break
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        
#6. Detector de Palíndromos (Manipulação de String) 

frase = input("Frase: ").replace(" ", "").upper()
inverso = frase[::-1]
if frase == inverso:
    print("É palíndromo!")
else:
    print("Não é palíndromo.")
    
#7. Análise de Grupo
mais_18 = 0
homens = 0
mulheres_menos_20 = 0
while True: #LOOP INFINITO
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    if idade > 18:
        mais_18 = mais_18 + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 = mulheres_menos_20 + 1
    resp = input("Continuar? (S/N): ").upper()
    if resp == 'N':
        break
print(f">18: {mais_18}, Homens: {homens}, Mulheres <20: {mulheres_menos_20}")

