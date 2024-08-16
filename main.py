import requests

# URL máy chủ quản lý thiết bị và điều khiển
server_url = "http://demluottruycap.atwebpages.com/devices"
control_url_template = "http://demluottruycap.atwebpages.com/control/{device_id}"

def lay_thiet_bi():
    """
    Lấy danh sách thiết bị từ máy chủ.
    """
    try:
        response = requests.get(server_url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        thiet_bi = response.json().get('devices', [])
        return thiet_bi
    except requests.RequestException as e:
        print(f"Lỗi khi lấy danh sách thiết bị: {e}")
        return []

def dieu_khien_thiet_bi(ma_thiet_bi, lenh):
    """
    Gửi lệnh điều khiển đến một thiết bị cụ thể.
    """
    try:
        control_url = control_url_template.format(device_id=ma_thiet_bi)
        payload = {'command': lenh}
        response = requests.post(control_url, json=payload)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        print(f"Phản hồi điều khiển: {response.status_code}")
    except requests.RequestException as e:
        print(f"Lỗi khi gửi lệnh điều khiển: {e}")

def main():
    """
    Chương trình chính để lấy danh sách thiết bị và gửi lệnh điều khiển.
    """
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
