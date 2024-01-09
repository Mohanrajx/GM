from sys_info.basic_info import get_basic_info
from sys_info.detailed_info import get_detailed_info
from sys_info.network_info import get_network_info

def display_system_info(basic_info, detailed_info, network_info):
    print("Basic System Information:")
    for key, value in basic_info.items():
        print(f"{key}: {value}")

    print("\nDetailed System Information:")
    for key, value in detailed_info.items():
        print(f"{key}: {value}")

    print("\nNetwork Information:")
    for key, value in network_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    try:
        basic_info = get_basic_info()
        detailed_info = get_detailed_info()
        network_info = get_network_info()
        display_system_info(basic_info, detailed_info, network_info)
    except Exception as e:
        print(f"An error occurred: {e}")
