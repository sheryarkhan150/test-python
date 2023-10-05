import csv
""""
rows = []
with open("Salary_Data.csv","r") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

with open("Salary_Data.csv") as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
print(rows)

with open("Salary_Data.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)"""
        
with open("Students.csv","w", newline='') as csvfile:
    data = [{'Name': 'Alex', 'M1 Score': 62, 'M2 Score': 80},
        {'Name': 'Brad', 'M1 Score': 45, 'M2 Score': 56},
        {'Name': 'Joey', 'M1 Score': 85, 'M2 Score': 98}]
    fieldnames = ['Name', 'M1 Score', 'M2 Score']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)