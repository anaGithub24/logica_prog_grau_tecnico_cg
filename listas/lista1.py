#0

# Mensagem inicial
# print("ola,mundo!")
# funcao print: funcao de saida / exibicao de dados

# 1. Identificação de Tipos
# o python identifica o tipo de variavel
# formato de declaracao de variavel: nome_da_variavel = valor_da_variavel
# nao e necessario (;) no final da declaracao

nome = "ESTER" # para toda string o valor precisa estar entre aspas 
idade = 17
peso = 10.5 # se utiliza (.) no lugar da virgula
menor_de_idade = True # valores possiveis: True ou False

# funcao type: funcao para mostrar o tipo da variavel

#print(type(nome))   # str
#print(type(idade))  # int
#print(type(peso))   # float
#print(type(menor_de_idade)) # bool

# 2. O "Bug" da Concatenação (Casting)

# concatenacao (juncao) de variaveis e por meio do sinal de (+)
# print("Eu tenho " + idade + " anos.") # codigo original
# motivo do erro: em python nao se junta variaveis de tipos diferentes

# conceito de conversao (cast)
# Convertendo de int para str
print("Eu tenho " + str(idade) + " meses.")

# 3. Soma de Inputs (Cuidado com Strings)

# funcao input: funcao de entrada / coleta de dados
# funcao print: funcao de saida / exibicao de dados

numero_1 = input("me de um numero: ") # numero_1 recebe um texto. Exemplo: "22"
numero_2 = input("me de outro numero: ") # numero_2 recebe um texto. Exemplo: "23"

# Convertendo str para int
soma=(int(numero_1) + int(numero_2))
print(soma)

# 4. Conversão de Float para Int

num = 15.89
inteiro = int(num)
print(inteiro)  # 15  
# não arredonda, apenas  removeu a parte decimal)

# 5. O Poder do Booleano
x = 10
y = 5
resultado = x > y
print(resultado)    # True
print(type(resultado)) # bool

# 6.  Informações do Usuário (Formatação)

nome = input("Nome: ")
idade = int(input("Idade: "))
altura = float(input("Altura (ex: 1.75): "))
print(f"Olá {nome}, você tem {idade} anos e mede {altura} metros.")

# 7. Tipos dentro de Strings
# numero_texto = "50" → converter para int, float e manter string, multiplicar por 2.
numero_texto = "50"
int_n = int(numero_texto) * 2
float_n = float(numero_texto) * 2
str_n = numero_texto * 2

print(int_n)    # 100
print(float_n)  # 100.0
print(str_n)    # "5050" (concatenação de string)


