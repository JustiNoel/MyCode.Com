import subprocess

def get_wifi_passwords():
    try:
        # Get the list of all Wi-Fi profiles stored on the device
        profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore")
        profiles = [line.split(":")[1].strip() for line in profiles_data.split('\n') if "All User Profile" in line]

        # Iterate through each profile and extract the password
        for profile in profiles:
            try:
                # Get the detailed information for the specific Wi-Fi profile
                profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="ignore")
                # Extract the password (Key Content)
                password = [line.split(":")[1].strip() for line in profile_info.split('\n') if "Key Content" in line]
                if password:
                    print(f"Wi-Fi Name: {profile} | Password: {password[0]}")
                else:
                    print(f"Wi-Fi Name: {profile} | Password: Not found")
            except subprocess.CalledProcessError:
                print(f"Wi-Fi Name: {profile} | Error: Unable to retrieve password")
            except Exception as e:
                print(f"Wi-Fi Name: {profile} | Error: {str(e)}")
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve Wi-Fi profiles. Make sure you run this script as Administrator.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("Retrieving Wi-Fi passwords for previously connected networks...\n")
    get_wifi_passwords()