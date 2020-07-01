import pandas as pd
import numpy as np
from _datetime import datetime


class AttendanceSystem:
    def __init__(self, path_to_internal_employees_file, path_to_attendance_log):
        self.clock = Clock(path_to_internal_employees_file, path_to_attendance_log)
        # add method - read csv, write csv
        self.report = Report(path_to_internal_employees_file, path_to_attendance_log)

# class Helper
    # add method - read csv, write csv
    #


    def start(self, user_id):
        # CHECK if user_id is None
        # start menu, being called after validation
        proceed = True
        while proceed:
            option = int(
                input("Enter the number of action you wish to do:\n1) Add employee manually\n2) Delete employee "
                      "manually\n3) Add employees from file\n4) Delete employees from file\n5) Mark attendance\n6) Generate "
                      "attnedance report for an employee\n7) Print monthly report for all employees\n8) Print report for "
                      "all late employees\nYour choice: "))
            # method that takes a dict (keys:options,val:methods)
            # 25-27 : method
            if option == 1:
                self.report.add_employee()
                answer = input("Would you like to go back to the menu?\nyes/no\nYour answer: ")
                if answer != 'yes':
                    proceed = False
            if option == 2:
                self.report.delete_employee()
                answer = input("Would you like to go back to the menu?\nyes/no\nYour answer: ")
                if answer != 'yes':
                    proceed = False
            if option == 3:
                self.report.add_employees_from_external_file()
                answer = input("Would you like to go back to the menu?\nyes/no\nYour answer: ")
                if answer != 'yes':
                    proceed = False
            if option == 4:
                self.report.delete_employees_from_external_file()
                answer = input("Would you like to go back to the menu?\nyes/no\nYour answer: ")
                if answer != 'yes':
                    proceed = False
            if option == 5:
                clock_option = int(
                    input("Enter the number of action you wish to do:\n1) Clock in\n2) Clock out\nYour answer: "))
                if clock_option == 1:
                    datetime = self.clock.get_date()
                    attendance_log_df = pd.read_csv(self.clock.path_to_attendance_log, dtype=str)
                    data = [{'employee_id': user_id, 'date_time_in': datetime}]
                    dict_df = pd.DataFrame.from_dict(data)
                    updated_attendance_log_df = attendance_log_df.append(dict_df, sort=False)
                    print(updated_attendance_log_df)
                    updated_attendance_log_df.to_csv(self.clock.path_to_attendance_log, mode='w', index=False)
                    answer = input("Would you like to go back to the menu?\nyes/no\nYour answer: ")
                    if answer != 'yes':
                        proceed = False
                if clock_option == 2:
                    # column- datetime, column= in\out
                    datetime = self.clock.get_date()
                    attendance_log_df = pd.read_csv(self.clock.path_to_attendance_log, dtype=str)
                    data = [{'date_time_out': datetime}]
                    dict_df = pd.DataFrame.from_dict(data)
                    updated_attendance_log_df = attendance_log_df.append(dict_df, sort=False)
                    print(updated_attendance_log_df)
                    updated_attendance_log_df.to_csv(self.clock.path_to_attendance_log, mode='w', index=False)
                    answer = input("Would you like to go back to the menu?\nyes/no\nYour answer: ")
                    if answer != 'yes':
                        proceed = False

    def is_valid(self):
        restart = True
        user_id = None
        # validating that the user is one of the employees of the company
        while restart:
            internal_employees_file_df = pd.read_csv(self.report.path_to_internal_employees_file, dtype=str)
            print(internal_employees_file_df)
            print("Welcome to Employee Attendance Management System.")
            user_id = str(input("Please enter your ID: "))
            user_name = str(input("Please enter your full name: "))
            # TODO: check validity
            input_df = pd.DataFrame(data=[[user_id, user_name]], columns=["user_id", "user_name"])
            is_id_valid = internal_employees_file_df['employee_id'].isin(input_df['user_id'])
            is_name_valid = internal_employees_file_df['employee_name'].isin(input_df['user_name'])
            if is_id_valid.any() and is_name_valid.any():
                restart = False
                print("you are valid")
            else:
                print("try again")
        if not restart:
            self.start(user_id)


class Clock:
    def __init__(self, path_to_internal_employees_file, path_to_attendance_log):
        self.path_to_internal_employees_file = path_to_internal_employees_file
        self.path_to_attendance_log = path_to_attendance_log

    def get_date(self):
        return datetime.now().isoformat(' ', 'seconds')


class Report:
    def __init__(self, path_to_internal_employees_file, path_to_attendance_log):
        self.path_to_internal_employees_file = path_to_internal_employees_file
        self.path_to_attendance_log = path_to_attendance_log

    def add_employee(self):
        # put in a dict
        new_employee_id = str(input("Please enter employee's ID: "))
        new_employee_name = str(input("Please enter employee's full name: "))
        new_employee_phone = str(input("Please enter employee's phone: "))
        new_employee_age = str(input("Please enter employee's age: "))
        input_df = pd.DataFrame(data=[[new_employee_id, new_employee_name, new_employee_phone, new_employee_age]],
                                columns=["employee_id", "employee_name", "employee_phone", "employee_age"])
        input_df.to_csv(self.path_to_internal_employees_file, mode='a', header=False, index=False)

    def delete_employee(self):
        deleted_employee_id = str(input("Please enter employee's ID: "))
        internal_employees_file_df = pd.read_csv(self.path_to_internal_employees_file, dtype=str)
        internal_employees_file_df.drop(
            internal_employees_file_df.loc[internal_employees_file_df['employee_id'] == deleted_employee_id].index,
            inplace=True)
        print("The new employees file after deleting:\n")
        print(internal_employees_file_df)
        internal_employees_file_df.to_csv(self.path_to_internal_employees_file, mode='w', index=False)

    def add_employees_from_external_file(self):
        external_file_path = str(input("Please enter file path: "))
        external_employees_file = pd.read_csv(external_file_path, dtype=str)
        external_employees_file.to_csv(self.path_to_internal_employees_file, mode='a', header=False, index=False)

    def delete_employees_from_external_file(self):
        external_file_path = str(input("Please enter file path: "))
        external_employees_to_delete_df = pd.read_csv(external_file_path, dtype=str)
        print(external_employees_to_delete_df)
        internal_employees_file_df = pd.read_csv(self.path_to_internal_employees_file, dtype=str)
        condition = internal_employees_file_df['employee_id'].isin(external_employees_to_delete_df['employee_id'])
        internal_employees_file_df.drop(internal_employees_file_df[condition].index, inplace=True)
        print("The new employees file after deleting:\n")
        print(internal_employees_file_df)
        internal_employees_file_df.to_csv(self.path_to_internal_employees_file, mode='w', index=False)

    def create_report_X(self):
        pass
        # sort by id,name - depends on the type of report
