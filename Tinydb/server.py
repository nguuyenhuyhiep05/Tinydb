from tinydb import TinyDB
import socket
import json
import threading

HOST = "0.0.0.0"
PORT = 5000

# Cơ sở dữ liệu của Node B
db = TinyDB("nodeB.json")

def handle_client(conn):
    try:
        data = conn.recv(4096).decode("utf-8")

        if data:
            student = json.loads(data)

            # Lưu dữ liệu vào TinyDB
            db.insert(student)

            print("\n[ĐỒNG BỘ] Đã nhận dữ liệu:")
            print(student)

    except Exception as e:
        print("Lỗi:", e)

    finally:
        conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Node B đang lắng nghe cổng {PORT}...")

while True:
    conn, addr = server.accept()
    print("Kết nối từ:", addr)

    thread = threading.Thread(
        target=handle_client,
        args=(conn,)
    )
    thread.start()