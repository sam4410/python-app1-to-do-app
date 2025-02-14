import utility_funcs
import FreeSimpleGUI as Fsg

label = Fsg.Text("Type in a to-do item")
input_box = Fsg.InputText(tooltip="Enter to-do", key='to-do')
add_button = Fsg.Button("Add")
list_box = Fsg.Listbox(values=utility_funcs.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = Fsg.Button("Edit")

window = Fsg.Window('My To-Do App',
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = utility_funcs.get_todos()
            todo = values['to-do'] + '\n'
            todos.append(todo)
            utility_funcs.write_todos(todos_arg=todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['to-do'] + '\n'
            todos = utility_funcs.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            utility_funcs.write_todos(todos_arg=todos)
            window['todos'].update(values=todos)
        case "todos":
            window['to-do'].update(value=values['todos'][0])
        case Fsg.WINDOW_CLOSED:
            break

window.close()
