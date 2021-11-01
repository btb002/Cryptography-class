from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import codecs

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
data=b'bots are stupids'
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()

print(key)