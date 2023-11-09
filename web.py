import streamlit as st
from modules import functions

# Global variables
todos = functions.get_todos()

# Global fucntions
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# def completed_todo():
#     for checkbox in st.checkbox():



# Layout of web page
st.title("My Todo App")
st.subheader("This is my todo web app")
st.write("This app is to incerase my productivity")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(on_change=add_todo, key ="new_todo",
              label="", placeholder="Add new todo...")

st.button("Edit")
st.button("Completed")
st.session_state










