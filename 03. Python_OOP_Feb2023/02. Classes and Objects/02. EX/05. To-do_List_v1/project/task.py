class Task:

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if self.name == new_name:
            return f"Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return f"Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        try:
            self.comments[comment_number] = new_comment
            return f"{', '.join(self.comments)}"
        except IndexError:
            return f"Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


# #######################################################################
# Test_Code_1:
# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
# --------------------------------------------
# Output_1:
# Go to University
# 28.05.2020
# Don't forget laptop and notebook
# Name: Go to University - Due Date: 28.05.2020
# Task Name: Go to University - Due Date: 28.05.2020 is added to the section
# Cleared 0 tasks.
# Section Daily tasks:
# Name: Go to University - Due Date: 28.05.2020
# Name: Make bed - Due Date: 27/05/2020
# #######################################################################