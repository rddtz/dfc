import socket
import ssl
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("What is the host? ")
dirs = input("Dirs you wanna search separated by / : ")

dirs = dirs.split("/")

hIP = socket.gethostbyname(host)

try:
    skt.connect((hIP, 443))
    skt = ssl.wrap_socket(skt, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
except:
    try:
        skt.connect((hIP, 80))
    except:
        print("Erro ao conectar")

print(f'Connected to {host}...')

print(skt)
print(" ")

for i in dirs:
    cmd = f'HEAD /{i}/ HTTP/1.1\r\nHost: {host}\r\n\r\n'.encode()

    print(cmd)
    print(" ")

    skt.send(cmd)


    data = skt.recv(1024)

    print(data.decode(),end='')
    print("\n ------------------------------------------------- \n")
skt.close()
