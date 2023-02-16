import streamlit as sl
import functions

# Access file
todos = functions.get_todos()


# Add a new item
def add_todo():
    todo = sl.session_state["new_todos"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# Set page elements
sl.set_page_config(layout="wide")
sl.title("My Todo App")
sl.subheader("This is My-Todo App.")
sl.write("<b>This app is designed to help you increase your productivity.</b>", unsafe_allow_html=True)

sl.text_input(label="Enter a new task: ", placeholder="Add a new task...",
              on_change=add_todo, key="new_todos")
sl.write("Check to complete a task")
sl.write("Your pending tasks:")
for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo.capitalize(), key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()
