from scanner.tcp_scan import scan_port


def discover_ports(target, start_port, end_port):

    open_ports = []

    for port in range(start_port, end_port + 1):

        is_open, sock = scan_port(target, port)

        if is_open:

            open_ports.append({
                "port": port,
                "socket": sock
            })

        else:
            pass

    return open_ports
