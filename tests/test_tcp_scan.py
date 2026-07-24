import socket
import threading

from scanner.tcp_scan import scan_port


def start_test_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind(
        ("127.0.0.1", 9998)
    )

    server.listen(1)

    connection, address = server.accept()

    connection.close()

    server.close()


def test_closed_port():

    result, sock = scan_port(
        "127.0.0.1",
        9999
    )

    assert result is False


def test_open_port():

    thread = threading.Thread(
        target=start_test_server
    )

    thread.start()

    result, sock = scan_port(
        "127.0.0.1",
        9998
    )

    assert result is True

    sock.close()

    thread.join()
