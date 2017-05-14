# ################# Start the server and listen for connections ########################################################

from face import FaceCube
import sockets
import sys
import solver as sv


if __name__ == '__main__':  # file is executed
    if len(sys.argv) < 2:
        sys.argv.append(str(8080))  # Port 8080 default port
    print('startserver')
    sockets.server_start(sys.argv)
else:
    def start(port):
        sockets.server_start((-1, port))
