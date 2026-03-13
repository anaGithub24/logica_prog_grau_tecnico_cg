
# lista 3. Estruturas condicionais

# 1.radar de velocidade

vel = float(input("Velocidade (km/h): "))
if vel > 80:
    print("Multado! Limite 80km/h")
else:
    print("Boa viagem")

# 2.lista par e impar

num = int(input("Número: "))
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# 3.maior de dois numeros .

a = float(input("1º: "))
b = float(input("2º: "))
if a > b:
    print("Primeiro é maior")
elif b > a:
    print("Segundo é maior")
else:
    print("Iguais")

# 4. preço por distancia
dist = float(input("Distância em km: "))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print(f"Preço do bilhete: r$ {preco:.2f}")

# 5. classificaçao de idade.
ano = int(input("Ano de nascimento: "))
idade = 2025 - ano  
if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 64:
    print("Adulto")
else:
    print("Sénior")


# 6.simulador de emprestimo

valor_casa = float(input("Valor da casa: "))
salario = float(input("Salário: "))
anos = int(input("Anos pagamento: "))
meses = anos * 12
prestacao = valor_casa / meses
if prestacao > (salario * 0.30):
    print("Empréstimo negado (prestação >30% salário)")
else:
    print("Empréstimo aprovado!")

# 7.mini calculadora
n1 = float(input("N1: "))
n2 = float(input("N2: "))
op = input("Operação (+, -, *, /): ")
if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    if n2 != 0:
        print(n1 / n2)
    else:
        print("Divisão por zero!")
else:
    print("Operação inválida")
