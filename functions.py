FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """ Read the text file and return a list of to-do items."""
    with open(filepath, "r") as files:
        todos_local = files.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file. """
    with open(filepath, "w") as files:
        files.writelines(todos_arg)
