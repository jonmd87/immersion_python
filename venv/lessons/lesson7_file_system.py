import os
from pathlib import Path

## how to know current directory
# print(os.getcwd()) #old style >>> /home/evghen/prog/immersion_in_python/venv/lessons
# print(Path.cwd()) # >>> /home/evghen/prog/immersion_in_python/venv/lessons

## how to make directory
# os.mkdir("new_dir_by_os")
# Path("new_dir_by_Path").mkdir()
## how to make subfolders
os.makedirs("new_dir_by_os/os_dirs/first")
Path("new_dir_by_Path/Path_dirs/first").mkdir(parents=True)