import socket

#target_host = "www.google.com"
#target_port = 80

target_host = "127.0.0.1"
target_port = 9998

# Socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect client
client.connect((target_host,target_port))

# Send some test data
#client.send(b"GET / HTTP/1.1 \r\nHost: testing.com\r\n\r\n")
client.send(b'Derka derka')


# Receive some data
response = client.recv(4096)

print(response.decode())

client.close()