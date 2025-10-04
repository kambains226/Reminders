from datetime import datetime
import time
import uuid
from colorama import Fore,Style
from firebase import db 
from tabulate import tabulate 



class Reminder:
    

    def __init__(self):
        self.docs = db.collection("task")
        

    def get_hour_mins(self,date:str):
        now = datetime.now()

        # diff=   datetime.strptime(task.to_dict()["due"],"%Y-%m-%d %H:%M")-now
        diff=   datetime.strptime(date,"%Y-%m-%d %H:%M")-now
        total_seconds = diff.total_seconds()
        hours= int(total_seconds //3600)
        mins =  int(total_seconds %3600)//60

        if hours >24:
            print(f"{Fore.YELLOW}Due:{Style.RESET_ALL} {date}")
        elif hours ==0: 
            print(f"{Fore.YELLOW}Due:{Style.RESET_ALL}  {mins} minutes ")

        else:
            print(f"{Fore.YELLOW}Due:{Style.RESET_ALL} {hours} hours and  {mins} minutes ")
        # return[hours,mins]



    def create_task(self,task: str,  done: bool = False, category: str = "None"):
        due = input(f"When is ${task} due e.g.(2025-10-04 14:30):\n" )
        id= str(uuid.uuid4())
        doc_ref = self.docs.document(id)

        date_obj = datetime.strptime(due, "%Y-%m-%d %H:%M")
        doc_ref.set({"Name": task, "done": False, "date": datetime.now(),"due":due})
        
 
    def read_tasks(self,task_name="",mode=""):


        tasks=self.docs.stream()
        #gets the task and the due date 
        task_info={}
        complete ={}
        for task in tasks:
            task_info[task.to_dict()["Name"]]=task.to_dict()["due"]
            complete[task.to_dict()["Name"]]=task.to_dict()["done"]

            # if task_name =="clear":
                    # self.docs.document(task.id).delte()
                    # return 

        if task_name !="":


            if task_info[task_name] and mode ==""  :



                print(f"{Fore.CYAN}📝 Task:{Style.RESET_ALL} {Fore.WHITE}{task_name}{Style.RESET_ALL}")
                self.get_hour_mins(task_info[task_name])
                # print(f"{Fore.YELLOW}Due:{Style.RESET_ALL} {task_info[task_name]}")
                print(f"{Fore.CYAN}📝 Complete:{Style.RESET_ALL} {Fore.WHITE}{complete[task_name]}{Style.RESET_ALL}")
                self.get_hour_mins(task.to_dict()["due"])
            if mode =="delete":
                self.docs.document(task.id).delete()
                print("task completed ")
            if mode =="comp":
                self.comp_task(self.docs.document(task.id))
       
        else:

            for x in task_info:

                print(f"{Fore.CYAN}📝 Task:{Style.RESET_ALL} {Fore.WHITE}{x}{Style.RESET_ALL}")
                self.get_hour_mins(task_info[x])
                print(f"{Fore.CYAN}📝 Complete:{Style.RESET_ALL} {Fore.WHITE}{complete[x]}{Style.RESET_ALL}")

            

    def clear(self):
        # get the id 
        tasks= self.docs.list_documents()

        for task in tasks:
            task.delete()

        print("tasks have been cleared ")


        self.docs
    def comp_task(self,ref):
        ref.update({"done":True})

    # def sk(self,ref):
        # ref.update({})


       




        
       







