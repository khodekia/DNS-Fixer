import requests
import os

url = "https://www.google.com/"
timeout = 5


if os.geteuid() == 0:
    try:
        request = requests.get(url, timeout=timeout)
        print(request)
        print("Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")

else:
    print("Please run this script with root Privileages.")