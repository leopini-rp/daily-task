from abc import ABC, abstractmethod
from input_validation import (
    validate_option, validate_task_time, clear_screen
)
from tasks import Task, TaskManager


class Menu(ABC):
    def __init__(self, menu_options):
        self.menu_options = menu_options

    def show_menu(self):
        for i, action in enumerate(self.menu_options):
            print(f"{i}- {action}")

        print()

        return range(len(self.menu_options))

    def select_menu_option(self):
        while True:
            self.show_menu()

            option = input("Opção: ")

            validated_option = validate_option(
                option,
                range(len(self.menu_options))
            )

            if validated_option is not None:
                return self.menu_options[validated_option]

    def get_valid_option(self, text_, tasks):
        while True:
            option = input(f"{text_}: ")

            if option.lower() == "sair":
                return option

            validated_option = validate_option(
                option,
                range(len(tasks))
            )

            if validated_option is not None:
                return tasks[validated_option]

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
        task_title = input("Digite o nome da tarefa: ")

        while True:
            task_time = input("Horário (HH:MM): ")

            validated_time = validate_task_time(task_time)

            if validated_time is not None:
                break

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
            manager.show_tasks()

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

        while True:
            print("Para sair digite 'sair'. \n")
            tasks = manager.show_tasks(show_index=True)

            selected_option = self.get_valid_option(
                "Marcar/desmarcar tarefa",
                tasks
            )

            if selected_option == "sair":
                clear_screen()
                break

            clear_screen()
            manager.check_completed(selected_option)

    def edit_task(self):
        clear_screen()
        manager = TaskManager()
        tasks = manager.show_tasks(show_index=True)

        selected_option = self.get_valid_option(
            "Editar tarefa",
            tasks
        )

        clear_screen()
        manager.edit_task(selected_option)

    def remove_task(self):
        clear_screen()
        manager = TaskManager()

        while True:
            print("Para sair digite 'sair'. \n")
            tasks = manager.show_tasks(show_index=True)

            selected_option = self.get_valid_option(
                "Remover tarefa",
                tasks
            )

            if selected_option == "sair":
                clear_screen()
                break

            manager.remove_task(selected_option)
            clear_screen()
