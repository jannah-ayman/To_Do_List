def load():
    taskList=[]
    try:
        with open("tasks.txt", "r") as taskFile:
            for line in taskFile:
                task,completed=line.strip().split("|")
                taskList.append({"task":task,"completed":completed})
    except FileNotFoundError:
        print("file is not found")
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
    pass

#########################################

def markAsComplete(tasks):
    task=input("\tChoose the task number you want to mark as completed: ")
    

#########################################

def saveTasks(tasks):
    try:
        with open("tasks.txt", "w") as taskFile:
            for task in tasks:
                taskFile.write(f'{task["task"]}|{"yes" if task["completed"]=="yes" else "no"}')
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
            deleteTask()

        elif(choice=="4"):
            markAsComplete()

        elif(choice=="5"):
            saveTasks()
            break
        else:
            print("\n\tInvalid choice!")
            
        
if __name__=="__main__":
    print("\n\tWelcome to your to-do list! ✨")
    main()