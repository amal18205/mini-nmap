import sys
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

for port in range(start_port, end_port + 1):
    scan_port(target, port)
