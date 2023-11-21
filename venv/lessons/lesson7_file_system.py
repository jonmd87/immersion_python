import os
from pathlib import Path

## how to know current directory
# print(os.getcwd()) #old style >>> /home/evghen/prog/immersion_in_python/venv/lessons
# print(Path.cwd()) # >>> /home/evghen/prog/immersion_in_python/venv/lessons

## how to make directory
# os.mkdir("new_dir_by_os")
# Path("new_dir_by_Path").mkdir()
## how to make subfolders
# os.makedirs("new_dir_by_os/os_dirs/first")
# Path("new_dir_by_Path/Path_dirs/first").mkdir(parents=True)

##how to remove directory
# os.rmdir("new_dir_by_os") #only when directory is empty
# Path("new_dir_by_os").rmdir() #only when directory is empty

## how to get list of directories and files
# print(os.listdir())
# p = Path(Path().cwd())
# for obj in p.iterdir():
#       print(obj)


## how to check if directory or file or link
# obj_lst = os.listdir()
# for item in obj_lst:
#     if os.path.isdir(item):
#         print(f"{item} = directory")
#     elif os.path.isfile(item):
#         print(f"{item} = file")
#     else:
#         print(f"{item} = link")

# p = Path(Path().cwd())
# for obj in p.iterdir():
#     if obj.is_dir():
#         print(f"dir{obj.name} D")
#     elif obj.is_file():
#         print(f"\t\tfile: {obj.name} F")
#     elif obj.is_symlink():
#         print(f"\t\tlink:{obj.name} @")
#     else:
#         print(f"\t\tobkect{obj.name} O")

## method os.walk()
# for dir_path, dir_name, file_name in os.walk(os.getcwd()):
#     print(f"{dir_path = } {dir_name = } {file_name =}")

## how to rename file
# os.rename("old_name", "new_name")
# Path("old_name").rename("new_name")

## how to replace file
# os.replace()
# Path.replace()