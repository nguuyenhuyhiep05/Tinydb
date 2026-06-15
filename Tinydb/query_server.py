from tinydb import TinyDB, Query
import socket
import json

db = TinyDB("node_db.json")
Student = Query()

HOST = "0.0.0.0"
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Query Server đang chạy...")

while True:
    conn, addr = server.accept()

    data = conn.recv(1024).decode()

    try:
        gpa_limit = float(data)

        result = db.search(
            Student.gpa >= gpa_limit
        )

        conn.send(
            json.dumps(result).encode()
        )

    except:
        conn.send(
            json.dumps([]).encode()
        )

    conn.close()