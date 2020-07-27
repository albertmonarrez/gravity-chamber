"""Configuration file for scripts"""
import os

Z_SAVE_FOLDER = r"DBFighterZ\Saved\SaveGames\29776760"
Z_SAVE_FOLDER_PATH = os.path.join(os.environ.get('localappdata'), Z_SAVE_FOLDER)
SAVE_FILE_NAME = 'SYSTEM.sav'
ROUTINE_BASE_PATH = r'C:\Code Repository\z game files 6-9-2020 (update)'
BACKUP_SAVE_PATH = os.path.join(ROUTINE_BASE_PATH, 'a Backup folder')
ROUTINES = {
    1: r'DEFENSIVE ROUTINE Level 2 (MEDIUM) (done)\SYSTEM.sav',
    2: r'DEFENSIVE ROUTINE Level 3 (EXTREME) (done)\SYSTEM.sav',
    3: r'DEFENSIVE ROUTINE SOLO Level 1 (HARD) (done)\SYSTEM.sav',
}
