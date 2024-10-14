from project.section import Section
from project.task import Task

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, '****'))
task.add_comment('TOO')
print(task.edit_comment(1, 'asdasd'))
print(task.details())

selection = Section("Today's tasks")
print(selection.add_task(task))
print(selection.add_task(task))

