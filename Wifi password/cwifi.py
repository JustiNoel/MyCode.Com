import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore')
profiles = [i.split(":")[1][1:-1] for i in data.split('\n') if "All User Profile" in i]

for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors='ignore')
        results = [b.split(":")[1][1:-1] for b in results.split('\n') if "Key Content" in b]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print("{:<30}|  {:<}".format(i, "ENCODING ERROR"))

input("Press Enter to exit...")
