import move_files
import sys

if __name__ == '__main__':
    routine = int(sys.argv[1])
    file_mover = move_files.SaveFileMover()
    file_mover.move_files(routine)
    print('Moved some files around.')
