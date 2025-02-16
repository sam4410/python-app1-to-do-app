import streamlit as st
import utility_funcs

todos = utility_funcs.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    utility_funcs.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is a todo app built on python")
st.write("This app is aimed to increase my productivity")
edit_button = st.button("Edit", key='todo_to_edit')

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(idx)
        utility_funcs.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a new to-do here:",
              on_change=add_todo, key='new_todo')
