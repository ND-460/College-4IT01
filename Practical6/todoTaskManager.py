taskNo = 0
listOfTasks=[]
def addTask(l,no,name):
    l.append(dict(taskNo=no,taskName=name))
def deleteTask(l,no):
    for i in l:
        if i["taskNo"] == no:
            l.remove(i)
            break
def viewTasks(l):
    for i in l:
        print(i)
choice = 'start'
print("Press\n1 for Adding task\n2 for Deleting task\n3 for Viewing task\nAny other for exit")
while(choice == 'start'):
    c = int(input("Enter the choice: "))
    match c:
        case 1:
            print("Adding the task")
            name = input("Enter the task name")
            taskNo +=1
            addTask(listOfTasks,taskNo, name)

        case 2:
            print("Deleting the task")
            no = int(input("Enter the number of task to delete"))
            deleteTask(listOfTasks,no)

        case 3:
            print("Viewing the tasks")
            viewTasks(listOfTasks)

        case _:
            choice = 'end'