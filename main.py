import os
import requests
import json

# URL máy chủ quản lý thiết bị
server_url = "https://your-server.com/devices"

def lay_thiet_bi():
    try:
        response = requests.get(server_url)
        thiet_bi = response.json().get('devices', [])
        return thiet_bi
    except Exception as e:
        print(f"Lỗi khi lấy danh sách thiết bị: {e}")
        return []

def dieu_khien_thiet_bi(ma_thiet_bi, lenh):
    try:
        control_url = f"https://your-server.com/control/{ma_thiet_bi}"
        payload = {'command': lenh}
        response = requests.post(control_url, json=payload)
        print(f"Phản hồi điều khiển: {response.status_code}")
    except Exception as e:
        print(f"Lỗi khi gửi lệnh điều khiển: {e}")

def main():
    thiet_bi = lay_thiet_bi()
    if not thiet_bi:
        print("Không tìm thấy thiết bị.")
        return

    print("Danh sách thiết bị hiện có:")
    for tb in thiet_bi:
        print(f"Mã: {tb['id']}, Tên: {tb['name']}")

    # Ví dụ: Điều khiển một thiết bị cụ thể
    ma_thiet_bi = input("Nhập mã thiết bị để điều khiển: ")
    lenh = input("Nhập lệnh để gửi: ")
    dieu_khien_thiet_bi(ma_thiet_bi, lenh)

if __name__ == "__main__":
    main()
