class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def display_info(self):
        return f"Course Code: {self.course_code}\nCourse Name: {self.course_name}"

class UndergraduateCourse(Course):
    def __init__(self, course_code, course_name, year_level):
        super().__init__(course_code, course_name)
        self.year_level = year_level

    def additional_info(self):
        return f"Year Level: {self.year_level}"

class GraduateCourse(Course):
    def __init__(self, course_code, course_name, research_area):
        super().__init__(course_code, course_name)
        self.research_area = research_area

    def additional_info(self):
        return f"Research Area: {self.research_area}"

def register_course():
    while True:
        course_type = input("Enter:\n1 for Under-Graduate\n2 for Graduate\n3 for Quit:\nWaiting for input: ")
        if course_type == "1":
            course_code = input("Enter course code: ")
            course_name = input("Enter course name: ")
            year_level = input("Enter year level: ")
            course = UndergraduateCourse(course_code, course_name, year_level)
            print(f"Your Course has Registered\n{course.display_info()}\n{course.additional_info()}")
        elif course_type == "2":
            course_code = input("Enter course code: ")
            course_name = input("Enter course name: ")
            research_area = input("Enter research area: ")
            course = GraduateCourse(course_code, course_name, research_area)
            print(f"Your Course has Registered\n{course.display_info()}\n{course.additional_info()}")
        elif course_type == "3":
            break

        else:
            print("Choose correct option.")
                    
register_course()
