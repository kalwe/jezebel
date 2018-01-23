class Client(object):

    is_connected = False

    def __init__(self):
        print("api client")

    def restart(self):
        print("restarting api connection...")

    def connect(self):
        if self.is_connected:
            return True
