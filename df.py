import socket
import ssl


def request(skt, i, host):
    cmd = f'HEAD /{i} HTTP/1.1\r\nHost: {host}\r\n\r\n'.encode()

    print(f"\nSending request: {cmd}\n")
    skt.send(cmd)

    data = b''
    while b'\r\n\r\n' not in data:
        data += skt.recv(1024)

    data = data.decode()
    status = data[:25]

    if '301' in status:
        redirect = data.split('\n')

        x = 0
        while 'Location' not in redirect[x]:
            x += 1
        redirect = redirect[x]

        for l in range(2):
            finder = redirect.find(':')
            redirect = redirect[finder + 1:]

        redirect = redirect[2:len(redirect) - 2]
        print(redirect)

        tempskt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tempskt.connect((socket.gethostbyname(redirect), 443))
        tempskt = ssl.wrap_socket(tempskt, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)

        request(tempskt, i, redirect)
        tempskt.close()
    else:
        print(data)



#----------------------------------------

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("What is the host? ")
dirs = input("Dirs you wanna search separated by ; : ")

dirs = dirs.split(";")


try:
    hIP = socket.gethostbyname(host)
except:
    try:
        if 'www' not in host:
            host = f'www.{host}'
            hIP = socket.gethostbyname(host)
    except:
        print("Erro ao conectar ao host.")

try:
    skt.connect((hIP, 443))
    skt = ssl.wrap_socket(skt, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
except:
    try:
        skt.connect((hIP, 80))
    except:
        print("Erro ao conectar")

print(f'\nConnected to {host} at {hIP}')

for i in dirs:
    request(skt, i, host)

skt.close()
