import hashlib

print(hashlib.algorithms_available)

filename = input("Enter the input file name: ")
sha256 = hashlib.sha256()
with open(filename, "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256.update(byte_block)
    print(sha256.hexdigest())
