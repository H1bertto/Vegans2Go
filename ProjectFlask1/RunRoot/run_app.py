from Project.root_app import app
import socket
import os

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', str(socket.gethostbyname(socket.gethostname())))
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
