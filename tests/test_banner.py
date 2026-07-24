import socket
import threading

from scanner.banner import grab_banner


def banner_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind(
        ("127.0.0.1", 9997)
    )

    server.listen(1)

    client, address = server.accept()

    client.send(
        b"TEST-SERVER-1.0"
    )

    client.close()
    server.close()


def test_banner():

    thread = threading.Thread(
        target=banner_server
    )

    thread.start()

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.connect(
        ("127.0.0.1", 9997)
    )

    banner = grab_banner(
        sock,
        9997
    )

    assert "TEST-SERVER" in banner

    sock.close()

    thread.join()
