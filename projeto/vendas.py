from estoque import produtos


carrinho_de_compras = []


def adicionar_ao_carrinho():
    print("Escolha o codigo do produto que deseja comprar: \n")
    codigo_produto = int(input("codigo do produto: \n"))
    produto_encontrado = False
    for produto in produtos:
        if produto["codigo"] == codigo_produto:
            produto_encontrado = True
            codigo_produto_selecionado = produto["codigo"]
            produto_selecionado = produto['nome']
            preco_produto_selecionado = produto['preco']
            quantidade_produto_selecionado = produto['quantidade']

            print(
                f"Produto selecionado: {produto_selecionado} - Preço: {preco_produto_selecionado} - Quantidade disponível: {quantidade_produto_selecionado}")
            break

    if produto_encontrado:
        quantidade_comprar = int(input("quantidade: \n"))
        if quantidade_comprar <= quantidade_produto_selecionado:
            produto_selecionado = dict(codigo=codigo_produto_selecionado, nome=produto_selecionado,
                                       preco=preco_produto_selecionado, quantidade=quantidade_comprar)
            carrinho_de_compras.append(produto_selecionado)
            print(f"Produto {produto_selecionado} adicionado ao carrinho. Quantidade: {quantidade_comprar} - Preço total: {preco_produto_selecionado * quantidade_comprar}")
        else:
            print(
                "Quantidade solicitada excede a quantidade disponível. Tente novamente.")
    else:
        print("Produto não encontrado. Tente novamente.")

    return carrinho_de_compras


def fechar_compra():
    print("Fechar compra")
    if carrinho_de_compras:
        print("Produtos no carrinho: \n")
        for produto in carrinho_de_compras:
            print(produto)
        preco_total = 0
        for produto in carrinho_de_compras:
            preco_total = produto['preco'] * produto['quantidade']
        print(f"Preço total: {preco_total}")
    else:
        print("O carrinho está vazio. Adicione produtos antes de fechar a compra.")
        return

    valor_pago = float(input("Digite o valor pago pelo cliente: \n"))
    troco = valor_pago - preco_total
    if troco < 0:
        print("Valor pago é insuficiente para cobrir o preço total. Tente novamente.")
    else:
        print(f"Valor pago: {valor_pago}")
        print(f"Troco: {troco}")
        print("Compra finalizada com sucesso. Obrigado pela preferência!")
        for produto_vendido in carrinho_de_compras:
            for produto_estoque in produtos:
                if produto_estoque["codigo"] == produto_vendido["codigo"]:
                    produto_estoque["quantidade"] = produto_estoque["quantidade"] - \
                        produto_vendido["quantidade"]
