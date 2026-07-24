from scanner.tcp_scan import scan_port
from concurrent.futures import ThreadPoolExecutor


def scan_single_port(target, port):

    is_open, sock = scan_port(target, port)

    if is_open:

        return {
            "port": port,
            "socket": sock
        }

    return None



def discover_ports(target, start_port, end_port, threads):

    open_ports = []

    ports = range(start_port, end_port + 1)


    with ThreadPoolExecutor(max_workers=threads) as executor:

        results = executor.map(
            lambda port: scan_single_port(target, port),
            ports
        )


        for result in results:

            if result:

                open_ports.append(result)


    return open_ports
