import socket
import time
import os

os.system("clear")

def timer(func):
    def wrapper(self):
        start_Time, template = func(self)
        print(template, time.time()-start_Time, "seconds.")
    return wrapper

class Socket:
    def __init__(self, **kwargs): # Kwargs takes arguments from socket.* [socket.AF_*, socket.SOCK_*]
        self.host = kwargs["host"]
        self.port = kwargs["port"]

        self.netType = (str(kwargs["netType"])).replace("AddressFamily.", "")
        self.conType = (str(kwargs["conType"])).replace("SocketKind.","")
        
        self.s = socket.socket(kwargs["netType"],kwargs["conType"])
    def __str__(self):
        return f"Network type is {self.netType} and connection type is {self.conType}"
    def __add__(self, other):
        print("Addition process cannot work with connections.")
    
    def connect(self):
        self.s.bind((self.host, self.port))
        self.s.listen()
        print(f"Listening on {self.host}:{self.port}")
        while True:
            self.client, self.address = self.s.accept()
            self.startTime = time.time()
            print(f"""
                  Connection successfully.\n
                  --------------------------------\n
                  | Client IP: {self.address[0]}\n
                  | Client PORT: {self.address[1]}\n
                  --------------------------------\n\n""")
            
            self.client.send("Test message.".encode())
            self.close()
            break
    @timer
    def close(self):
        self.client.close()
        return self.startTime, f"""
        [I] Connection closed.\n
        [I] Total session time """

socket1 = Socket(netType=socket.AF_INET, conType=socket.SOCK_STREAM, host="127.0.0.1", port=55555)
socket1.connect()