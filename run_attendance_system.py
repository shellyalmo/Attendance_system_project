from attendance_system import AttendanceSystem

my_attendance_system = AttendanceSystem(
    r"C:\Users\Shelly\PycharmProjects\Attendance_log_project\project_code\Internal_Employees_file.csv",
    r"C:\Users\Shelly\PycharmProjects\Attendance_log_project\project_code\Attendance_log.csv")

my_attendance_system.is_valid()

# my_attendance_system.create_report()
