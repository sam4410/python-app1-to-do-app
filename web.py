import streamlit as st
import utility_funcs

todos = utility_funcs.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    utility_funcs.write_todos(todos)
    print(todo)


st.title("My ToDo App")
st.subheader("This is a todo app built on python")
st.write("This app is aimed to increase my productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new to-do here:",
              on_change=add_todo, key='new_todo')

st.session_state


