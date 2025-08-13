# import os.path


def copy_file(files_names: str) -> None:
    file_list = files_names.split(" ")
    if len(file_list) != 3 or file_list[0] != "cp":
        return

    _, f1, f2 = file_list

    if f1 == f2:
        return

    # if not os.path.exists(f1):
    #     return
    try:
        with open(f1, "r") as file_1, open(f2, "w") as file_2:
            data = file_1.read()
            file_2.write(data)
    except FileNotFoundError:
        return
