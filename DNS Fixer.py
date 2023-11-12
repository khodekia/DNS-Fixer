import requests
import os
#at the moment this code only checks if it is running with root privileges and checks your internet connection
url = "https://www.google.com/"
timeout = 5


if os.geteuid() == 0:
    try:
        request = requests.get(url, timeout=timeout)
        print(request)
        print("Connected to the Internet")
        #this code is not completed it will be updated with a working cod
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")

else:
    print("Please run this script with root Privileages.")
