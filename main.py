# Python standard library
import sys

sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/entity')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/component')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/system')

# Game
import system


if __name__ == "__main__":

    system = system.System()
    sys.exit(system.Run())
