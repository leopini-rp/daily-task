import readline
from database import (
    save_db_item, get_all, update_completed, update_task, remove_task
)
from input_validation import (
    validate_task_time
)
import os


class Task:
    def __init__(self, title, time, completed=False, id_=None):
        self.title = title
        self.time = time
        self.completed = completed
        self.id_ = id_

    @classmethod
    def create_task(cls, task_title, task_time):
        task = Task(
            title=task_title,
            time=task_time,
            id_=save_db_item(task_title, task_time)
        )

        return task


class TaskManager:
    def list_tasks(self):
        rows = get_all()

        tasks = []

        for row in rows:
            tasks.append(
                Task(
                    id_=row[0],
                    title=row[1],
                    time=row[2],
                    completed=row[3],
                )
            )

        return tasks

    def show_tasks(self, show_index=False):
        tasks = self.list_tasks()
        sorted_tasks = sorted(
            tasks,
            key=lambda task: task.time, reverse=True
        )

        for i, task in enumerate(sorted_tasks):
            completed_check = (
                "✓" if task.completed else " "
            )

            if show_index:
                print(f"{i}- [{completed_check}] {task.time} - {task.title}")

            else:
                print(f"[{completed_check}] {task.time} - {task.title}")

        print()

        return tasks

    def check_completed(self, selected_task):
        selected_task.completed = int(not selected_task.completed)

        update_completed(selected_task.completed, selected_task.id_)

    def edit_task(self, selected_task):
        readline.set_startup_hook(
            lambda: readline.insert_text(selected_task.title)
        )

        new_title = input("Editar título: ")

        readline.set_startup_hook()

        while True:
            readline.set_startup_hook(
                lambda: readline.insert_text(selected_task.time)
            )

            new_time = input("Editar horário: ")

            readline.set_startup_hook()

            validated_time = validate_task_time(new_time)

            if validated_time is not None:
                break

        task_id = selected_task.id_

        update_task(new_title, new_time, task_id)

    def remove_task(self, selected_task):
        valid_answer = ["Y", "y", "N", "n"]
        confirm_remove = ""

        while confirm_remove not in valid_answer:
            os.system("clear")
            confirm_remove = input(
                f"Deseja remover '{selected_task.title}'? (Y/N) \n"
            )

        if confirm_remove.lower() == "y":
            remove_task(selected_task.id_)

        else:
            return
