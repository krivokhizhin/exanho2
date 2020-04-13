import hmac
import os

def client_authenticate(connection, secret_key, algorithm = 'sha256'):
    message = connection.recv(32)
    digest = hmac.digest(secret_key, message, algorithm)
    connection.send(digest)

def server_authenticate(connection, secret_key, algorithm = 'sha256'):
    message = os.urandom(32)
    connection.send(message)
    digest = hmac.digest(secret_key, message, algorithm)
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest,response)