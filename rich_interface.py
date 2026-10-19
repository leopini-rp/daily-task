from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel


def show_interface(menu_text, content_text, input_text=None):
    console = Console()
    layout = Layout()

    layout.split_row(
        Layout(name="menu", ratio=1),
        Layout(name="content", ratio=2)
    )

    layout["menu"].update(
        Panel(
            menu_text,
            title="Menu"
        )
    )

    layout["content"].update(
        Panel(
            content_text,
            title="Daily Task"
        )
    )

    console.print(layout)


if __name__ == "__main__":
    show_interface()
