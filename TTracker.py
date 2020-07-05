"""
This reads a "task.txt" file and creates (or appends) Tasks_yyyy_mm_dd.csv file.
It scans tasks.txt and lists the task with numbers to choose from. 
As soon as user chooses the task, counter for that gets started. Then user chooses too witch task by pressing s and hits enter.

At that point it logs a row (with three columns) to csv file as:
Task: Start Time: End Time
"""
import os.path
import datetime

tFileP = "tasks.txt"
while True:
    if not os.path.isfile(tFileP):
        print("File ", tFileP, " does not exist")
        break
    with open(tFileP) as f:
        tasks = f.readlines()
    tasks = [t.strip() for t in tasks if len(t.strip()) > 0]
    print("Choose your tasks: ")
    for i in range(len(tasks)):
        print(i, tasks[i])
    t = input()
    if not t.isnumeric():
        print("Please enter only number")
        continue
    t = int(t)
    if t >= len(tasks):
        print("Task number > task in tasks.txt. Only enter from 0 to",len(tasks))
        continue
    s_time = datetime.datetime.now()
    print("Started task: ",tasks[t]," at: ",s_time, "\n Press Enter to end task")
    e = input()
    e_time = datetime.datetime.now()
    print("Ended Task: ", tasks[t], " ended.\n Enter any comments associated with the task, and press enter")
    c = input()
    print("Logging entry. Task: ",tasks[t])
    print("S_time: ",s_time.time())
    print("E_time: ",e_time.time())
    print("Comment: ",c)
    csvFile = "{}".format(s_time.date())
    csvFile += ".csv"
    with open(csvFile, "a") as f:
        f.write("\n{t},{s_t},{e_t},{c}".format(t=tasks[t], s_t=s_time.time(), e_t=e_time.time(), c=c))