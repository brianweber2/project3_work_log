"""
Author: Brian Weber
Date Created: December 5, 2016
Revision: 1.0
Title: Work Log
Description: In order to prepare better timesheets for your company, you've
been asked to develop a terminal application for logging what work someone did
on a certain day. The script should ask for a task name, how much time was
spent on the task, and any general notes about the task. Record each of these
items into a row of a CSV file along with a date.

Provide a way for a user to find all of the tasks that were done on a certain
date or that match a search string (either as a regular expression or a plain
text search). Print a report of this information to the screen, including the
date, title of task, time spent, and general notes.
"""
import re
import csv
import os
import sys
import datetime

from entry import Entry


# CSV file name
filename = "worklog.csv"


def clear_screen():
    """Clear screen by sending command to OS."""
    os.system('cls' if os.name == 'nt' else 'clear')


class WorkLog(object):
    """All methods for the WorkLog"""

    def prompt_for_entry(self):
        """Add a new work log entry."""
        clear_screen()
        entry_dict = {}
        task_name = input("Enter a task name: ")
        try:
            time_spent = int(
                input("Enter number of minutes spent working on it: ")
            )
        except ValueError:
            print("\nNot a valid time entry. Please enter time as a whole"
            "integer, i.e. 45")
            time_spent = int(
                input("\nEnter number of minutes spent working on it: ")
            )
        notes = input("Any additional notes? ")
        date_added = (datetime.datetime.now()).strftime("%m/%d/%Y")
        self.add_entry_to_file(task_name, time_spent, notes, date_added)
        clear_screen()
        print("Entry added!\n")


    def add_entry_to_file(self, task_name, time_spent, notes, date_added):
        """Add entry to CSV file."""
        with open(filename, 'a') as csvfile:
            entrywriter = csv.writer(csvfile, delimiter=',',
                lineterminator='\n')
            entrywriter.writerow([task_name, time_spent, notes, date_added])


    def search_entries(self):
        """Lookup previous entries."""
        clear_screen()
        while True:
            user_input = input("Choose from the following search options:\n\n"
                "[D]ate\n"
                "[T]ime spent\n"
                "[K]eyword\n"
                "[P]attern\n"
                "[Q]uit and return to the main menu\n\n"
                )
            if user_input.lower() == 'q':
                self.menu()
            elif user_input.lower() == 'd':
                pass
            elif user_input.lower() == 't':
                pass
            elif user_input.lower() == 'k':
                pass
            elif user_input.lower() == 'p':
                pass
            else:
                clear_screen()
                print("{} is not a valid command! Please try again.\n"
                    "".format(user_input))


    def find_by_date(self):
        """Find all entries by date."""
        pass


    def menu(self):
        """Present menu to user."""
        clear_screen()
        print("Welcome to Work Log 3.0!\n")
        while True:
            user_input = input(
                "Please choose from the following options:\n\n"
                "[A]dd new work entry\n"
                "[S]earch work entries\n"
                "[Q]uit Work Log 3.0\n\n"
            )
            if user_input.lower() == 'q':
                print("Thanks for using Work Log 3.0!")
                sys.exit()
            elif user_input.lower() == 'a':
                self.prompt_for_entry()
            elif user_input.lower() == 's':
                self.search_entries()
            else:
                clear_screen()
                print("{} is not a valid command! Please try again.\n"
                    "".format(user_input))


    def __init__(self):
        super(WorkLog, self).__init__()
        self.menu()



WorkLog()
