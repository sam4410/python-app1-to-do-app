FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write an updated list of to-do items into a text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


print(__name__)
if __name__ == "__main__":
    print("Hello from utility_funcs")
    print(get_todos())
