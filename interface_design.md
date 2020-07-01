### Interface Design - before GUI from TKInter
#### Log in to the system

```python
Id:
Name:
```
#### Options menu
```python
1) Add employee manually
2) Delete employee manually
3) Add employee from file
4) Delete employee from file
5) Mark attendance
6) Generate attnedance report for an employee
7) Print monthly report for all employees
8) Print report for all late employees
```
If the user chooses option (1) or (2):
```python
Please enter the employee's details:
Id:
Name:
Phone:
Age:
```
If the user chooses option (3) or (4):
```python
Please enter the file path:
```
If the user chooses option (5):
```python
What would you like to do?
1) Clock in
2) Clock out
```
If the user chooses option (6):
```python
Please enter the employee's ID:
```
```python
Report for employee 305785400:
```
  Date   | Time in | Time out |
 ------ | ------- | -------- |
 03/04/20     | 9:00  | 18:00
  04/04/20    | 9:30  | 19:00
  05/04/20    | 8:30  | 17:30
  06/04/20 | 8:00 | 18:00
  07/04/20 | 8:30| 18:30

If the user chooses option (7):
```python
Please enter the month: 
Please enter the year:
```
```python
Report for January 2020: 
```
|    ID  |  Day   | Time in | Time out |
| ------- | ------ | ------- | -------- |
| 305785400  | 1     | 9:00  | 18:00
| 305785400 | 2    | 9:30  | 19:00
| 305785400    | 3    | 8:30  | 17:30
| 055346787 | 1 | 8:00 | 18:00
|055346787 | 2 | 8:30| 18:30
|055346787 |3 | 10:00|19:30

If the user chooses option (8):

|    ID  |  Day   | Time in | Time out |
| ------- | ------ | ------- | -------- |
| 305785400  | 1     | 9:39  | 18:00
| 305785400 | 2    | 9:46| 19:00
| 305785400    | 3    | 10:09  | 17:30
| 055346787 | 1 | 09:55 | 18:00
|055346787 | 2 | 11:23| 18:30
|055346787 |3 | 10:00|19:30