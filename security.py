import zmq, zmq.auth
from zmq.auth.thread import ThreadAuthenticator

ctx = zmq.Context.instance()
auth = ThreadAuthenticator(ctx)
auth.start()
auth.allow("127.0.0.1")
auth.configure_curve(domain = "*", location = ".")
server = ctx.socket(zmq.REP)
server_public, server_secret = zmq.auth.load_certificate("server_transfer.key_secret")
server.curve_secretkey = server_secret
server.curve_publickey = server_public
server.curve_server = True
server.bind("tcp://*:8089")

users = {
    1: "Testing Software"
}

while True:
    authentication_data = server.recv().decode()

    if authentication_data in users.values():
        access = "success"
    else:
        access = "denied"

    print(access)

    server.send(access.encode())

auth.stop()
