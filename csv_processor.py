import csv

from student import Student


class CSVImporter:
    def __init__(self):
        pass

    def process(self):
        students = []
        with open("data/small.csv", newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row in reader:
                students.append(Student(row))
        return students


