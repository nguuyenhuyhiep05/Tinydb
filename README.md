# Tinydb
##1. Dự án đã chọn

Tên dự án: TinyDB

Ngôn ngữ lập trình: Python

Mô tả:
TinyDB là một hệ quản trị cơ sở dữ liệu NoSQL hướng tài liệu (Document-Oriented Database) được viết hoàn toàn bằng Python. Dữ liệu được lưu trữ dưới dạng tệp JSON, không yêu cầu cài đặt máy chủ cơ sở dữ liệu riêng biệt.

Công nghệ sử dụng:

Python 3.x
TinyDB
JSON
##2. Mục đích, chức năng và ứng dụng thực tế
Mục đích
Lưu trữ dữ liệu đơn giản cho các ứng dụng Python.
Thay thế cơ sở dữ liệu quan hệ trong các dự án nhỏ.
Hỗ trợ thao tác dữ liệu dễ dàng mà không cần cài đặt MySQL hoặc PostgreSQL.
Chức năng
Thêm dữ liệu (Insert)
Tìm kiếm dữ liệu (Search)
Cập nhật dữ liệu (Update)
Xóa dữ liệu (Delete)
Lọc dữ liệu theo điều kiện
Ứng dụng thực tế
Quản lý sinh viên
Quản lý thư viện
Lưu cấu hình phần mềm
Hệ thống IoT quy mô nhỏ
Các ứng dụng Desktop Python
##3. Thiết lập cài đặt và kết quả thực nghiệm
Bước 1: Cài đặt TinyDB

Lệnh cài đặt:

pip install tinydb

Bước 2: Tạo cơ sở dữ liệu

from tinydb import TinyDB

db = TinyDB('students.json')

Bước 3: Thêm dữ liệu

db.insert({
'id':'SV001',
'name':'Nguyen Van A',
'gpa':3.5
})

Bước 4: Truy vấn dữ liệu

from tinydb import Query

Student = Query()

result = db.search(Student.id == 'SV001')

print(result)

Kết quả

[
{'id':'SV001',
'name':'Nguyen Van A',
'gpa':3.5}
]

Nhận xét:

TinyDB hoạt động ổn định.
Thao tác CRUD đơn giản.
Tốc độ phù hợp với dữ liệu nhỏ và trung bình.
##4. Phát triển hai tính năng mới liên quan đến xử lý phân tán
###Tính năng 1: Đồng bộ dữ liệu giữa nhiều nút (Data Replication)

Mô tả:

Mỗi máy tính (Node) có một bản sao TinyDB riêng.

Khi Node A cập nhật dữ liệu:

Gửi bản cập nhật qua Socket TCP.
Các Node còn lại nhận và cập nhật dữ liệu.
Bảo đảm dữ liệu giống nhau trên toàn hệ thống.

Lợi ích:

Tăng khả năng chịu lỗi.
Một Node hỏng vẫn còn dữ liệu ở Node khác.

###Tính năng 2: Truy vấn phân tán (Distributed Query)

Mô tả:

Dữ liệu được chia trên nhiều Node.

Node trung tâm gửi yêu cầu truy vấn tới tất cả Node.

Các Node:

Tìm kiếm dữ liệu cục bộ.
Trả kết quả về máy chủ.

Máy chủ:

Tổng hợp kết quả.
Trả về cho người dùng.
#2 tính năng phát triển mới
1.tính năng 1
File server.py

(Node B và Node C chạy file này)

from tinydb import TinyDB
import socket
import json
import threading

DB_FILE = "node_db.json"
HOST = "0.0.0.0"
PORT = 5000

db = TinyDB(DB_FILE)

def handle_client(conn):
    data = conn.recv(4096).decode()

    if data:
        student = json.loads(data)

        # Ghi dữ liệu vào TinyDB
        db.insert(student)

        print("\n[+] Đã nhận dữ liệu:")
        print(student)

    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Server đang lắng nghe tại cổng {PORT}...")

    while True:
        conn, addr = server.accept()
        print(f"Kết nối từ {addr}")

        thread = threading.Thread(
            target=handle_client,
            args=(conn,)
        )
        thread.start()

if __name__ == "__main__":
    start_server()

    File client_replication.py

(Node A gửi dữ liệu đến các node khác)

from tinydb import TinyDB
import socket
import json

db = TinyDB("nodeA.json")

student = {
    "id": "23010178",
    "name": "Nguyen Huy Hiep",
    "major": "CNTT",
    "gpa": 3.7
}

# Lưu dữ liệu cục bộ
db.insert(student)

# Danh sách các node cần đồng bộ
nodes = [
    ("127.0.0.1", 5000),
    # Có thể thêm:
    # ("192.168.1.10", 5000),
    # ("192.168.1.11", 5000)
]

for host, port in nodes:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        client.send(
            json.dumps(student).encode()
        )

        client.close()

        print(f"Đã đồng bộ đến {host}:{port}")

    except Exception as e:
        print("Lỗi:", e)

print("\nHoàn tất đồng bộ dữ liệu.")
