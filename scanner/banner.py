import socket


def grab_banner(sock, port):

    try:

        # HTTP services
        if port == 80 or port == 8080:
            request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
            sock.send(request.encode())

        banner = sock.recv(1024)

        return banner.decode(errors="ignore").strip()

    except socket.timeout:
        return "No banner received"

    except Exception:
        return "Unable to grab banner"
