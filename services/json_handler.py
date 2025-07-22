import json
import os
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.file_path = 'data/tasks.json'
        self.ensure_file_exists()

    def ensure_file_exists(self):
        # I want to ensure that the file exists before we create it
        if not os.path.exists(self.file_path):
            os.makedirs('data')

        if not os.path.isfile(self.file_path):
            initial_data= {
                "daily_tasks":[],
            }    
            self.save_data(initial_data)
       
    def load_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_task(self, task_text, task_type = "daily"):

        data= self.load_data()

        # need to generrate a new id for the task that will be added
        new_id = len(data["daily_tasks"]) + 1 

        new_task = {
            "id": new_id,
            "text": task_text,
            "created_at": datetime.now().isoformat(),
            "completed": False
        }

        # now append it to the array of tasks
        data["daily_tasks"].append(new_task)

        self.save_data(data)
        return new_task
    def get_tasks(self, task_type="daily"):
        data = self.load_data()
        return data[f'{task_type}_tasks'] 
    
    def delete_task(self, task_id, task_type="daily"):
        data = self.load_data()
        tasks = data[f'{task_type}_tasks']
        
        # Find the task with the given ID
        task_to_delete = next((task for task in tasks if task['id'] == task_id), None)
        
        if task_to_delete:
            tasks.remove(task_to_delete)
            self.save_data(data)
            return True
        return False
    def complete_task(self, task_id, task_type="daily"):
        data = self.load_data()
        tasks = data[f'{task_type}_tasks']

        task_to_complete = next((task for task in tasks if task['id'] == task_id), None)
        if task_to_complete:
            task_to_complete['completed'] = True
            self.save_data(data)
            return task_to_complete
        return None




