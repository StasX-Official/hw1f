class Math:
    def __init__(self, math_level):
        self.math_level = math_level

    def math_skills(self):
        return f"Math level: {self.math_level}"

class Language:
    def __init__(self, language_level):
        self.language_level = language_level

    def language_skills(self):
        return f"Language level: {self.language_level}"

class Science:
    def __init__(self, science_level):
        self.science_level = science_level

    def science_skills(self):
        return f"Science level: {self.science_level}"

class Student(Math, Language, Science):
    def __init__(self, name, math_level, language_level, science_level):
        self.name = name
        Math.__init__(self, math_level)
        Language.__init__(self, language_level)
        Science.__init__(self, science_level)
    def student_info(self):
        return f"Student: {self.name}, Math: {self.math_level}, Language: {self.language_level}, Science: {self.science_level}"

student = Student("Alex", "Advanced", "Intermediate", "Basic")
print(student.student_info())
print(student.math_skills())
print(student.language_skills())
print(student.science_skills())
