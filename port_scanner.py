import socket 

# some colors
class COLORS:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[31m'


host = '127.0.0.1'

def port_scan(port):
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
            return False
    else:
            return True
    finally:
        s.close()

def main():
    for portNumber in range(440,445):
        if port_scan(portNumber):
            print(f'{COLORS.RED} Port {portNumber} is open!')
        else:
            print(f'{COLORS.GREEN} Port {portNumber} is closed!')

main()
