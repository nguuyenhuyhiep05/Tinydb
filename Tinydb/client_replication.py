from tinydb import TinyDB
import socket
import json

# CSDL của Node A
db = TinyDB("nodeA.json")

# ===== Nhập thông tin sinh viên =====
student = {
    "id": input("Nhập mã sinh viên: "),
    "name": input("Nhập tên sinh viên: "),
    "class": input("Nhập lớp: "),
    "gpa": float(input("Nhập GPA: "))
}

# Lưu dữ liệu vào Node A
db.insert(student)
print("\nĐã lưu vào Node A!")

# Danh sách node cần đồng bộ
nodes = [
    ("127.0.0.1", 5000)
]

# Gửi dữ liệu sang các node khác
for host, port in nodes:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        message = json.dumps(student)
        client.send(message.encode("utf-8"))

        client.close()

        print(f"Đã đồng bộ đến {host}:{port}")

    except Exception as e:
        print(f"Lỗi khi đồng bộ đến {host}:{port}")
        print(e)

print("\nHoàn tất đồng bộ.")