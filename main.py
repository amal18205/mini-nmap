import sys

from pipeline.scan_pipeline import run_scan
from utils.formatter import print_results


if len(sys.argv) != 4:

    print("Usage: python main.py <target_ip> <start_port> <end_port>")
    exit()


target = sys.argv[1]

try:

    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

except ValueError:

    print("Error: ports must be numbers")
    exit()


if start_port < 1 or end_port > 65535:

    print("Error: Ports must be between 1 and 65535.")
    exit()


if start_port > end_port:

    print("Error: Start port must be less than or equal to end port.")
    exit()


print(f"Scanning {target} from port {start_port} to {end_port}\n")


results, open_ports, scan_duration, report_file, json_file = run_scan(
    target,
    start_port,
    end_port
)


print_results(results)


print("\nScan completed")
print(f"Open ports found: {open_ports}")
print(f"Scan duration: {scan_duration:.2f} seconds")
print(f"Report saved: {report_file}")
print(f"JSON report saved: {json_file}")
