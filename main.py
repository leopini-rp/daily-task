from database import (
    db_init
)
from input_validation import (
    validate_option, validate_task_time, clear_screen
)
from tasks import Task, TaskManager


MAIN_MENU = [
    "Adicionar",
    "Listar",
    "Sair",
]


TASKS_MENU = [
    "Marcar/desmarcar tarefa",
    "Editar",
    "Remover",
    "Voltar"
    ]


def show_menu(menu_list):
    for i, action in enumerate(menu_list):
        print(f"{i}- {action}")

    print()

    return range(len(menu_list))


db_init()
clear_screen()
print("Bem vindo ao seu gerenciador de tarefas!\n")

while True:
    while True:
        options = show_menu(MAIN_MENU)
        print()

        option = input("Opção: ")

        validated_option = validate_option(option, options)

        if validated_option is not None:
            break

    option = MAIN_MENU[validated_option]

    if option == "Adicionar":
        clear_screen()
        task_title = input("Digite o nome da tarefa: ")

        while True:
            task_time = input("Horário (HH:MM): ")

            validated_time = validate_task_time(task_time)

            if validated_time is not None:
                break

        task = Task.create_task(task_title, validated_time)
        clear_screen()

    elif option == "Listar":
        clear_screen()
        manager = TaskManager()

        while True:
            manager.show_tasks()

            options = show_menu(TASKS_MENU)

            option = input("Opção: ")

            validated_option = validate_option(option, options)

            if validated_option is not None:
                clear_screen()
                break

        option = TASKS_MENU[validated_option]

        if option == "Marcar/desmarcar tarefa":
            clear_screen()
            manager = TaskManager()

            while True:
                print("Para sair digite 'sair'. \n")
                tasks = manager.show_tasks(show_index=True)

                option = input("Marcar/desmarcar tarefa: ")

                if option.lower() == "sair":
                    clear_screen()
                    break

                validated_option = validate_option(
                    option,
                    range(len(tasks))
                    )

                if validated_option is not None:
                    clear_screen()
                    selected_task = tasks[validated_option]
                    manager.check_completed(selected_task)

        elif option == "Editar":
            clear_screen()
            manager = TaskManager()
            tasks = manager.show_tasks(show_index=True)

            option = input("Editar tarefa: ")

            validated_option = validate_option(
                option,
                range(len(tasks))
            )

            if validated_option is not None:
                clear_screen()
                selected_task = tasks[validated_option]

                manager.edit_task(selected_task)

        elif option == "Remover":
            clear_screen()
            manager = TaskManager()

            while True:
                print("Para sair digite 'sair'. \n")
                tasks = manager.show_tasks(show_index=True)

                option = input("Remover tarefa: ")

                if option.lower() == "sair":
                    clear_screen()
                    break

                validated_option = validate_option(
                    option,
                    range(len(tasks))
                    )

                if validated_option is not None:
                    selected_task = tasks[validated_option]
                    manager.remove_task(selected_task)
                    clear_screen()

        elif option == "Voltar":
            clear_screen()
            continue

    elif option == "Sair":
        clear_screen()
        break
