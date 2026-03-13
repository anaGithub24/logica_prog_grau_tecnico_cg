

#1 o maior e menor (lista basica)
valores = []
for i in range(5):
    valores.append(float(input(f"Valor {i+1}: ")))
print(f"Lista: {valores}")
print(f"Maior: {max(valores)}")
print(f"Menor: {min(valores)}")

# 2.Pares e Ímpares (listas separadas)
numeros = []
while True:
     n = int(input("Número: "))
     numeros.append(n)
     if input("Continuar? (S/N): ").upper() == 'N':
        break
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]
print(f"Todos: {numeros}\nPares: {pares}\nÍmpares: {impares}")#



# 3. funçao area 
def area (larg,comp):
    a = larg * comp
    print(f"A área é {a}m²")

print(area(10, 20))   # A área é 200m²

#4.fatorial modularizado


def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat 

num = int(input("Fatorial de: "))
print(f"{num}! = {fatorial(num)}")#fatorial de 5*4*3*1=120

# 5.validaçao de voto
from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    
    if idade <16 :
        return f"com {idade} anos: nao vota"
    elif 16 <= idade < 18 or idade > 65:
        return f"com {idade} anos: opcional"
    else: 
        return f"com {idade} anos: obrigatorio"

nasc = int(input("em que ano voce nasceu? "))
print(voto(nasc))

#6 Matriz 3x3

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Valor [{l},{c}]: "))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
print(f"Soma dos pares: {soma_pares}")

#7 Sistema de notas

def notas(*n):
    dados = {}
    dados['quantidade'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n)/len(n)
    if dados['media'] >= 7:
        dados['situacao'] = "Aprovado"
    else:
        dados['situacao'] = "Reprovado"
    return dados

resultado = notas(8.5, 7.0, 9.2, 5.5)
print(resultado)