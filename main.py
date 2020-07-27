import move_files
import sys

if __name__ == '__main__':
    routine = int(sys.argv[1])
    files = move_files.MoveSaveFiles()
    files.move_files(routine)
    print('Moved some files around.')
