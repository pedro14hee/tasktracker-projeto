def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")


def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break


if __name__ == "__main__":
    main()
