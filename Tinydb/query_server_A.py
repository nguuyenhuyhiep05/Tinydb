from tinydb import TinyDB, Query
import socket
import json

db = TinyDB("nodeC.json")
Student = Query()

HOST = "0.0.0.0"
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Node C đang chờ truy vấn...")

while True:
    conn, addr = server.accept()

    gpa = float(conn.recv(1024).decode())

    result = db.search(Student.gpa >= gpa)

    conn.send(json.dumps(result).encode())

    conn.close()