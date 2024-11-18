def coletar_itens_e_precos():
    """
    Coleta os itens e seus respectivos preços do usuário.
    Retorna um dicionário com os itens como chaves e os preços como valores.
    """
    itens = {}

    try:
        quantidade = int(input('Quantos itens você quer armazenar? '))
        for _ in range(quantidade):
            item = input('Digite o nome do item: ').strip()
            if item in itens:
                print(f'O item "{item}" já foi adicionado. Atualize ou ignore.')
            else:
                while True:
                    try:
                        preco = float(input(f'Digite o preço para "{item}": '))
                        itens[item] = preco
                        break
                    except ValueError:
                        print("Por favor, digite um valor numérico válido para o preço.")
    except ValueError:
        print("Por favor, insira um número válido para a quantidade de itens.")

    return itens


def exibir_dicionario(dic):
    """Exibe o dicionário formatado de maneira clara para o usuário."""
    print("\nItens e preços armazenados:")
    for item, preco in dic.items():
        print(f"- {item}: R$ {preco:.2f}")
    print(f"\nTotal de itens: {len(dic)}")


def main():
    """Função principal do programa."""
    print("Bem-vindo ao organizador de itens e preços!")
    itens_e_precos = coletar_itens_e_precos()
    if itens_e_precos:
        exibir_dicionario(itens_e_precos)
    else:
        print("Nenhum item foi adicionado.")


if __name__ == "__main__":
    main()
