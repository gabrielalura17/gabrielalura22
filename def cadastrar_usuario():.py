print("==============================================")
print("          SEJA BEM-VINDO À NOSSA LOJA1!         ")
print("==============================================")
print("Estamos felizes em ter você aqui!")
print("Esperamos que você encontre tudo o que precisa.")
print("==============================================")

import getpass
import hashlib

usuarios = {}

def cadastrar_usuario():
    """
    Cadastrar um novo usuário
    """
    login = input("Digite nome de usuario: ")
    senha = getpass.getpass("Digite a senha: ")
    cpf = input("Digite o CPF: ")

    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido!")
        return

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    usuarios[login] = {"senha": senha_hash, "cpf": cpf}

    print("Usuário cadastrado com sucesso!")

def login_usuario():
    """
    Fazer login com um usuário existente
    """
    login = input("Digite o login: ")
    senha = getpass.getpass("Digite a senha: ")

    if login not in usuarios:
        print("Usuário não encontrado!")
        return

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    if usuarios[login]["senha"] != senha_hash:
        print("Senha incorreta!")
        return

    print("Login realizado com sucesso!")

def main():
    """
    Loop principal do programa
    """
    while True:
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
produtos = {
    "1": {"nome": "Arroz", "preco": 2.50},
    "2": {"nome": "Feijão", "preco": 3.00},
    "3": {"nome": "Carne", "preco": 10.00},
    "4": {"nome": "Frango", "preco": 8.00},
    "5": {"nome": "Peixe", "preco": 12.00},
    "6": {"nome": "Legumes", "preco": 1.50},
    "7": {"nome": "Frutas", "preco": 2.00},
    "8": {"nome": "Bebidas", "preco": 3.50},
    "9": {"nome": "Doces", "preco": 4.00},
    "10": {"nome": "Salgados", "preco": 5.00}
}

carrinho = {}

def adicionar_produto():
    """
    Adicionar um produto ao carrinho
    """
    print("Produtos disponíveis:")
    for produto in produtos:
        print(f"{produto}: {produtos[produto]['nome']} - R$ {produtos[produto]['preco']:.2f}")
    produto_escolhido = input("Digite o código do produto que deseja adicionar: ")
    if produto_escolhido in produtos:
        quantidade = int(input("Digite a quantidade que deseja adicionar: "))
        if produto_escolhido in carrinho:
            carrinho[produto_escolhido]["quantidade"] += quantidade
        else:
            carrinho[produto_escolhido] = {"nome": produtos[produto_escolhido]["nome"], "preco": produtos[produto_escolhido]["preco"], "quantidade": quantidade}
        print(f"Produto {produtos[produto_escolhido]['nome']} adicionado ao carrinho!")
    else:
        print("Produto não encontrado!")

def remover_produto():
    """
    Remover um produto do carrinho
    """
    print("Produtos no carrinho:")
    for produto in carrinho:
        print(f"{produto}: {carrinho[produto]['nome']} - R$ {carrinho[produto]['preco']:.2f} x {carrinho[produto]['quantidade']}")
    produto_escolhido = input("Digite o código do produto que deseja remover: ")
    if produto_escolhido in carrinho:
        del carrinho[produto_escolhido]
        print(f"Produto {produtos[produto_escolhido]['nome']} removido do carrinho!")
    else:
        print("Produto não encontrado no carrinho!")

def calcular_total():
    """
    Calcular o total do carrinho
    """
    total = 0
    for produto in carrinho:
        total += carrinho[produto]["preco"] * carrinho[produto]["quantidade"]
    print(f"Total: R$ {total:.2f}")

def main():
    """
    Loop principal do programa
    """
    while True:
        print("1. Adicionar produto ao carrinho")
        print("2. Remover produto do carrinho")
        print("3. Calcular total")
        print("4. Sair")
        opcao = input("Digite a opção: ")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            calcular_total()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
