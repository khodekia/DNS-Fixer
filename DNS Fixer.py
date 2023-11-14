import requests
import os

url = "https://www.google.com/"
timeout = 5
maindns =("8.8.8.8")
backupdns = ("8.8.8.4")

if os.geteuid() == 0:
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        print("Your DNS is probably Alright...")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("Possible DNS Failure!")
        print("Rewriting /etc/resolv.conf...")
        f = open('/etc/resolv.conf', 'r+')
        f.truncate(0)
        f.write("nameserver "+ maindns+"\nnameserver "+ backupdns)
        f.close()
        print("Good to Go...")
else:
    raise Exception("Please run this script with root Privileages.")