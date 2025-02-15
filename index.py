def load():
    taskList=[]
    try:
        with open("tasks.txt", "r") as taskFile:
            for line in taskFile:
                task,completed=line.strip().split("|")
                taskList.append({"task":task,"completed":completed})
    except FileNotFoundError:
        print("\tFile not found. Creating a new 'tasks.txt' file. . .")
        with open("tasks.txt", "w") as taskFile:
            pass 
    return taskList

#########################################

def showTasks(tasks):
    if tasks:
        for i, task in enumerate(tasks,1):
            print(f"\t{i}. {task["task"]}: {'Completed' if task["completed"]=="yes" else 'Not Completed'} ")
    else:
        print("\tThere are no tasks!")

#########################################

def addTask(tasks):
    task=input("\tEnter the new task: ")
    task={"task":task,"completed":"no"}
    tasks.append(task)
    saveTasks(tasks)
    print("\tTask added succesfully!")

#########################################

def deleteTask(tasks):
    showTasks(tasks)
    if tasks:
        try:
            taskNum=int(input("\tChoose the task number you want to delete: "))
            if 1 <= taskNum <= len(tasks):
                deletedTask=tasks.pop(taskNum-1)
                saveTasks(tasks)
                print("\tTask deleted succesfully!")
            else:
                print("\tThis task number doesn't exist!")
        except ValueError:
            print("\tEnter a numerical value!")
    else:
        print("\tThere are no tasks to delete!")

#########################################

def markAsComplete(tasks):
    showTasks(tasks)
    if tasks:
        try:
            taskNum=int(input("\tChoose the task number you want to mark as completed: "))
            if 1 <= taskNum <= len(tasks):
                tasks[taskNum-1]["completed"]="yes"
                saveTasks(tasks)
                print("\tTask marked as completed succesfully!")
            else:
                print("\tThis task number doesn't exist!")
        except ValueError:
            print("\tEnter a numerical value!")
    else:
        print("\tThere are no tasks to mark as complete!")

#########################################

def saveTasks(tasks):
    try:
        with open("tasks.txt", "w") as taskFile:
            for task in tasks:
                taskFile.write(f'{task["task"]}|{"yes" if task["completed"]=="yes" else "no"}\n')
    except FileNotFoundError:
        print("file is not found")

#########################################

def main():
    while True:
        tasks=load()

        print("\n\t1. Show Tasks\n\t2. Add a task\n\t3. Delete a task\n\t4. Mark a task as completed\n\t5. Save and exit")
        choice=input("\n\tWhat's your choice? ")

        if(choice=="1"):
            showTasks(tasks)

        elif(choice=="2"):
            addTask(tasks)

        elif(choice=="3"):
            deleteTask(tasks)

        elif(choice=="4"):
            markAsComplete(tasks)

        elif(choice=="5"):
            print("\tGoodbye!")
            break
        else:
            print("\n\tInvalid choice!")
            
        
if __name__=="__main__":
    print("\n\tWelcome to your to-do list! ✨")
    main()