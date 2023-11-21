# DNS-Fixer
When nekoray isn't closed properly, it usually messes up /etc/resolv.conf file, so here is the lazy fix. 

## Creating Command in Linux
First store the script in a permanent location

Open terminal & type :
```
sudo nano .bashrc
```

edit the script path in the following command :
```
alias fixdns='sudo python3 [File path]/DNS\ Fixer.py'
```
Go to the end of bashrc file and Paste it.

Press CTRL+O to save and CTRL+X To exit.

Reboot and enjoy.

