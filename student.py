class Student:
  
    
    def __init__(self, name, family):
        self.courseMarks = {} 
        self.firstname = name 
        self.lastname = family

    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark 
    
    def average(self):
        average = None
        mark = 0 
        for mark in courseMarks:
            mark += mark
        average = mark / len(courseMarks)
