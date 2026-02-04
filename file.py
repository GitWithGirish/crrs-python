class Student:
    def __init__(self, name, student_id, email, phone):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone

    def display(self):
        print("ID: ", self.student_id, "Name: ", self.student_id,
              "E-mail: ", self.email, "Phone: ", self.phone)

    def update_info(self, name=None, student_id=None, email=None, phone=None):
        if name != "" and name != None:
            self.name = name
        if student_id != "" and student_id != None:
            self.student_id = student_id
        if email != "" and email != None:
            self.email = email
        if phone != "" and phone != None:
            self.phone = phone


class Courses:
    def __init__(self, title, course_id, credit):
        self.title = title
        self.course_id = course_id
        self.credit = credit

    def display(self):
        print("Course Title: ", self.title, "Course ID: ",
              self.course_id, "Total Credits: ", self.credit)


class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id

    def display(self):
        print("Enrollment ID: ", self.enrollment_id, "Student ID: ",
              self.student_id, "Course ID: ", self.course_id)


class Result:
    def __init__(self, result_id, enrollment_id, score):
        self.result_id = result_id
        self.enrollment_id = enrollment_id
        self.score = int(score)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.score >= 85:
            return "HD"
        elif self.score >= 75:
            return "D"
        elif self.score >= 65:
            return "C"
        elif self.score >= 50:
            return "P"
        elif self.score <= 50:
            return "F"
        else:
            return "INVALID"


STUDENTS_FILE = "students.txt"
COURSES_FILE = "courses.txt"
ENROLLMENTS_FILE = "enrollments.txt"
RESULTS_FILE = "results.txt"
LOG_FILE = "system_log.txt"


def load_file(filename):
    try:
        f = open(filename, "r")
        data = f.readlines()
        f.close()
        return data
    except:
        f = open(filename, "w")
        f.close()
        return []


def save_file(filename, data):
    f = open(filename, "w")
    for line in data:
        f.write(line)
        f.close()



def log(msg):
    f = open(LOG_FILE, "a")
    f.write(msg, "\n")
    f.close()


class CRRSManager:
    def __init__(self):
        self.students = load_file(STUDENTS_FILE)
        self.courses = load_file(COURSES_FILE)
        self.enrollments = load_file(ENROLLMENTS_FILE)
        self.results = load_file(RESULTS_FILE)
        log("System started")

    def add_student(self):
        sid = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        if name == "" or sid == "":
            print("Please enter the missing entries.")
            return

        for s in self.students:
            if s.startswith(sid + ","):
                print("Student already exists")
                return
        self.students.append(sid + "," + name + "," +
                             email + "," + phone + "\n")
        save_file(STUDENTS_FILE, self.students)
        log("Student added")

    def list_students(self):
        for s in self.students:
            print(s.strip())

    def update_student(self):
        sid = input("Enter Student ID to update: ")

        for i in range(len(self.students)):
            s = self.students[i].strip().split(",")
            if s[0] == sid:
                print("Leave blank to keep old value")
                name = input("New Name: ")
                email = input("New Email: ")
                phone = input("New Phone: ")

                if name == "":
                    name = s[1]
                if email == "":
                    email = s[2]
                if phone == "":
                    phone = s[3]

                self.students[i] = sid + "," + name + \
                    "," + email + "," + phone + "\n"
                save_file(STUDENTS_FILE, self.students)
                log("Student updated")
                print("Student updated")
                return
            else:
                print("Student not Found.")

    def add_course(self):
        title = input("Course Title: ")
        cid = input("Course ID: ")
        credit = input("Credit: ")

        if title == "" or cid == "":
            print("Please enter the missing entries.")
            return

        self.courses.append(cid + "," + title + "," + credit + "\n")
        save_file(COURSES_FILE, self.courses)
        log("Course added")

    def list_courses(self):
        for c in self.courses:
            print(c.strip())

    def update_course(self):
        cid = input("Enter Course ID to update: ")
        for i in range(len(self.courses)):
            c = self.courses[i].strip().split(",")
            if c[0] == cid:
                print("Leave blank to keep old value")

            title = input("New Title: ")
            credit = input("New Credit: ")

            if title == "":
                title = c[1]
            if credit == "":
                credit = c[2]

            self.courses[i] = cid + "," + title + "," + credit + "\n"
            save_file(COURSES_FILE, self.courses)
            log("Course updated")
            print("Course updated")
            return

    def enroll_student(self):
        eid = input("Enrollment ID: ")
        sid = input("Student ID: ")
        cid = input("Course ID: ")

        record = eid + "," + sid + "," + cid + "\n"
        if record in self.enrollments:
            print("Enrollment repeated")
            return

        self.enrollments.append(record)
        save_file(ENROLLMENTS_FILE, self.enrollments)
        log("Student enrolled")

    def list_enrollments(self):
        for e in self.enrollments:
            print(e.strip())

    def record_result(self):
        rid = input("Result ID: ")
        eid = input("Enrollment ID: ")
        score = input("Score (0-100): ")

        if not score.isdigit():
            print("Invalid score")
            return

        score = int(score)
        if score < 0 or score > 100:
            print("Invalid score")
            return

        r = Result()
        r.res(rid, eid, score)

        self.results.append(rid + "," + eid + "," +
                            str(score) + "," + r.grade + "\n")
        save_file(RESULTS_FILE, self.results)
        log("Result recorded")

    def view_results(self):
        for r in self.results:
            print(r.strip())

    def update_result(self):
        rid = input("Enter Result ID to update: ")
        for i in range(len(self.results)):
            r = self.results[i].strip().split(",")
            if r[0] == rid:
                new_score = input("New Score (0-100): ")

            if not new_score.isdigit():
                print("Invalid score")
                return

            new_score = int(new_score)
            if new_score < 0 or new_score > 100:
                print("Invalid score")
                return

            res = Result()
            res.res(rid, r[1], new_score)

            self.results[i] = rid + "," + r[1] + "," + \
                str(new_score) + "," + res.grade + "\n"
            save_file(RESULTS_FILE, self.results)
            log("Result updated")
            print("Result updated")
            return


def menu():
    print("\n1 Add Student")
    print("2 Add Course")
    print("3 Enroll Student")
    print("4 Record Result")
    print("5 View Students")
    print("6 View Courses")
    print("7 View Enrollments")
    print("8 View Results")
    print("9 Update Student")
    print("10 Update Course")
    print("11 Update Result")
    print("12 Exit")


def main():
    system = CRRSManager()
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.add_course()
        elif choice == "3":
            system.enroll_student()
        elif choice == "4":
            system.record_result()
        elif choice == "5":
            system.list_students()
        elif choice == "6":
            system.list_courses()
        elif choice == "7":
            system.list_enrollments()
        elif choice == "8":
            system.view_results()
        elif choice == "9":
            system.update_student()
        elif choice == "10":
            system.update_course()
        elif choice == "11":
            system.update_result()
        elif choice == "12":
            log("Program exited")
            break
        else:
            print("Invalid choice")


main()
