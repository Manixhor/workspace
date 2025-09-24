import socket

host_name = socket.gethostname()

ip_address = socket.gethostbyname(host_name)

print(host_name)
print(ip_address)