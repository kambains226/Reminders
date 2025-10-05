
import time

from firebase import db 

import argparse

from reminder import Reminder


if __name__== "__main__":
    
    
    
    task = Reminder()


    parser = argparse.ArgumentParser(description="Task CLI")
    parser.add_argument("command", help="Command to run (list, create, delete, complete, clear)")
    parser.add_argument("arg", nargs="*", help="Task Name")
    args = parser.parse_args()

    if args.command == "list":
        if args.arg:


            task_name = " ".join(args.arg)if args.arg else None
            if(task_name):
                task.read_tasks(task_name)
            else:

                task.read_tasks()

    elif args.command == "create":
        task_name = " ".join(args.arg) if args.arg else None
        if task_name:
            task.create_task(task_name)
        else:
            print("Please provide a task name.")
            
    elif args.command == "delete":
        task_id = " ".join(args.arg)
        task.read_tasks(task_id, mode="delete")

    elif args.command == "complete":
        task_id = " ".join(args.arg)
        task.read_tasks(task_id, mode="comp")

    elif args.command == "clear":
        task.clear()

    else:
        print("Unknown command. Use --help for usage.")




