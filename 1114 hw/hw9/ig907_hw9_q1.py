import os
class Student:
    name = ""
    NYU_id = ""
    net_id = ""
    grades_list = {}

    def __init__(self, name, NYU_id, net_id):
        self.name = name
        self.NYU_id = NYU_id
        self.net_id = net_id
        self.grades_list = {}

    def __repr__(self):
        return ("Name: " + self.name + "NYU id: " + self.NYU_id + "net id: " + self.net_id + "Grades list: " + self.grades_list)
    def add_grade(self, catalog_name, grade):
        add = []
        add.append(catalog_name)
        add.append(grade)
        self.grades_list[catalog_name] = grade

    def average(self): #needs to be fixed for tuple support
       denom = len(self.grades_list)
       sum = 0
       for key in self.grades_list:
           if(self.grades_list[key] != '' and self.grades_list[key] != "\n"):
               sum+= int(self.grades_list[key])
       average = str(sum/denom)
       return average
    def get_email(self):
        return (self.net_id + "@nyu.edu")

def load_students(students_data_filename):
    studentDictionary = {}
    listOfStudents =[]
    studentsDataFile = open(students_data_filename, "r")

    for line in studentsDataFile:
        currentLine = studentsDataFile.readline()
        listOfStudents.append(currentLine.split(","))
    header = listOfStudents[0]

    for i in range(len(listOfStudents)):
        currentStudent = listOfStudents[i]
        NYU_id = currentStudent[0]
        name = currentStudent[1]
        net_id = currentStudent[2]
        studentDictionary[name] = Student(name, NYU_id, net_id)
        for j in range(3, len(listOfStudents[i])):
            studentDictionary[name].add_grade(header[j], currentStudent[j])
    return studentDictionary

def generate_performance_report(students_lst, out_filename):
    performanceReport = []
    header = ("NYU ID,Average")
    newFile = open(out_filename, "w")
    newFile.write(header+"\n")
    for key in students_lst:
        NYU_id = students_lst[key].NYU_id
        average = students_lst[key].average()
        newFile.write(NYU_id+","+average+"\n")

def generate_course_mailing_list(students_lst, catalog_name, out_filename): #this is the part that's broken
    outFile = open(out_filename, "w")
    for key in students_lst:
        for key2 in students_lst[key].grades_list:
            if (students_lst[key].grades_list[key2] != ''):
                outFile.write(students_lst[key].get_email()+"\n")



def main():
    filename = input("Enter the filename")
    studentDictionary = load_students(filename)
    newFilename = input("Enter a name for the report file: ")
    generate_performance_report(studentDictionary, newFilename)
    generate_course_mailing_list(studentDictionary, "CS-UY 1114", "CS 1114 Mailing list.csv")
    generate_course_mailing_list(studentDictionary, "MA-UY 1024", "MA-UY 1024 Mailing list.csv")
    generate_course_mailing_list(studentDictionary, "EG-UY 1001", "EG-UY 1001 Mailing list.csv")
    generate_course_mailing_list(studentDictionary, "EG-UY 1003", "EG-UY 1003 Mailing list.csv")
    generate_course_mailing_list(studentDictionary, "CS-UY 1122", "CS-UY 1122 Mailing list.csv")
    generate_course_mailing_list(studentDictionary, "CS-UY 1134", "CS-UY 1134 Mailing list.csv")
    generate_course_mailing_list(studentDictionary, "MA-UY 1124", "MA-UY 1124 Mailing list.csv")

main()


