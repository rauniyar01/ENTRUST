import os
import sys

def run_ping(ip_address):
    # WARNING: This command is vulnerable to injection!
    command = f"ping -c 2 {ip_address}"
    os.system(command)  # Directly passes user input to the system shell

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 vulnerable_script.py <IP address>")
        sys.exit(1)

    ip = sys.argv[1]
    run_ping(ip)