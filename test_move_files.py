import unittest
import move_files


class TestMoveFiles(unittest.TestCase):
    def test_move_files(self):
        file_manager = move_files.MoveSaveFiles()
        file_manager.move_files(1)
        print('does a thing')

    def test_routine_1(self):
        file_manager = move_files.MoveSaveFiles()
        file_manager.move_files(1)
        print('does a thing')

    def test_routine_2(self):
        file_manager = move_files.MoveSaveFiles()
        file_manager.move_files(2)
        print('does a thing')

    def test_routine_3(self):
        " "

    def test_backup_files(self):
        " "
