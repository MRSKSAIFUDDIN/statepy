from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

public_key_pem = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAj6T+umGOoinEjOLWbaue
xAZEtyaOTrlnQNaamo3BMsCKOqk7QYtZxkbi2xiraP4Wtacx3QeWUgLHskiD7Sv6
BxvBX37YZ4d/hnKsY8THqzX8l6UgUBQTWgLL+x6AxCxh5hHWnF6ipnkogsKNr0A5
ip0TT5CmUmswPYsz3ABPTOJ9jbJLx+IjufGyq/o3W5XJ0yc82B+7QPj19CckLK26
rbh0EuZUOBcwRMiV+mOIADfk4DZyzVwNenN/K6D5ec/ylu6knpC4xl8n8wMyXuRu
WR0JpoPuDoocIBMakbVZBSH3QzN7LkjLgNXRQXw9fd4H40cW0xveyPcHH/OOVVxf
WwIDAQAB
-----END PUBLIC KEY-----"""

# Load the public key
public_key = serialization.load_pem_public_key(public_key_pem)

# The password to encrypt
password = b"StateJIT@123"

# Encrypt using RSA OAEP with SHA256
encrypted = public_key.encrypt(
    password,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Encode as Base64
encrypted_base64 = base64.b64encode(encrypted).decode()

print(encrypted_base64)
