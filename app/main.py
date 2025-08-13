import os.path


def copy_file(files_names: str) -> None:
    file_list = files_names.split(" ")
    if len(file_list) != 3 or file_list[0] != "cp":
        return None

    _, file1, file2 = file_list

    if file1 == file2:
        return None

    if not os.path.exists(file1):
        return None

    with open(file1, "rb") as file_1, open(file2, "wb") as file_2:
        data = file_1.read()
        file_2.write(data)
