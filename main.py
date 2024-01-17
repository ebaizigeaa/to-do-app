from functions import readtodos, writetodos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is: {now}")
while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit' : ")
    user_action = user_action.strip() # remove any white space that the user might include.

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        todo = todo.capitalize()
        todos = readtodos()
        todos.append(todo)
        writetodos(todos)
    elif user_action.startswith("show"):
        todos = readtodos()
        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index + 1} - {todo}")
    elif user_action.startswith("edit"):
        try:
            todos = readtodos()
            number = user_action[5: ]
            number = int(number)
            new_todo = input("Enter the new todo: ") + '\n'
            todos[number - 1] = new_todo
            writetodos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        todos = readtodos()
        number = user_action[9:]
        number = int(number)
        todos.remove(todos[number - 1])
        writetodos(todos)
    elif user_action.startswith("exit"):
        break
    else:
        print("You entered a wrong choice")

print("Bye!")
