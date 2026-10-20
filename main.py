from database import (
    db_init
)
from input_validation import (
    clear_screen
)
from menu import MainMenu


db_init()
clear_screen()

main_menu = MainMenu()

main_menu.run()
