class Entry(object):
    """
    Attributes of new instance of the Entry class:

    task_name (str): Task name of work
    time_spent (int): minutes spent on task
    notes (str): supporting information about task
    time (datetime): current time
    date_added (str): datetime formatted as Month/Day/Year
    """
    def __init__(self, **kwargs):
        super(Entry, self, **kwargs).__init__()
        self.task_name = kwargs.get('task_name')
        self.time_spent = kwargs.get('time_spent')
        self.notes = kwargs.get('notes')
        self.date_added = kwargs.get('date_added')


    def __str__(self):
        return """
            Task Name: {}
            Date Recorded: {}
            Time Spent: {} minutes
            Notes: {}
        """.format(self.task_name,
                   self.date_added,
                   self.time_spent,
                   self.notes
            )
