# Build a simple expense tracker application to manage your finances. The application should allow users to 
# add, delete, and view their expenses. The application should also provide a summary of the expenses.

# Requirements
# Application should run from the command line and should have the following features:

# Users can add an expense with a description and amount.
# $ expense-tracker add --description "Lunch" --amount 20
# # Expense added successfully (ID: 1)

# $ expense-tracker add --description "Dinner" --amount 10
# # Expense added successfully (ID: 2)
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
def update_exp(id):
    pass

# Users can delete an expense.
def delete_exp(id):
    pass

# Users can view all expenses.
# $ expense-tracker list
# # ID  Date       Description  Amount
# # 1   2024-08-06  Lunch        $20
# # 2   2024-08-06  Dinner       $10
def display():
    with open('expenses.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{"\t\t".join(row)}')
                line_count += 1
            else:
                print(f"{row[0]}\t\t{row[1]}\t{row[2]}\t\t\t{row[3]}")
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
        case "add":
            add_exp(sys.argv[3],sys.argv[5])
        case "list":
            display()
        # case "list":
        #     # if(len(sys.argv)>2):
            #     display_status(sys.argv[2])
            # else:
            #     display()
        case "summary":
            month = sys.argv[3] if len(sys.argv) > 3 else 13
            summary(month)
        case _:
            print("The given argument(s) isn't supported.")
main()