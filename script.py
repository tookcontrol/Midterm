from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
import os

parameters = dh.generate_parameters(generator=2, key_size=2048)

alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()
alice_public_bytes = alice_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()
bob_public_bytes = bob_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

alice_shared_key = alice_private_key.exchange(bob_public_key)
bob_shared_key = bob_private_key.exchange(alice_public_key)

print("Alice's public key:")
print(alice_public_bytes.decode())
print("\nBob's public key:")
print(bob_public_bytes.decode())
print("\nAlice's shared secret (first 10 bytes):")
print(alice_shared_key[:10].hex())
print("\nBob's shared secret (first 10 bytes):")
print(bob_shared_key[:10].hex())

print("\nShared secrets match:", alice_shared_key == bob_shared_key)
