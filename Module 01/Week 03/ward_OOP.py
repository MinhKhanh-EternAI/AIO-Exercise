class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"- Name: {self.name}, YoB: {self.yob}, Grade: {self.grade}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"- Name: {self.name}, YoB: {self.yob}, Subject: {self.subject}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f"- Name: {self.name}, YoB: {self.yob}, Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctors(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_by_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average_yob(self):
        total_yob = sum(person.yob for person in self.people if isinstance(person, Teacher))
        num_teachers = sum(1 for person in self.people if isinstance(person, Teacher))
        return total_yob / num_teachers if num_teachers > 0 else 0


# Tạo Ward và thêm các đối tượng
ward = Ward("Ward-test")
ward.add_person(Student("Ngọc", 2020, "7"))
ward.add_person(Teacher("Đan", 1985, "Toán"))
ward.add_person(Teacher("Vy", 1990, "Lịch sử"))
ward.add_person(Doctor("Chi Mai", 1980, "Y học cổ truyển"))
ward.add_person(Doctor("Quỳnh", 1978, "Da liễu"))

# In thông tin
ward.describe()

# Đếm số lượng doctor
print(f"\nSố lượng bác sĩ: {ward.count_doctors()}")

# Sắp xếp theo tuổi và in lại
ward.sort_by_age()
print("\nSau khi sắp xếp theo độ tuổi:")
ward.describe()

# Tính trung bình tuổi của giáo viên
average_yob = ward.compute_average_yob()
print(f"\nAverage YoB of teachers: {average_yob}")
