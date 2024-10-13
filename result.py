# Hi,
#
# Here is the results of Matriculation of each year.
#
# Your job is to find total marks of each student and then show the results of each year
#      1. Topper of  each year
#      2. Total Marks of each student
#      3.  If any student is failed in any subject, his/her total marks should not be shown.  Subjects name shown in which he has suply
#
#
# Sample Output:
#
# 2007:
#     1st Position:   Student-Name  ( 700/800)
#     2nd Position:   Student-Name  ( 700/800)
#     3rd Position:   Student-Name  ( 700/800)
#     Others:
#      Student-Name:   obtained_marks / full_marks
#
#
#
# 2008:
#     1st Position:   Student-Name  ( 700/800)
#     2nd Position:   Student-Name  ( 700/800)
#     3rd Position:   Student-Name  ( 700/800)
#     Others:
#      Student-Name:   obtained_marks / full_marks
import csv
import datetime
import random
def add_exp(description,amount):
    with open('expenses.csv','r') as f:
        if f.read() == '':
            with open('expenses.csv',mode='w',newline='') as c:
                fieldnames = ['ID', 'Date', 'Description','Amount']
                writer = csv.DictWriter(c, fieldnames=fieldnames)
                writer.writeheader()
                id = int(random.random()*12424)
                writer.writerow({'ID': id, 'Date': datetime.date.today(), 'Description': description,'Amount':amount})
                print(f"Expense added successfully (ID: {id})")
        else:
            with open('expenses.csv', mode='a',newline='') as csv_file:
                fieldnames = ['ID', 'Date', 'Description','Amount']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                id = int(random.random()*12424)
                writer.writerow({'ID': id, 'Date': datetime.date.today(), 'Description': description,'Amount':amount})
                print(f"Expense added successfully (ID: {id})")
