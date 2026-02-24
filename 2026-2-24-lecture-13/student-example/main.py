class Student:
    avg_to_gpa = 4.0

    def __init__(self, name, id = None, grades = None):
        if grades == None:
            grades = []

        self.name = name
        self.grades = grades
        self.id = id
        self._private = "hello world"

    def __str__(self):
        avg = self.calc_average()
        avg_str = ""
        if avg == None:
            avg_str =  f"Average: {avg}"
        else:
            avg_str = f"Average: {avg:.2f}"

        return f"{self.name}, {avg_str}"

    def add_grade(self, grade):
        self.grades.append(grade)

    def calc_average(self):
        if len(self.grades) < 1:
            return None

        total = 0
        for grade in self.grades:
            total += grade
        return (total / len(self.grades)) / 100

    def calc_gpa(self):
        avg = self.calc_average()
        if avg == None:
            return None

        return avg * self.avg_to_gpa

eric = Student("Eric", grades=[90,50,86,100,73])
john = Student("John")
john.add_grade(90)

print(eric)
print(john)

print(eric.calc_gpa())
print(john.calc_gpa())


test = "asdfr"
