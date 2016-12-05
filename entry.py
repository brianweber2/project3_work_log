import datetime


class Entry(object):
    """docstring for Entry"""
    def __init__(self, task_name, time_spent, notes):
        super(Entry, self).__init__()
        self.task_name = task_name
        self.time_spent = time_spent
        self.notes = notes
        self.time = datetime.datetime.now()
        self.date_added = self.time.strftime("%m/%d/%Y")


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
