import sys


from pipeline.scan_pipeline import run_scan


# Vérification des arguments
if len(sys.argv) < 4:
    print(
        "Usage: python main.py <target_ip> "
        "<start_port> <end_port> "
        "[--threads number]"
    )
    exit()


target = sys.argv[1]

# Vérification des ports
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


# Valeur par défaut des threads
threads = 50


# Lecture de l'option --threads
if "--threads" in sys.argv:

    index = sys.argv.index("--threads")

    try:
        threads = int(sys.argv[index + 1])

    except (ValueError, IndexError):
        print("Error: threads must be a number")
        exit()


if threads <= 0:
    print("Error: threads must be greater than 0")
    exit()


print(
    f"Scanning {target} "
    f"from port {start_port} to {end_port}"
)
print(f"Using {threads} threads\n")


# Lancement du pipeline
results, open_ports, scan_duration, report_file, json_file = run_scan(
    target,
    start_port,
    end_port,
    threads
)


# Affichage des résultats

print("\n----------------------")
print("Scan Results")
print("----------------------\n")


for result in results:

    print(
        f"Port: {result['port']} | "
        f"State: {result['state']} | "
        f"Banner: {result['banner']}"
    )


print("\n----------------------")
print("Scan completed")
print(f"Open ports found: {open_ports}")
print(f"Scan duration: {scan_duration:.2f} seconds")
print(f"Report saved: {report_file}")
print(f"JSON report saved: {json_file}")
