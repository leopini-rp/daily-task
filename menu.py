from abc import ABC, abstractmethod
from input_validation import (
    validate_option, validate_task_time, clear_screen
)
from tasks import Task, TaskManager
from rich_interface import show_interface


class Menu(ABC):
    def __init__(self, menu_options):
        self.menu_options = menu_options

    def show_menu(self, selected=None):
        menu_text = ""

        for i, action in enumerate(self.menu_options):
            if action == selected:
                menu_text += (f"[green]{i}- {action}[/green]\n")
            else:
                menu_text += f"{i}- {action}\n"
        return menu_text

    def select_menu_option(self):
        while True:
            option = input("Opção: ")

            validated_option = validate_option(
                option,
                range(len(self.menu_options))
            )

            if validated_option is not None:
                return self.menu_options[validated_option]

    def get_valid_option(self, tasks):
        option = input()

        if option.lower() == "sair":
            return option

        validated_option = validate_option(
            option,
            range(len(tasks))
        )

        if validated_option is not None:
            return tasks[validated_option]

        return None

    @abstractmethod
    def run(self):
        pass


class MainMenu(Menu):
    def __init__(self):
        super().__init__([
            "Adicionar",
            "Listar",
            "Sair"
        ])

    def run(self):
        while True:
            # rich_interface func
            show_interface(
                self.show_menu(),
                "Bem vindo ao seu gerenciador de tarefas!",
                "Opção: "
            )

            option = self.select_menu_option()

            if option == "Adicionar":
                self.add_task()

            elif option == "Listar":
                TasksMenu().run()

            elif option == "Sair":
                clear_screen()
                break

    def add_task(self):
        clear_screen()
        input_text = "Digite o nome da tarefa:"

        show_interface(
            self.show_menu("Adicionar"),
            f"{input_text}",
        )

        task_title = input()
        input_text = "Horário (HH:MM):\n"

        while True:
            clear_screen()
            show_interface(
                self.show_menu("Adicionar"),
                f"{input_text}"
            )

            task_time = input()

            validated_time = validate_task_time(task_time)

            if validated_time is not None:
                break

            else:
                input_text = "Horário inválido!\nHorário (HH:MM):"

        Task.create_task(task_title.strip(), validated_time)
        clear_screen()


class TasksMenu(Menu):
    def __init__(self, ):
        super().__init__([
            "Marcar/desmarcar tarefa",
            "Editar",
            "Remover",
            "Voltar"
        ])

    def run(self):
        clear_screen()

        while True:
            manager = TaskManager()

            show_interface(
                self.show_menu(),
                manager.show_tasks()
            )

            option = self.select_menu_option()

            if option == "Marcar/desmarcar tarefa":
                self.check_tasks()

            elif option == "Editar":
                self.edit_task()

            elif option == "Remover":
                self.remove_task()

            elif option == "Voltar":
                clear_screen()
                return

    def check_tasks(self):
        clear_screen()
        manager = TaskManager()

        input_text = "Para sair digite 'sair' \n"

        while True:
            tasks = manager.list_tasks()

            tasks_text = manager.show_tasks(show_index=True)

            show_interface(
                self.show_menu("Marcar/desmarcar tarefa"),
                f"{tasks_text}\n{input_text}"
            )

            selected_option = self.get_valid_option(
                tasks
            )

            if selected_option is None:
                input_text = (
                    "OPÇÃO INVÁLIDA!\n"
                    "Para sair digite 'sair' \n"
                )
                continue

            else:
                input_text = "Para sair digite 'sair' \n"

            if (
                isinstance(selected_option, str)
                and selected_option.lower() == "sair"
            ):
                clear_screen()
                break

            clear_screen()
            manager.check_completed(selected_option)

    def edit_task(self):
        clear_screen()

        manager = TaskManager()

        tasks = manager.list_tasks()

        tasks_text = manager.show_tasks(show_index=True)

        input_text = "Para sair digite 'sair' \n"

        while True:
            show_interface(
                self.show_menu("Editar"),
                f"{tasks_text}\n{input_text}"
            )

            selected_option = self.get_valid_option(
                tasks
            )

            if selected_option is None:
                input_text = (
                    "OPÇÃO INVÁLIDA!\n"
                    "Para sair digite 'sair' \n"
                )
                continue

            else:
                break

        clear_screen()
        if (
            isinstance(selected_option, str)
            and selected_option.lower() == "sair"
        ):
            return

        manager.edit_task(selected_option)

    def remove_task(self):
        clear_screen()
        manager = TaskManager()
        input_text = "Para sair digite 'sair' \n"

        while True:
            tasks = manager.list_tasks()
            tasks_text = manager.show_tasks(show_index=True)

            show_interface(
                self.show_menu("Remover"),
                f"{tasks_text}\n{input_text}"
            )

            selected_option = self.get_valid_option(tasks)

            if selected_option is None:
                input_text = (
                    "OPÇÃO INVÁLIDA!\n"
                    "Para sair digite 'sair' \n"
                )
                continue

            if (
                isinstance(selected_option, str)
                and selected_option.lower() == "sair"
            ):
                clear_screen()
                break

            input_text = "Para sair digite 'sair' \n"
            manager.remove_task(selected_option, self.show_menu("Remover"))
            clear_screen()
