import subprocess
s = subprocess.getstatusoutput('netsh interface ip show address "Wi-Fi" | findstr "IP Address"')
lis = s[1].split()
print(lis[2])
