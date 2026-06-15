from tinydb import TinyDB
import socket
import json

db = TinyDB("nodeA.json")

student = {
    "id": "23010178",
    "name": "Nguyen Huy ha",
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