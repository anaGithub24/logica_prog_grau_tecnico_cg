
from estoque import listar_produtos, cadastrar_produto
from vendas import adicionar_ao_carrinho, fechar_compra

while (True):
    print("Smart Store \n")
    print("Lista de opcoes: \n")
    print("1. Cadastrar novo produto. \n")
    print("2. Listar produtos disponíveis \n")
    print("3. Vender produto (Adicionar ao carrinho) \n")
    print("4. Fechar compra (Calcular total e troco) \n")
    print("5. Desempacotar Kit Promocional \n")
    print("6. Sair \n")

    opcao = int(input("Escolha sua opcao: "))

    if opcao == 1:
        print("Cadastrar produto")
        codigo = int(input("codigo do produto: \n"))
        nome = input("nome do produto:\n")
        preco = float(input("digite o preco:\n"))
        quantidade = int(input("digite quantidade:\n"))

        cadastrar_produto(codigo=codigo, nome=nome,
                          preco=preco, quantidade=quantidade)

    if opcao == 2:
        listar_produtos()

    if opcao == 3:
        listar_produtos()
        adicionar_ao_carrinho()
    if opcao == 4:
        fechar_compra()
    if opcao == 5:
        print("Desempacotar kit promocional")
    if opcao == 6:
        print("Saindo do sistema. Obrigado por usar a Smart Store!")
        break
