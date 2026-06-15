import socket
import json

# Danh sách các node
nodes = [
    ("127.0.0.1", 6000),  # Node A
    ("127.0.0.1", 6001)   # Node B
]

# Nhập điều kiện tìm kiếm
gpa_condition = float(input("Nhập GPA tối thiểu: "))

all_results = []

# Gửi truy vấn đến từng node
for host, port in nodes:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        client.send(str(gpa_condition).encode())

        response = client.recv(4096).decode()
        data = json.loads(response)

        all_results.extend(data)

        client.close()

    except Exception as e:
        print(f"Không kết nối được tới {host}:{port}")
        print(e)

print("\n===== KẾT QUẢ TRUY VẤN PHÂN TÁN =====")

for student in all_results:
    print(
        f"{student['id']} | "
        f"{student['name']} | "
        f"{student['major']} | "
        f"GPA: {student['gpa']}"
    )