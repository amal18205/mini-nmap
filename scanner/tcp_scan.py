import socket


def scan_port(target, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(2)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            return True, sock

        else:
            sock.close()
            return False, None

    except socket.error:
        sock.close()
        return False, None
