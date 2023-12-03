import os
import time
from pyfiglet import figlet
from colorama import fore, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    def display_text_animation(text, delay=1.0, clear=True):
        fig = figlet(font='slant')
        if clear:
            clear_screen()
        for line in text.splitlines():
            print(fore.RED + fig.renderText(line))
            time.sleep(delay)

def main():
    display_text_animation("I", delay=0.5)
    display_text_animation("I Like", delay=0.5)
    display_text_animation("I Lke You", delay=0.5)

    response = ask_question("You Like Me?")

    if response == 'yes':
        display_text_animation("I Love", delay=0.5)
        display_text_animation("I Love You", delay=0.5)

        print(fore.RED + "hehe<3")

    elif response == 'no':
        display_text_animation("H", delay=0.5)
        display_text_animation("Hh", delay=0.5)
        display_text_animation("Hhh", delay=0.5)
        display_text_animation("Hhhh", delay=0.5)
        display_text_animation("Hhhhh", delay=0.5)
        clear_screen()
        display_text_animation("Hhhhh", delay=0.5)

if __name__ == "__main__":
    main()