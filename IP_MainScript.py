import requests
import platform
import socket

def get_ip_info(ip=""):
    """
    Fetches geolocation and network information for the given IP address.
    If no IP is provided, it fetches information for the user's own IP.
    """
    api_url = f"https://ipinfo.io/{ip}/json"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: Unable to fetch IP info (Status code: {response.status_code})")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_device_info():
    """
    Gathers basic device information like hostname, OS, and processor details.
    """
    device_info = {
        "Hostname": socket.gethostname(),
        "System": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return device_info

def display_info(ip_data, device_data):
    """
    Displays IP and device information in a readable format.
    """
    print("\nIP Address Information:")
    print("-" * 30)
    if ip_data:
        print(f"IP: {ip_data.get('ip', 'N/A')}")
        print(f"Hostname: {ip_data.get('hostname', 'N/A')}")
        print(f"City: {ip_data.get('city', 'N/A')}")
        print(f"Region: {ip_data.get('region', 'N/A')}")
        print(f"Country: {ip_data.get('country', 'N/A')}")
        print(f"Location: {ip_data.get('loc', 'N/A')}")
        print(f"Organization: {ip_data.get('org', 'N/A')}")
        print(f"Postal: {ip_data.get('postal', 'N/A')}")
        print(f"Timezone: {ip_data.get('timezone', 'N/A')}")
    else:
        print("No IP data available.")
    print("-" * 30)

    print("\nDevice Information:")
    print("-" * 30)
    for key, value in device_data.items():
        print(f"{key}: {value}")
    print("-" * 30)

def main():
    print("Welcome to the Enhanced IP & Device Info Script!")

    choice = input("Enter an IP address to lookup (leave blank to use your own IP): ").strip()
    ip_data = get_ip_info(choice)
    device_data = get_device_info()

    display_info(ip_data, device_data)

if __name__ == "__main__":
    main()
