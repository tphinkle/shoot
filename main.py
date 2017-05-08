# Python standard library
import sys

sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/entity')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/component')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/system')

# Game
import system as system


if __name__ == "__main__":

    game_system = system.System()
    sys.exit(game_system.Run())
