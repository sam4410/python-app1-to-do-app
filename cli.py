# from modules.utility_funcs import get_todos, write_todos
import utility_funcs
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
while True:
    # strip the space characters from user input
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    # check if user provided action is to 'add' and item
    if user_action.startswith('add'):
        todo = user_action[4:].strip()

        todos = utility_funcs.get_todos()   # function call

        todos.append(todo + '\n')

        utility_funcs.write_todos(todos_arg=todos)

    elif user_action.startswith('show') or user_action.startswith('display'):
        # check if user provided action is to 'show' list of items
        todos = utility_funcs.get_todos()

        # new_todos = [x.strip('\n') for x in todos]    # list comprehension for removing \n
        for idx, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{idx + 1}-{todo.title()}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            # check if user provided action is to 'edit' a particular item
            number = int(user_action[5:])

            todos = utility_funcs.get_todos()

            print(f"You want to edit todo item at position: {number}")
            user_confirmation = input("Is that correct? Answer in Yes or No: ")
            replace_value = input("What new todo you want to replace with: ") + "\n"
            if user_confirmation == "Yes":
                todos[number-1] = replace_value

            utility_funcs.write_todos(todos_arg=todos)

        except ValueError:
            print("Your command is not valid. Missing a number after calling 'edit'..")
            continue

    elif user_action.startswith('complete'):
        try:
            # check if user provided action is to mark 'complete' and remove item from list
            todo_completed = int(user_action[9:]) - 1
            print(f"Position of item to be removed: {todo_completed + 1}")

            todos = utility_funcs.get_todos()

            todo_to_remove = todos[todo_completed].strip('\n')
            todos.pop(todo_completed)

            utility_funcs.write_todos(todos_arg=todos)

            message = f"Todo '{todo_to_remove.title()}' has been removed successfully!"
            print(message)
        except IndexError:
            print("There is no todo item to remove at provided index position..")

    elif user_action.startswith('exit'):
        # check if user provided action is to 'exit' from program
        break
    else:
        # check if user has not provided a valid action
        print("Hey, you entered an unknown command. Please check!")

print('Bye!')
