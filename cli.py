from modules import functions
import time

print(time.strftime("%d - %b - %Y"))
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        if len(todos) != 0:
            todos.append('\n' + todo)
        else:
            todos.append(todo)
        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        number = int(input("Number of the todo to edit: "))
        number = number - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("complete"):
        number = int(input("Number of the todo to complete: "))
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
        with open("todos.txt", 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list"

    else:
        break

import time
