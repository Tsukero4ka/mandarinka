from numpy import mean, array
import uuid
MAX_SIZE = 20


class Student:
    """Class for storing info of students"""
    def __init__(self, name, surname, grades):
        if not isinstance(name, str):
            raise TypeError('Name should be string data type!')
        if not isinstance(surname, str):
            raise TypeError('Surname should be string data type!')
        if not all(isinstance(x, int) for x in grades.values()):
            raise TypeError('Grades values should be int type!')
        if not all(isinstance(x, str) for x in grades.keys()):
            raise TypeError('Grades keys should be string type!')
        self.__name = name
        self.__surname = surname
        self.__id = uuid.uuid4()
        self.__grades = grades

    def __str__(self):
        return f'{self.name} {self.surname}, student id: {self.__id}, average grade: {self.get_average()}'

    def get_average(self):
        return mean(list(self.grades.values()))

    def name(self):
        return self.__name

    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name should be string data type!')
        self.__name = value

    def surname(self):
        return self.__surname

    def surname(self, value):
        if not not isinstance(value, str):
            raise TypeError('Surname should be string data type!')
        self.__surname = value

    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        if not all(isinstance(x, int) for x in value.values()):
            raise TypeError('Grades values should be int type!')
        if not all(isinstance(x, str) for x in value.keys()):
            raise TypeError('Grades keys should be string type!')
        self.__grades = value


class Group:
    def __init__(self):
        self.__student_list = []
        self.__students = 0

    def checker(self, inp):
        return inp.name + inp.surname in [x.name + x.surname for x in self.__student_list]

    def add_student(self, inp):
        if self.__students == MAX_SIZE:
            raise AssertionError('No more than 20 students in a group!')
        if not isinstance(inp, Student):
            raise TypeError('Input should be Student type!')
        if self.checker(inp):
            raise ValueError('Student with this name and surname already exists!')
        self.__student_list.append(inp)
        self.__students += 1

    def top_five(self):
        avg = array([x.get_average() for x in self.__student_list])
        ids = (-avg).argsort()[:5]
        return [self.__student_list[x] for x in ids]

    def __str__(self):
        return '\n'.join([str(x) for x in self.top_five()])


def main():
    a = Student('Yehor', 'Skachedub', {'subj1': 56, 'subj2': 90, 'subj3': 79, 'subj4': 82, 'subj5': 78})
    b = Student('Vlad', 'Babenko', {'subj1': 70, 'subj2': 74, 'subj3': 89, 'subj$': 92, 'subj5': 88})
    c = Student('Vlad', 'Kuzmenko', {'subj1': 75, 'subj2': 76, 'subj3': 75, 'subj4': 96, 'subj5': 73})
    d = Student('Mikita', 'Serikov', {'subj1': 94, 'subj2': 70, 'subj3': 68, 'subj4': 71, 'subj5': 67})
    e = Student('Nazariy', 'Galich', {'subj1': 74, 'subj2': 61, 'subj3': 60, 'subj4': 94, 'subj5': 60})
    f = Student('Max', 'Palamar', {'subj1': 95, 'subj2': 94, 'subj3': 64, 'subj4': 97, 'subj5': 93})

    group = Group()
    group.add_student(a)
    group.add_student(b)
    group.add_student(c)
    group.add_student(d)
    group.add_student(e)
    group.add_student(f)
    print(group)


if __name__ == '__main__':
    main()