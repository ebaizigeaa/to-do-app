FILEPATH = "todolist.txt"


def readtodos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def writetodos(todos, filepath=FILEPATH):
    """
    Write the to-do items in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("Hello")
    print(readtodos())

