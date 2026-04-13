
from modulo_3.modulo8 import exercicio_3_pares_impares


def desafio_extra_agenda():
    contatos = {}

    while True:
        print("\n--- Agenda de Contatos ---")
        print("1. Adicionar/Atualizar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Listar todos")
        print("5. Voltar ao menu principal")

        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            nome = input("Nome: ").strip()
            telefone = input("Telefone: ").strip()

            if nome and telefone:
                contatos[nome] = telefone
                print(f"Contato '{nome}' foi salvo/atualizado com sucesso.")
            else:
                print("Nome e telefone são obrigatórios.")

        elif opc == "2":
            nome = input("Nome do contato a remover: ").strip()
            if nome in contatos:
                del contatos[nome]
                print(f"Contato '{nome}' foi removido.")
            else:
                print("Contato não encontrado.")

        elif opc == "3":
            nome = input("Nome do contato a buscar: ").strip()
            if nome in contatos:
                print(f"{nome}: {contatos[nome]}")
            else:
                print("Contato não encontrado.")

        elif opc == "4":
            if contatos:
                print("\n--- Lista de Contatos ---")
                for nome, telefone in contatos.items():
                    print(f"{nome}: {telefone}")
            else:
                print("Nenhum contato cadastrado.")

        elif opc == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")



def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Exercício 1 - Lista de Compras")
        print("2. Exercício 2 - Dicionário de Aluno")
        print("3. Exercício 3 - Números Pares e Ímpares")
        print("4. Desafio Extra - Agenda de Contatos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            exercicio_1_lista_compras()  # pyright: ignore[reportUndefinedVariable]
        elif escolha == "2":
            exercicio_2_dicionario_aluno() # pyright: ignore[reportUndefinedVariable]
        elif escolha == "3":
            exercicio_3_pares_impares()
        elif escolha == "4":
            desafio_extra_agenda()
        elif escolha == "5":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "_main_":
    main()