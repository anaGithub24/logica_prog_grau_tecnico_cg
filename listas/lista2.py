
# Operadores e matemática

# 1. Antecessor e sucessor 
n= int(input("Digite um número: "))
print(f"Antecessor: {n-1}, Sucessor: {n+1}")

# 2.calculadora media  com (input)
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
print(f"Média: {media:.1f}")  # :.1f = uma casa decimal

#3.dobro,triplo e raiz
n = float(input("Número: "))
print(f"Dobro: {n*2}")
print(f"Triplo: {n*3}")
print(f"Raiz quadrada: {n**0.5:.2f}")

#4. divisao de conta  resto e inteiro 
#50 balas para 6 crianças

balas = 50
criancas = 6
cada = balas // criancas   # divisão inteira
sobra = balas % criancas    # resto
print(f"Cada criança recebe {cada} bala(s). Sobram {sobra}.")

# 5.conversor de moedas.formataçao
reais = float(input("Quantos R$ você tem? "))
dolar = 5.80
conversao = reais / dolar
print(f"Você pode comprar US$ {conversao:.2f}")
 
#6.Validaçao de acesso (operadores logicos)
idade = int(input("Idade: "))
convite = input("Tem convite? (True/False): ").lower() == "true"
acesso = (idade >= 18) and convite
print(acesso)   # True apenas se ambas verdadeiras