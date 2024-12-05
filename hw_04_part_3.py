from colorama import Fore
from pathlib import Path
import sys
path = sys.argv[1]

start_folder_path = Path(path)
# function is to built structure of indicated folder
def parse_folder(path, prefix="     "):
    try:
        for item in path.iterdir(): #cycle to go through folders in underlevel of start folder
            if item.is_dir():
                print(Fore.RED + f" 📂{item.name}") #print folders names with red colour
                parse_folder(item)
            if item.is_file():
                print(Fore.GREEN + f" {prefix}┣📜{item.name}") #print files names with green colours
    except FileNotFoundError:
        (print("Directory does not exist or wrong path specified"))

parse_folder(start_folder_path)

