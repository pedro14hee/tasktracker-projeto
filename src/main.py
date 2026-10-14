"""TaskTracker - gerenciador de tarefas em linha de comando.

Bootcamp II - Fase 2 (Entrega Intermediária).
"""

PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "media": "Média",
    "média": "Média",
    "baixa": "Baixa",
}


def ler_titulo():
    """Pede o título até que um valor não vazio (e não só espaços) seja digitado."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Título obrigatório!")


def ler_prioridade():
    """Pede a prioridade até receber Alta, Média (ou Media) ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("Prioridade inválida! Digite Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas, proximo_id):
    """Coleta os dados, cria a tarefa com status Pendente e a salva na lista."""
    print("\n--- Cadastrar Nova Tarefa ---")
    titulo = ler_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    """Exibe todas as tarefas ou avisa que a lista está vazia."""
    print("\n--- Tarefas Cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for tarefa in tarefas:
        print("-" * 40)
        print(f"ID:          {tarefa['id']}")
        print(f"Título:      {tarefa['titulo']}")
        print(f"Descrição:   {tarefa['descricao'] or '(sem descrição)'}")
        print(f"Prioridade:  {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite'] or '(não informada)'}")
        print(f"Status:      {tarefa['status']}")
    print("-" * 40)


def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")


def main():
    tarefas = []
    proximo_id = 1

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas, proximo_id)
            proximo_id += 1
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
