import sys
import time
from scanner.tcp_scan import scan_port

if len(sys.argv) != 4:
    print("Usage: python main.py <target_ip> <start_port> <end_port>")
    exit()

target = sys.argv[1]
try :
   start_port = int(sys.argv[2])
   end_port = int(sys.argv[3])
except  ValueError:
   print("Error: ports must be numbers")
   exit()
if start_port < 1 or end_port > 65535:
    print("Error: Ports must be between 1 and 65535.")
    exit()

if start_port > end_port:
    print("Error: Start port must be less than or equal to end port.")
    exit()

print(f"Scanning {target} from port {start_port} to {end_port}\n")

open_ports = 0

start_time = time.time()

for port in range(start_port, end_port + 1):
    if scan_port(target, port):
        open_ports += 1
end_time = time.time()
scan_duration = end_time - start_time
print("\n----------------------")
print("Scan completed")
print(f"Open ports found: {open_ports}")
print(f"Scan duration: {scan_duration:.2f} seconds")
