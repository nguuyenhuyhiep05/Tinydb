from tinydb import TinyDB, Query

db = TinyDB('students.json')
Student = Query()

# Thêm sinh viên
db.insert({
    'id': 'SV001',
    'name': 'Nguyen Huy Hiep',
    'gpa': 3.5
})

# Tìm sinh viên
student = db.search(Student.id == 'SV001')
print(student)

# Cập nhật GPA
db.update({'gpa': 3.8}, Student.id == 'SV001')

# Hiển thị toàn bộ
for s in db.all():
    print(s)
