from datetime import datetime
import os


def clear_screen():
    os.system("clear")


def validate_option(option, options):
    try:
        option = int(option)

    except ValueError:
        os.system("clear")
        return None

    if option not in options:
        os.system("clear")
        return None

    return option


def validate_task_time(task_time):
    try:
        time_obj = datetime.strptime(task_time, "%H:%M")
        return time_obj.strftime("%H:%M")

    except ValueError:
        clear_screen()
        return None

    return task_time
