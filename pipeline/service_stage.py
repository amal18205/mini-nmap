from scanner.banner import grab_banner


def detect_services(open_ports):

    results = []

    for item in open_ports:

        port = item["port"]
        sock = item["socket"]

        banner = grab_banner(sock, port)

        results.append({
            "port": port,
            "state": "OPEN",
            "banner": banner
        })

        sock.close()

    return results
