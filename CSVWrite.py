import csv
filename = "Students_Data.csv"
header = []
data = []
with open(filename, "w", newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(data)

"""header = ["Name","M1 Score","M2 Score"]
data = [["Alex", 62, 80],["Brad", 45, 56],["Joey", 85, 98]]
filename = "Student_scores.csv"
with open(filename,"w") as file:
    for header in header:
        file.write(str(header)+", ")
    file.write('n')
    for row in data:
        for x in row:
            file.write(str(x)+", ")
        file.write('n')"""
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
filename = 'Student_scores.csv'
with open(filename, 'w') as file:
    for header in header:
        file.write(str(header)+', ')
    file.write('n')
    for row in data:
        for x in row:
            file.write(str(x)+', ')
        file.write('n')