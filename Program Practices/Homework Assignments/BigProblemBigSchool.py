'''

The 🅱️ig city school 🅱️oard has hired you to develop a student course tracker system. 
You will need to create a Student class which can help track a student’s average and overall course load.

You need to implement a function to add a course to a Student’s course list, a function to update a Course’s mark given the Course’s subject (course name) and teacher, 
and a function to get the overall average of the student across all their courses.

(Hint: create a separate class called Course and create a list of Course type objects in Student)


'''



class Course():
    def __init__(self, subject, teacher, mark):
        self.subject = subject
        self.teacher = teacher
        self.mark = mark

class Student():
    def __init__(self, name):
        self.student_name = name
        self.courses = []

    def add_course(self, subject, teacher, mark):
        c_course = Course(subject, teacher, mark)
        self.courses.append(c_course)
    
    def update_course_mark(self, mark, subject, teacher):
        for i in range(self.courses):
            if i.subject == subject and i.teacher == teacher:
                i.mark = mark

    def get_overall_average_score(self):
        sum = 0.0
        for score in range(self.courses):
            sum += score.mark
        return sum / len(self.courses)

