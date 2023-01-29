import streamlit as sl
import functions

todos = functions.get_todos()


def add_todo():
    todo = sl.session_state["new_todos"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


sl.title("Task Manager")
sl.subheader("This is My-Todo App.")
sl.write("This app is designed to help you increase your productivity.")
sl.write("Your pending tasks:")
for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo.title(), key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()

sl.write("Tick to complete a task")
sl.text_input(label="Enter a new task: ", placeholder="Add a new task...",
              on_change=add_todo, key="new_todos")

