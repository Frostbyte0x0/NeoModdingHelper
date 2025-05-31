import os

def camel_to_snake(string: str):
    return "_".join([s.lower() for s in string.split("ABCDEFGHIJKLMNOPQRSTUVWXYZ")])

def snake_to_camel(string: str):
    return "".join([s.capitalize() for s in string.split("_")])


def select_from_menu(options: list[str]) -> int:
    for i in range(len(options)):
        print(str(i+1) + ": " + options[i].capitalize())

    out = int(input("> "))
    return out - 1


def load_template(file: str, camel_name: str, mod_id: str, package: str):
    with open("templates/" + file + ".txt", "r") as f:
        template = f.read()

    snake_name = camel_to_snake(camel_name)

    template = (template.replace("^P", camel_name.capitalize())
                .replace("^S", snake_name)
                .replace("^U", snake_name.upper())
                .replace("^M", mod_id)
                .replace("^J", package)
                .replace("^N", snake_name.replace("_", " ").capitalize())
                .replace("^C", camel_name))

    return template


def write_to_file(path_to_file: str, text: str, line_offset: int, from_bottom: bool = True):
    print(f"Writing to file '{path_to_file}'")
    try:
        with open(path_to_file, "r") as f:
            lines = f.readlines()

        index = len(lines) - line_offset if from_bottom else line_offset
        lines.insert(index, text)

        with open(path_to_file, "w") as f:
            f.writelines(lines)
    except:
        print(f"Failed to write to file '{path_to_file}'")


def write_to_new_file(path: str, file_name: str, text: str):
    print(f"Creating new file '{path + '/' + file_name}'")
    try:
        with open(path + "/" + file_name, "w") as f:
            f.write(text)
    except:
        print(f"Failed to create new file '{path + '/' + file_name}'")


def erase_from_file(path_to_file: str, text: str):
    print(f"Erasing from file '{path_to_file}'")
    try:
        with open(path_to_file, "r") as f:
            txt = f.read()

        txt = txt.replace(text, "")

        with open(path_to_file, "w") as f:
            f.writelines(txt)
    except:
        print(f"Failed to erase from file '{path_to_file}'")


def erase_file(path_to_file: str):
    print(f"Erasing file '{path_to_file}'")
    try:
        os.remove(path_to_file)
    except:
        print(f"Failed to erase file '{path_to_file}'")


def get_all_folders(path: str):
    return [entry.name for entry in os.scandir(path) if entry.is_dir()]

def get_all_files(path: str):
    return [entry.name for entry in os.scandir(path) if not entry.is_dir()]

