from base import UdpClient

if __name__ == '__main__':

    host = "192.168.*.*"  # IP of the server or host.
    port = 13000

    # By default, exit_code is "exit", you can choose any string as exit_code.
    # Upon receiving this exit code, connection will be closed.
    client = UdpClient(host=host, port=port, exit_code="stop")

    # You will not see "no-msg" on the server, since client closes connection
    # upon reading "exit".
    random_message_list = ["hi", "hello", "world", "python", "socket", "exit", "no-msg"]

    for msg in random_message_list:
        client.send_data(msg)
