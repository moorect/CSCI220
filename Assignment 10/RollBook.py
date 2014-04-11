# RollBook.py
# Author: Pharr

from Student import Student

class RollBook:
    def __init__(self, number, name, term):
        self.number = number     # really a string
        self.name = name
        self.term = term
        self.students = []

    ## addStudent appends a clone of the student
    def addStudent(self, stu):
        newStu = Student(stu.getStudentNumber(), stu.getFirst(),
                         stu.getLast(), stu.getGrades(), stu.getEnrollDate())
        self.students.append(newStu) 

    def displayCourseInfo(self):
        s = "Course: " + self.number + " - " + self.name + " - "
        s = s + self.term + "\n"
        return s

    def classAverage(self):
        avg = 0
        sum = 0.0
        count = 0
        for i in range(len(self.students)):
            stu = self.students[i]
            stuAvg = stu.calcAvg()
            if stuAvg >= 0:
                sum = sum + stuAvg
                count = count + 1
        if count != 0:
            avg = sum / count
        else:
            avg = "No average"
        return avg

    def __str__(self):
        s = "Course: " + self.number + " - " + self.name + " - "
        s = s + self.term + "\n"
        length = len(self.students)
        if length == 0:
            s = s + "No students enrolled\n"
        else:
            for stu in self.students:
                s = s + str(stu) + "\n\n"
        return s




