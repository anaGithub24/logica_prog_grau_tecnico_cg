
from estoque import produtos

while (True):
    print("SMART STORE \n")
    print("Lista de opcoes: \n")
    print("1. Cadastrar novo produto. \n")
    print("2. Listar produtos disponíveis \n")
    print("3. Vender produto (Adicionar ao carrinho) \n")
    print("4. Fechar compra (Calcular total e troco) \n")
    print("5. Desempacotar Kit Promocional \n")
    print("6. Sair \n")
    
    opcao=int(input("Escolha sua opcao: "))
    
    if opcao ==1:
        print("Cadastrar produto")
        codigo=int(input("codigo do produto: \n"))
        nome=input("nome do produto:\n")
        preco=float(input("digite o preco:\n"))
        quantidade=int(input("digite quantidae:\n"))
        
        print("Produto cadastrado: \n ")
        novo_produto = dict(codigo=codigo, nome=nome, preco=preco, quantidade=quantidade)
        produtos.append(novo_produto)
        print(novo_produto)
    if opcao==2:
        print("Estoque atual: \n")
        for produto in produtos:
            print(produto)
    if opcao ==3:
        print("adicionar o carrinho")
    if opcao == 4:
        print("fechar compra")
    if opcao ==5:
        print("desempacotar kit promocional")
    if opcao == 6:
        break