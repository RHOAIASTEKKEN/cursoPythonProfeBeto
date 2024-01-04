import subprocess

redes = subprocess.run(["netsh","wlan","show","network"],
                       capture_output=True,text=True).stdout
ls=redes.split("\n")
ssids=[v.strip() for k, b in (p.split(':') for p in ls if 'SSID' in p)]

print(ssids)