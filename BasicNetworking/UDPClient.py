import socket

target_host = "127.0.0.1"
target_port = 9997

# Socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data
client.sendto(b"AAABBBCCC", (target_host,target_port))

# Receive data
data,addr = client.recvfrom(4096)

print(data.decode())
client.close()