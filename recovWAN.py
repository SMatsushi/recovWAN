#!/usr/bin/env python3

import datetime as dt
from pythonping import ping
import subprocess

##             Google DNS, Cloud flre
ping_hosts = ['8.8.8.8', '1.1.1.1'] # for production
#ping_hosts = ['8.8.8.0', '1.1.1.1'] # first fail
#ping_hosts = ['8.8.8.0', '1.1.0.5'] # fail all

WAN_port = "enp1s0"
ifdown = f"/usr/sbin/ifdown {WAN_port}"
ifup = f"/usr/sbin/ifup {WAN_port}"

print(dt.datetime.now().strftime('%y/%m/%d %H:%M:%S - ping '), end="")
for i,h in enumerate(ping_hosts):
    r = ping(h, verbose=1, count=1)
    if r.success():
        print(f" {i:02}: {h} Success. exit.")
        exit(0)
    print(f" {i:02}: {h} {r.success()} Continue.")

cmd = f"{ifdown} && sleep 10 && {ifup}"
print(f"Rebooting WAN {WAN_port} with '{cmd}'...")
# print(cmd)
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# wait proc done
for ln in iter(proc.stdout.readline,b''):
    print(ln.rstrip().decode("utf8"))

# proc.wait()
# print(proc.stdout.decode('utf8'))
