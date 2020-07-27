import config
import pathlib
from pathlib import Path
import shutil
import datetime


class MoveSaveFiles:
    def __init__(self):
        self.save_folder = config.Z_SAVE_FOLDER_PATH
        self.current_save_file = Path(self.save_folder, config.SAVE_FILE_NAME)
        self.routines_path = config.ROUTINE_BASE_PATH
        self.backup_directory = Path(config.BACKUP_SAVE_PATH)

    def move_files(self, routine_number: int):
        if self.current_save_file.exists():
            self.backup(self.current_save_file)
            routine = Path(self.routines_path, config.ROUTINES.get(routine_number))
            if routine.exists():
                shutil.copy2(routine, self.current_save_file)

    def backup(self, save_file: pathlib.WindowsPath) -> None:
        """Backs up the current save file to backup folder"""
        if self.backup_directory.exists():
            name = f"{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')} {save_file.name}"
            save_copy = Path(self.backup_directory, name)
            return shutil.copy2(save_file, save_copy)

        raise FileNotFoundError("backup directory: {} does not exist".format(self.backup_directory))
