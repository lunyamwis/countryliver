class TaskManager:
    """
    this task manager helps in allocating tasks for different users in the 
    system based on priority of the tasks and skill level of the workers.
    """
    def __init__(self,due_date_time,area,task,
                completed_date_time,person_assigned):
        self.due_date_time = due_date_time
        self.area = area
        self.task = task
        self.completed_date_time = completed_date_time
        self.person_assigned = person_assigned


"""
below is the test procedure of 
the taskmanager class
"""
if __name__=='__main__':
    task_1 = TaskManager('2021-10-11','A1','clearing of the land',
                        '2021-11-11','Martin')
    print(task_1.task)