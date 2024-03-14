"""
The Section class should receive a username (string) upon initialization. The task also has one instance attribute: tasks (empty list)
The Section class should also have four methods:
-	add_task(new_task: Task)
o	Adds a new task to the collection and returns "Task {task details} is added to the section"
o	If the task is already in the collection, return "Task is already in the section {section_name}"
-	complete_task(task_name: str)
o	Changes the task to completed (True) and returns "Completed task {task_name}"
o	If the task is not found, returns "Could not find task with the username {task_name}"
-	clean_section()
o	Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
-	view_section()
o	Returns information about the section and its tasks in this format:
    "Section {section_name}:
     {details of the first task}
     {details of the second task}
     …
     {details of the n task}"
"""
from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            curr_task = next(filter(lambda ct: ct.username == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the username {task_name}"

        curr_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        count = 0
        for curr_task in self.tasks:
            if curr_task.completed:
                count += 1
                self.tasks.remove(curr_task)

        return f"Cleared {count} tasks."


    def view_section(self):
        tasks_details = '\n'.join([t.details() for t in self.tasks])
        return f"Section {self.name}:\n{tasks_details}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
