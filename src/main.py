import manager
import pyfiglet


def main():

    result = pyfiglet.figlet_format("The Village", font="banner")
    print(result)
    game = manager.Instance()

    a = input()
    read = ''
    while read != 'q':
        game.tick_day()
        read = input()

if __name__ == "__main__":
    main()
