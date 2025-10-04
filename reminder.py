from datetime import datetime
import time
import uuid
from colorama import Fore,Style
from firebase import db 



class Reminder:
    

    def __init__(self):
        pass
        self.docs = db.collection("task")
        

    def create_task(self,task: str, due: str, done: bool = False, category: str = "None"):
        id= str(uuid.uuid4())
        doc_ref = self.docs.document(id)

        date_obj = datetime.strptime(due, "%Y-%m-%d %H:%M")
        doc_ref.set({"Name": task, "done": False, "date": datetime.now(),"due":due})
        
 
    def read_tasks(self,task_name=""):


        tasks=self.docs.stream()
        #gets the task and the due date 
        task_info={}
        for task in tasks:

            task_info[task.to_dict()["Name"]]=task.to_dict()["due"]

        if task_name !="":

            print("task:", task_info[task_name])
        else:
            for x in task_info:

                print(f"{Fore.CYAN}📝 Task:{Style.RESET_ALL} {Fore.WHITE}{x}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Due:{Style.RESET_ALL} {task_info[x]}")
                # print(f"{Fore.GREEN if task_info['done'] else Fore.RED}Status:{Style.RESET_ALL} {'✅ Done' if task_info['done'] else '❌ Not done'}")

            


    def comp_task(self,task:str):

        pass
       







