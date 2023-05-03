import socket
import ipaddress
import os
import threading
import signal
import sys

os.system("title Made by eg4ar#7018")
print("Fast ip ranges scanner by eg4ar#7018, eg4ar.com")

port = int(input("Enter a port you want to scan: "))

def scan(ip_address, out_file):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        s.connect((str(ip_address), port))
        print(f"port {port} is openned on {ip_address}")
        out_file.write(str(ip_address) + '\n')
        out_file.flush()
        s.close()

    except (socket.timeout, ConnectionRefusedError):
        pass
    except socket.gaierror:
        print(f"can't resolve ip: {ip_address}")
        pass

def scan_range(start_ip, end_ip, out_file):
    threads = []
    for ip_int in range(int(start_ip), int(end_ip) + 1):
        ip_address = ipaddress.IPv4Address(ip_int)
        thread = threading.Thread(target=scan, args=(ip_address, out_file))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def sigint_handler(sig, frame):
    print('Program stopped by user')
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

with open('diapasons.txt', 'r') as f, open('output.txt', 'w') as out_file:
    for line in f:
        start_ip, end_ip = map(str.strip, line.split('-'))
        start_ip = ipaddress.IPv4Address(start_ip)
        end_ip = ipaddress.IPv4Address(end_ip)
        scan_range(start_ip, end_ip, out_file)