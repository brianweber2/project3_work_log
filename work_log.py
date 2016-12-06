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
        task_name = input("Enter a task name: ")
        while True:
            try:
                time_spent = int(
                    input("Enter number of minutes spent working on it: ")
                )
                break
            except ValueError:
                print("\nNot a valid time entry. Please enter time as a whole"
                "integer, i.e. 45\n")
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
        while True:
            clear_screen()
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
                self.find_by_date()
            elif user_input.lower() == 't':
                pass
            elif user_input.lower() == 'k':
                self.search_keyword()
            elif user_input.lower() == 'p':
                pass
            else:
                clear_screen()
                print("{} is not a valid command! Please try again.\n"
                    "".format(user_input))


    def search_keyword(self):
        """
        Search for a keyword (str) that is in either the task name or notes.
        """
        pass


    def remove_duplicates(self, dates):
        """Remove duplicate dates from a list."""
        unique_dates = []
        for date in dates:
            if date in unique_dates:
                continue
            else:
                unique_dates.append(date)
        return unique_dates


    def read_csv_file(self, filename):
        """Read a CSV file and return all data in a list."""
        import csv
        data = []
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=',', lineterminator='\n')
            rows = list(reader)
            for row in rows:
                data.append(row)
        return data


    def find_by_date(self):
        """Find all entries by date."""
        clear_screen()
        print("FIND BY DATE")
        print('\n' + '=' * 40 + '\n')
        dates = []
        # Find all unique dates and display to user
        with open(filename, 'r') as csvfile:
            datereader = csv.reader(csvfile, delimiter=',',
                lineterminator='\n')
            rows = list(datereader)
            for row in rows:
                dates.append(row[-1])
        dates = self.remove_duplicates(dates)
        print("Here are the dates we have entries for: \n")
        for date in dates:
            print(date)
        ### Validate date input ###
        user_input = self.validate_date(dates)
        ### Find all and display all entires with the date provided by user ###
        data = self.read_csv_file(filename)
        entires = []
        for line in data:
            if user_input in line:
                entires.append(line)
        clear_screen()
        print("Date: {}".format(user_input))
        print('\n' + '=' * 40 + '\n')
        for entry in entires:
            print("Task Name: {}\nTime Spent: {} minutes\nNotes: {}\n"
                "Date: {}".format(entry[0], entry[1], entry[2], entry[3]))
            input("\nPress ENTER for next entry...")
            clear_screen()
            print("Date: {}".format(user_input))
            print('\n' + '=' * 40 + '\n')
        clear_screen()
        response = input("Do you want to search something else? Y/[n] ")
        if response.lower() != 'y':
            self.menu()
        else:
            self.search_entries()


    def validate_date(self, dates):
        """Validate date input."""
        # Check that the string can be converted to an integer
        while True:
            user_input = input("\nWhich date would you like to view? ")
            numbers = user_input.split('/')
            if not self.convert_to_int(numbers):
                print("\n{} is not a valid date entry. Please enter"
                " in the format of mm/dd/yyyy. Only numbers!"
                "".format(user_input))
            # Check that the input is the correct length
            elif not self.check_date_length(numbers):
                print("\n{} is not a valid date entry. Please enter in the"
                        " format of mm/dd/yyyy.".format(user_input))
            elif user_input not in dates: # Check if date is in database
                print("\n{} is not in the work log. Please enter from the "
                    "following dates: ".format(user_input) + ", ".join(dates))
            else:
                break
        return user_input


    def convert_to_int(self, numbers):
        """Convert a list of strings to integers."""
        try:
            for number in numbers:
                int(number)
            return True
        except ValueError:
            return False


    def check_date_length(self, numbers):
        """Checks the date's length to be mm/dd/yyyy."""
        if (len(numbers[0]) == 2 and len(numbers[1]) == 2
            and len(numbers[2]) == 4):
            return True
        else:
            return False


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
