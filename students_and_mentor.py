class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Средняя оценка за домашние задания 
    def __average_rating__(self):
        avg = 0
        cnt = 0
        for course in self.grades:
            cnt += len(self.grades[course])
            for grade in self.grades[course]:
                avg += grade
        if cnt > 0:
            avg /= cnt
        return avg

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_rating__()}\n'
                f'Курсы в процессе изучения: {str.join(", ", self.courses_in_progress)}\n'
                f'Завершенные курсы: {str.join(", ", self.finished_courses)}')
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__average_rating__() < other.__average_rating__()
        else:
            return 'Ошибка'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__average_rating__() == other.__average_rating__()
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.__average_rating__() > other.__average_rating__()
        else:
            return 'Ошибка'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
      

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    # Средняя оценка за лекции
    def __average_rating__(self):
        avg = 0
        cnt = 0
        for course in self.grades:
            cnt += len(self.grades[course])
            for grade in self.grades[course]:
                avg += grade
        if cnt > 0:
            avg /= cnt
        return avg

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_rating__()}'
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__average_rating__() < other.__average_rating__()
        else:
            return 'Ошибка'

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.__average_rating__() == other.__average_rating__()
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.__average_rating__() > other.__average_rating__()
        else:
            return 'Ошибка'

        
class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Студент № 1
best_student = Student('Иван', 'Пупкин', 'Мужской')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

# Студент № 2
bad_student = Student('Джон', 'Доу', '-')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Git']
bad_student.finished_courses += ['Введение в программирование']

# Лектор № 1
best_lecturer = Lecturer('Ричард', 'Сидоров')
best_lecturer.courses_attached += ['Python', 'Git']

# Лектор № 2
bad_lecturer = Lecturer('Пабло', 'Педалес')
bad_lecturer.courses_attached += ['Python', 'Git']

# Проверяющий
cool_reviwer = Reviewer('Дуня', 'Иванова')
cool_reviwer.courses_attached += ['Python', 'Git']

# Оценки студента № 1
cool_reviwer.rate_hw(best_student, 'Python', 10)
cool_reviwer.rate_hw(best_student, 'Git', 8)
cool_reviwer.rate_hw(best_student, 'Python', 8)

# Оценки студента № 2
cool_reviwer.rate_hw(bad_student, 'Python', 5)
cool_reviwer.rate_hw(bad_student, 'Git', 4)
cool_reviwer.rate_hw(bad_student, 'Python', 3)

# Оценки лектора № 1
best_student.rate_hw(best_lecturer, 'Python', 10)
best_student.rate_hw(best_lecturer, 'Python', 9)
best_student.rate_hw(best_lecturer, 'Python', 8)
best_student.rate_hw(best_lecturer, 'Git', 9)
best_student.rate_hw(best_lecturer, 'Git', 10)

# Оценки лектора № 2
bad_student.rate_hw(bad_lecturer, 'Python', 6)
bad_student.rate_hw(bad_lecturer, 'Python', 4)
bad_student.rate_hw(bad_lecturer, 'Python', 5)
bad_student.rate_hw(bad_lecturer, 'Git', 4)
bad_student.rate_hw(bad_lecturer, 'Git', 4) 

# Строковые представления объектов
print(cool_reviwer)
print(best_lecturer)
print(bad_lecturer)
print(best_student)
print(bad_student)

# Сравнения студентов
print(f'best_student < bad_student = {best_student < bad_student}')
print(f'best_student == bad_student = {best_student == bad_student}')
print(f'best_student > bad_student = {best_student > bad_student}')

# Сравнения лекторов
print(f'best_lecturer < bad_lecturer = {best_lecturer < bad_lecturer}')
print(f'best_lecturer == bad_lecturer = {best_lecturer == bad_lecturer}')
print(f'best_lecturer > bad_lecturer = {best_lecturer > bad_lecturer}')

# Средняя оценка за домашние задания по курсу
def average_course_student(cource, students):
    val = 0
    all_val =0
    for student in students:
        if isinstance(student, Student) and cource in student.grades and len(student.grades[cource]) > 0:
            val = 0
            for grade in student.grades[cource]:
                val += grade
            all_val += val / len(student.grades[cource])
    return all_val / len(students)

print(f'Python, средняя оценка за домашние задания по курсу - {average_course_student("Python", [best_student, bad_student])}')
print(f'Git, средняя оценка за домашние задания по курсу - {average_course_student("Git", [best_student, bad_student])}')
print(f'JS, средняя оценка за домашние задания по курсу - {average_course_student("JS", [best_student, bad_student])}')

# Средняя оценка за лекции по курсу
def average_course_lecturer(cource, lecturers):
    val = 0
    all_val =0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and cource in lecturer.grades and len(lecturer.grades[cource]) > 0:
            val = 0
            for grade in lecturer.grades[cource]:
                val += grade
            all_val += val / len(lecturer.grades[cource])
    return all_val / len(lecturers)

print(f'Python, средняя оценка за лекции по курсу - {average_course_lecturer("Python", [best_lecturer, bad_lecturer])}')
print(f'Git, средняя оценка за лекции по курсу - {average_course_lecturer("Git", [best_lecturer, bad_lecturer])}')
print(f'C#, средняя оценка за лекции по курсу - {average_course_lecturer("C#", [best_lecturer, bad_lecturer])}')