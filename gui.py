from modules import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


sg.theme("DarkPurple4")
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size = [45,10])
edit_button = sg.Button("Edit")
completed_button = sg.Button("Completed")
exit_button = sg.Button("Exit")


window = sg.Window("My To-Do App",
                   layout=[[clock],
                            [label],
                           [input_box, add_button],
                           [list_box, edit_button, completed_button],[exit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case sg.WIN_CLOSED:
            break
        case "Exit":
            exit()
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todos = functions.get_todos()
            value_to_edit = ""
            value_to_edit = value_to_edit.join(values['todos'])
            for item in todos:
                if item == value_to_edit:
                    index_of_todo = todos.index(item)
                    todos[index_of_todo] = values['todo'] + "\n"
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
        case "Completed":
            todos = functions.get_todos()
            value_to_remove = ""
            value_to_remove = value_to_remove.join(values['todos'])
            for item in todos:
                if item == value_to_remove:
                    index_of_todo = todos.index(item)
                    print(index_of_todo)
                    todos.pop(index_of_todo)
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
window.close()