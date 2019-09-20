import abc
from socket import socket, AF_INET, SOCK_DGRAM


class UdpServerBase(abc.ABC):
    def __init__(self, host="", port=13000, buffer_size=1024, exit_command="exit"):
        self.__host = host
        self.__port = port
        self.__buffer_size = buffer_size
        self.__exit_command = exit_command
        self.__udp_socket = None

        self.__bind_socket()

    def __bind_socket(self):
        self.__udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.__udp_socket.bind((self.__host, self.__port))

        while True:
            (data_bytes, address_tuple) = self.__udp_socket.recvfrom(self.__buffer_size)
            address, port = address_tuple
            str_data = data_bytes.decode("utf-8")
            self.on_data_received(address, port, data_bytes, str_data)

            if str_data == self.__exit_command:
                self.__udp_socket.close()
                break

    @abc.abstractmethod
    def on_data_received(self, address, port, byte_data, str_data):
        """
        Callback for on data received.


        :param address: Host address from where the request came from
        :type address: str
        :param port: Port
        :type: int
        :param byte_data: The actual data received in byte format
        :type byte_data: byte
        :param str_data: The received data encoded as a string.
        :type str_data: str
        :return: None
        """
        pass


class UdpClient(object):
    def __init__(self, host, port, exit_code="exit"):
        self.__host = host
        self.__port = port
        self.__exit_code = exit_code
        self.__udp_socket = None
        self.__bind()

    def __bind(self):
        self.__udp_socket = socket(AF_INET, SOCK_DGRAM)

    def send_data(self, str_data):
        self.__udp_socket.sendto(str_data.encode(), (self.__host, self.__port))

        if str_data == self.__exit_code:
            self.__udp_socket.close()