# Users can update an expense.
def update_exp(id,description,amount):
    rows = []
    found = False
    with open('expenses.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        header = next(csv_reader)
        rows.append(header)
        for row in csv_reader:
            if int(row[0]) == int(id):
                found = True
                updated_row = [id,row[1],description,amount]
                # updated_row = 
                rows.append(updated_row)
            else:
                rows.append(row)

    if not found:
        print("Expense doesn't exist!")
    else:
        with open('expenses.csv', 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(rows)
            print("Expense updated successfully!")


# Users can delete an expense.
def delete_exp(id):
    rows = []
    found = False
    with open('expenses.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        header = next(csv_reader)
        rows.append(header)
        for row in csv_reader:
            if int(row[0]) == int(id):
                found = True
            else:
                rows.append(row)

    if not found:
        print("Expense doesn't exist!")
    else:
        with open('expenses.csv', 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(rows)
            print("Expense deleted successfully!")


# Users can view all expenses.
# $ expense-tracker list
# # ID  Date       Description  Amount
# # 1   2024-08-06  Lunch        $20
# # 2   2024-08-06  Dinner       $10
#      1. Topper of  each year
# 2007:
#     1st Position:   Student-Name  ( 700/800)
#     2nd Position:   Student-Name  ( 700/800)
#     3rd Position:   Student-Name  ( 700/800)
#     Others:
#      Student-Name:   obtained_marks / full_marks
#
#

def topper():
    with open('students.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = {}
        for row in csv_reader:
            if line_count == 0:
                print(f'{"\t\t".join(row)}')
                line_count += 1
            else:
                if row[0] in data:

                    data[row[0]]+=[{row[1]:int(row[2].replace("/100","").rstrip())+int(row[3].replace("/100","").rstrip())+int(row[4].replace("/100","").rstrip())+int(row[5].replace("/100","").rstrip())+int(row[6].replace("/100","").rstrip())+int(row[7].replace("/100","").rstrip())+int(row[8].replace("/100","").rstrip())}]
                else:
                    data[row[0]]=[{row[1]:int(row[2].replace("/100","").rstrip())+int(row[3].replace("/100","").rstrip())+int(row[4].replace("/100","").rstrip())+int(row[5].replace("/100","").rstrip())+int(row[6].replace("/100","").rstrip())+int(row[7].replace("/100","").rstrip())+int(row[8].replace("/100","").rstrip())}]
                # print(row[0])
                # print(
                #     f"{row[0]}\t\t{row[1]}\t\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}\t\t{row[7]}\t\t{row[8]}")
                line_count += 1
        for key, value in data.items():
            print(f"{key}:{value}")




def parse_marks(mark):
    got, full = map(int, mark.split('/'))
    return got, full

def calculate_results():
    data = {}
    with open("students.csv", mode='r') as file:
        file_read = csv.DictReader(file)
        # print(file_read)
        for row in file_read:
            year = row['year']
            student = {
                'Name': row['student_name'],
                'Maths': parse_marks(row['math']),
                'Physics': parse_marks(row['phy']),
                'Chemistry': parse_marks(row['che']),
                'Computer Science': parse_marks(row['comp']),
                'English': parse_marks(row['eng']),
                'FailedSubjects': [],
                'TotalMarks': 0
            }
            print(student)
            # {'Name': 'VVVVV', 'Maths': (25, 100), 'Physics': (47, 100), 'Chemistry': (5, 100), 'Computer Science': (25, 100), 'English': (16, 100), 'FailedSubjects': [], 'TotalMarks': 0}
            for subject, marks in student.items():
                if subject in ['Name', 'FailedSubjects', 'TotalMarks']:
                    continue
                obtained, full = marks
                if obtained < 33:
                    student['FailedSubjects'].append(subject)
                else:
                    student['TotalMarks'] += obtained

            if year not in data:
                data[year] = []
            data[year].append(student)

    # print(data.items())
    #  {'Name': 'YYYYY', 'Maths': (73, 100), 'Physics': (86, 100), 'Chemistry': (57, 100), 'Computer Science': (80, 100), 'English': (73, 100), 'FailedSubjects': [], 'TotalMarks': 369}

    for year, students in data.items():
        print(f"\nResults for the year {year}:")

        students.sort(key=lambda x: x['TotalMarks'], reverse=True)
        # print(students)
        # [{'Name': 'CCCCC', 'Maths': (70, 100), 'Physics': (91, 100), 'Chemistry': (86, 100), 'Computer Science': (81, 100), 'English': (96, 100), 'FailedSubjects': [], 'TotalMarks': 424},
        for i, student in enumerate(students[:3]):
            print(f"{i + 1}st Position: {student['Name']} with {student['TotalMarks']} marks")

        print("\nOther Students:")
        for student in students[3:]:
            if not student['FailedSubjects']:
                print(f"{student['Name']} with {student['TotalMarks']} marks (Passed)")
            else:
                print(f"{student['Name']} failed in {', '.join(student['FailedSubjects'])}")


def display():
    with open('students.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{"\t\t".join(row)}')
                line_count += 1
            else:
                print(f"{row[0]}\t\t{row[1]}\t\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}\t\t{row[7]}\t\t{row[8]}")
                line_count += 1
# Users can view a summary of all expenses.
# Users can view a summary of expenses for a specific month (of current year).

def summary(month):
    total = 0
    if month==13:
        with open('expenses.csv','r') as f:
            csv_reader = csv.reader(f,delimiter=',')
            line = 0
            for row in csv_reader:
                if line == 0:
                    line+=1
                else:
                    total+=int(row[3])
                    line+=1
            print(f"Total expenses: ${total}")
    else:
        with open('expenses.csv','r') as f:
            csv_reader = csv.reader(f,delimiter=',')
            line = 0
            for row in csv_reader:
                if line == 0:
                    line+=1
                else:
                    date_str = row[1]
                    month_exp = date_str.split("-")[1]
                    if(int(month)==int(month_exp)):
                        total+=int(row[3])
                    line+=1
            print(f"Total expenses: ${total}")
# Here are some additional features that you can add to the application:

# Add expense categories and allow users to filter expenses by category.
# Allow users to set a budget for each month and show a warning when the user exceeds the budget.
# Allow users to export expenses to a CSV file.

# The list of commands and their expected output is shown below:





# $ expense-tracker summary
# # Total expenses: $30



# $ expense-tracker delete --id 1
# # Expense deleted successfully

# $ expense-tracker update --id 1 --description "Lunch" --amount 50
# # Expense updated successfully

# $ expense-tracker summary
# # Total expenses: $20

# $ expense-tracker summary --month 8
# # Total expenses for August: $20
# Implementation
# You can implement the application using any programming language of your choice. Here are some suggestions:

# Use any programming language for any available module for parsing command arguments (e.g. python with the argparse, node.js with commander etc).
# Use a simple text file to store the expenses data. You can use JSON, CSV, or any other format to store the data.
# Add error handling to handle invalid inputs and edge cases (e.g. negative amounts, non-existent expense IDs, etc).
# Use functions to modularize the code and make it easier to test and maintain.
import sys
def main():
    print("Welcome to Expense Tracker!!!")
    arg = sys.argv[1]
    match arg:
        case "topper":
            topper()
        case "list":
            display()
        case "calc":
            calculate_results()
        case "update":
            update_exp(sys.argv[3],sys.argv[5],sys.argv[7])
        case "summary":
            month = sys.argv[3] if len(sys.argv) > 3 else 13
            summary(month)
        case "delete":
            delete_exp(sys.argv[3])
        case _:
            print("The given argument(s) isn't supported.")
main()