import utility_funcs
import FreeSimpleGUI as Fsg

label = Fsg.Text("Type in a to-do item")
input_box = Fsg.InputText(tooltip="Enter to-do", key='to-do')
add_button = Fsg.Button("Add")

window = Fsg.Window('My To-Do App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = utility_funcs.get_todos()
            todos.append(values['to-do'] + '\n')
            utility_funcs.write_todos(todos_arg=todos)
        case Fsg.WINDOW_CLOSED:
            break

window.close()
