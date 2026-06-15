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
        db.insert(student)
        print("[+] Đã nhận:", student)

    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Server đang lắng nghe tại cổng {PORT}...")

    while True:
        conn, addr = server.accept()
        print("Kết nối từ:", addr)

        threading.Thread(
            target=handle_client,
            args=(conn,)
        ).start()

if __name__ == "__main__":
    start_server()