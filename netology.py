class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'\
               f'Средняя оценка за домашние задания: {self.avgocenka()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def avgocenka(self):
        sumocenk = 0
        i = 0
        avgocenk = 0
        for listocenka in self.grades.values():
            for ocenka in listocenka:
                sumocenk += ocenka
                i += 1
                avgocenk = sumocenk / i
        return round(avgocenk, 1)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, (int, float, Student)):
            raise TypeError("Нельзя сравнить эти параметры")

        sc = other if isinstance(other, (int, float)) else other.avgocenka()
        return self.avgocenka() < sc

    def __eq__(self, other):
        if not isinstance(other, (int, float, Student)):
            raise TypeError("Нельзя сравнить эти параметры")

        sc = other if isinstance(other, (int, float)) else other.avgocenka()
        return self.avgocenka() == sc

    def __le__(self, other):
        if not isinstance(other, (int, float, Student)):
            raise TypeError("Нельзя сравнить эти параметры")

        sc = other if isinstance(other, (int, float)) else other.avgocenka()
        return self.avgocenka() <= sc


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avgocenka()}'

    def avgocenka(self):
        sumocenk = 0
        i = 0
        avgocenk = 0
        for listocenka in self.grades.values():
            for ocenka in listocenka:
                sumocenk += ocenka
                i += 1
                avgocenk = sumocenk / i
        return round(avgocenk, 1)

    def __lt__(self, other):
        if not isinstance(other, (int, float, Lecturer)):
            raise TypeError("Нельзя сравнить эти параметры")

        sc = other if isinstance(other, (int, float)) else other.avgocenka()
        return self.avgocenka() < sc

    def __eq__(self, other):
        if not isinstance(other, (int, float, Lecturer)):
            raise TypeError("Нельзя сравнить эти параметры")

        sc = other if isinstance(other, (int, float)) else other.avgocenka()
        return self.avgocenka() == sc

    def __le__(self, other):
        if not isinstance(other, (int, float, Lecturer)):
            raise TypeError("Нельзя сравнить эти параметры")

        sc = other if isinstance(other, (int, float)) else other.avgocenka()
        return self.avgocenka() <= sc


class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def avgstudentocenka(students, course_name):
    sumx = 0
    i = 0
    avgstudent = 0
    for r in students:
        for t in r.grades.items():
            if t[0] == course_name:
                for x in t[1]:
                    sumx += x
                    i += 1
                    avgstudent = sumx / i
    return round(avgstudent, 1)


def avglecturerocenka(lecturers, course_name):
    sumx = 0
    i = 0
    avglecturer = 0
    for r in lecturers:
        for t in r.grades.items():
            if t[0] == course_name:
                for x in t[1]:
                    sumx += x
                    i += 1
                    avglecturer = sumx / i
    return round(avglecturer, 1)


best_student = Student('Ruoy', 'Eman', 'female')
best_student.courses_in_progress += ['Python', 'JS', 'Java', 'Figma', 'SQL']
best_student.finished_courses += ['Random']

studentik = Student('Norman', 'Ridus', 'male')
studentik.courses_in_progress += ['Python', 'JS', 'Java', 'Figma', 'SQL']
studentik.finished_courses += ['Random']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'JS', 'Java', 'Figma', 'SQL']

simple_mentor = Mentor('Larry', 'David')
simple_mentor.courses_attached += ['Python', 'JS', 'Java', 'SQL']

rev = Reviewer('Ivan', 'Ivanov')
rev.courses_attached += ['Python', 'JS', 'Java', 'SQL']
rev.rate_hw(best_student, 'Python', 10)
rev.rate_hw(best_student, 'JS', 8)
rev.rate_hw(best_student, 'Figma', 7)
rev.rate_hw(studentik, 'Python', 10)
rev.rate_hw(studentik, 'JS', 8)
rev.rate_hw(studentik, 'Figma', 7)

rev2 = Reviewer('David', 'Brown')
rev2.courses_attached += ['Python', 'JS', 'Java', 'SQL']
rev.rate_hw(best_student, 'Python', 4)
rev.rate_hw(best_student, 'JS', 5)
rev.rate_hw(best_student, 'Figma', 6)
rev.rate_hw(studentik, 'Python', 8)
rev.rate_hw(studentik, 'JS', 9)
rev.rate_hw(studentik, 'Figma', 10)

lec1 = Lecturer('Sergio', 'Mold')
lec1.courses_attached += ['Python', 'JS', 'Java', 'Figma', 'SQL']
lec2 = Lecturer('Ralf', 'Loren')
lec2.courses_attached += ['Python', 'JS', 'Java']

best_student.rate_lecturer(lec1, 'Python', 10)
best_student.rate_lecturer(lec1, 'Figma', 7)
best_student.rate_lecturer(lec1, 'JS', 8)
best_student.rate_lecturer(lec2, 'Python', 1)

studentik.rate_lecturer(lec1, 'JS', 3)
studentik.rate_lecturer(lec1, 'Figma', 4)
studentik.rate_lecturer(lec1, 'Python', 5)
studentik.rate_lecturer(lec2, 'Python', 3)

print(lec1)
print(lec2)
print(best_student)
print(studentik)
print(rev)
print(rev2)
print(studentik.avgocenka())
print(best_student.avgocenka())
print(lec1.avgocenka())
print(lec2.avgocenka())
print(lec1 > lec2)
print(lec1 == lec2)
print(lec1 <= lec2)
print(studentik == best_student)
print(avgstudentocenka([best_student, studentik], 'Python'))
print(avgstudentocenka([lec1, lec2], 'Python'))
