import zmq.auth

server_public_file, server_secret_file = zmq.auth.create_certificates(
    ".", "server_transfer"
)
client_public_file, client_secret_file = zmq.auth.create_certificates(
    ".", "client_transfer"
)