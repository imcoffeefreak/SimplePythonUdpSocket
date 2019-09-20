from base import UdpServerBase


class RealServer(UdpServerBase):
    def on_data_received(self, address, port, byte_data, str_data):
        # Implement your logic here.
        # This is the part which receives data.
        msg = "Received from: {0}, port: {1}. Data: {2}"
        print(msg.format(address, port, str_data))


if __name__ == '__main__':
    real_server = RealServer()
