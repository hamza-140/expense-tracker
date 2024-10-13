import csv
def display():
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

def calc_result():
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


import sys
def main():
    print("Welcome to Result Calculate!!!")
    arg = sys.argv[1]
    match arg:
        case "display":
            display()
        case "calc":
            calc_result()
        case _:
            print("The given argument(s) isn't supported.")
main()