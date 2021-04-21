class Student:
    def __init__(self, row):
        self.name = row[0].lower()
        self.code = row[1]
        self.reference = row[2]
        self.award = row[3]
        self.type = row[4]
        
    def __str__(self):
        return f"{self.name} {self.code} {self.reference} {self.award} {self.type}"

    def __repr__(self):
        return "\n" + self.__str__() + "\n"

