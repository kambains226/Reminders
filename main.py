
import time

from firebase import db 

import argparse

from reminder import Reminder


if __name__== "__main__":
    
    
    
    task = Reminder()


    parser = argparse.ArgumentParser(description="Task CLI")
    parser.add_argument("command", help="Command to run (list, create, delete, complete, clear)")
    parser.add_argument("arg", nargs="?", help="Task Name")

    args = parser.parse_args()

    if args.command == "list":
        task.read_tasks()
    elif args.command == "create":
        task.create_task(args.arg)
    elif args.command == "delete":
        task.read_tasks(args.arg, mode="delete")
    elif args.command == "complete":
        task.read_tasks(args.arg, mode="comp")
    elif args.command == "clear":
        task.clear()
    else:
        print("Unknown command. Use --help for usage.")






