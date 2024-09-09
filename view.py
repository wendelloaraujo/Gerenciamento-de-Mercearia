import Controller
import os.path


def criarArquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")


criarArquivos("categoria.txt", "clientes.txt", "estoque.txt", "fornecedores.txt", "funcionarios.txt", "venda.txt")

if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar (Categorias)\n"
                          "Digite 2 para acessar (Estoque)\n"
                          "Digite 3 para acessar (Fornecedor)\n"
                          "Digite 4 para acessar (Cliente)\n"
                          "Digite 5 para acessar (Funcionario)\n"
                          "Digite 6 para acessar (Vendas)\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 8 para sair\n"))

        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar\n")
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja remover\n")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a categoria que deseja alterar\n")
                    novaCategoria = input("Digite a categoria para qual deseja alterar\n")
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break

        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para ver o estoque\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do produto: \n")
                    preco = input("Digite o preço do produto:\n")
                    categoria = input("Digite a categoria do produto:\n")
                    quantidade = input("Digite a quantidade do produto:\n")
                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    nome = input("Digite o produto que deseja remover\n")
                    cat.removerProduto(nome)
                elif decidir == 3:
                    nome = input("Digite o produto que deseja alterar\n")
                    nomeAlterar = input("Digite o produto para qual deseja alterar\n")
                    preco = input("Digite o preço do novo produto\n")
                    categoria = input("Digite a categoria do novo produto\n")
                    quantidade = input("Digite a quantidade do novo produto\n")
                    cat.alterarProduto(nomeAlterar, nome, preco, categoria, quantidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break

        elif local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para ver os fornecedores\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do fornecedor: \n")
                    cnpj = input("Digite o cnpj do fornecedor:\n")
                    telefone = input("Digite o telefone do fornecedor:\n")
                    categoria = input("Digite a categoria do fornecedor:\n")
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    nome = input("Digite o fornecedor que deseja remover\n")
                    cat.removerFornecedor(nome)
                elif decidir == 3:
                    nome = input("Digite o nome do fornecedor que deseja alterar\n")
                    nomeAlterar = input("Digite o nome do fornecedor para qual deseja alterar\n")
                    cnpj = input("Digite o novo cnpj do fornecedor\n")
                    telefone = input("Digite o telefone do novo fornecedor\n")
                    categoria = input("Digite a categoria do novo fornecedor\n")
                    cat.alterarFornecedor(nome, nomeAlterar, cnpj, telefone, categoria)
                elif decidir == 4:
                    cat.mostrarFornecedores()
                else:
                    break

        elif local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para ver os clientes\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do cliente: \n")
                    telefone = input("Digite o telefone do cliente:\n")
                    cpf = input("Digite o cpf do cliente:\n")
                    email = input("Digite o email do cliente:\n")
                    endereco = input("Digite o endereço do cliente:\n")
                    cat.cadastrarCliente(nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    nome = input("Digite o cliente que deseja remover\n")
                    cat.removerCliente(nome)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do cliente que deseja alterar\n")
                    novoNome = input("Digite o novo nome do cliente\n")
                    novoTelefone = input("Digite o novo telefone do cliente\n")
                    novoCpf = input("Digite o novo cpf do cliente\n")
                    novoEmail = input("Digite o novo email do cliente\n")
                    novoEndereco = input("Digite o novo endereco do cliente\n")
                    cat.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cat.mostrarClientes()
                else:
                    break

        elif local == 5:
            cat = Controller.ControllerFuncionario()
            while True:
                decidir = int(input("Digite 1 para cadastrar um funcionário\n"
                                    "Digite 2 para remover um funcionário\n"
                                    "Digite 3 para alterar um funcionário\n"
                                    "Digite 4 para ver os funcionários\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    clt = input("Digite a clt do funcionário: \n")
                    nome = input("Digite o nome do funcionário: \n")
                    telefone = input("Digite o telefone do funcionário:\n")
                    cpf = input("Digite o cpf do funcionário:\n")
                    email = input("Digite o email do funcionário:\n")
                    endereco = input("Digite o endereço do funcionário:\n")
                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    nome = input("Digite o funcionário que deseja remover\n")
                    cat.removerFuncionario(nome)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do funcionário que deseja alterar\n")
                    novoClt = input("Digite o novo clt do funcionário\n")
                    novoNome = input("Digite o novo nome do funcionário\n")
                    novoTelefone = input("Digite o novo telefone do funcionário\n")
                    novoCpf = input("Digite o novo cpf do funcionário\n")
                    novoEmail = input("Digite o novo email do funcionário\n")
                    novoEndereco = input("Digite o novo endereco do funcionário\n")
                    cat.alterarFuncionario(nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cat.mostrarFuncionario()
                else:
                    break

        elif local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = int(input("Digite 1 para realizar uma venda\n"
                                    "Digite 2 para ver as vendas\n"
                                    "Digite 3 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do produto\n")
                    vendedor = input("Digite o nome do vendedor\n")
                    comprador = input("Digite o nome do cliente\n")
                    quantidade = input("Informe a quantidade do produto\n")
                    cat.cadastrarVenda(nome, vendedor, comprador, quantidade)
                elif decidir == 2:
                    dataInicio = input("Digite a data de inicio no formato dia/mes/ano:\n")
                    dataTermino = input("Digite a data de termino no formato dia/mes/ano:\n")
                    cat.mostrarVenda(dataInicio, dataTermino)
                else:
                    break


        elif local == 7:
            a = Controller.ControllerVenda()
            a.relatorioProdutos()
        else:
            break