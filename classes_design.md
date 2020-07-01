```python
class AttendanceSystem:
    def __init__(self, path_to_employee_file, path_to_attendance_log):
        self.clock = Clock(path_to_employee_file, path_to_attendance_log)
        self.report = Report(path_to_employee_file, path_to_attendance_log)

    def start(self):
        # TODO: show interface and do actions                
        pass
```
```python
class Clock:
    def __init__(self, path_to_employee_file, path_to_attendance_log):
        pass

    def clock_in(self, employee_id):
        assert employee_id in self.employee_file
        pass

    def clock_out(self, employee_id):
        pass

    def is_valid_employee(self, employee_id):
        pass
```
```python
class Report:
    def __init__(self, path_to_employee_file, path_to_attendance_log):
        pass

    def add_employee(self, name, employee_id):
        pass

    def  create_report_X(self, ...):
```