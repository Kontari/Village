#import menu_wrapper
#import curses
#import curses
import manager


def main():

  game = manager.Instance()

  read = ''
  while read != 'q':

    game.tick_day()
    read = input()

if __name__ == "__main__":
    main()