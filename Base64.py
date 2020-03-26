import base64

print(base64.b64decode('bWNkb3Y0ZXI5bGwxIXNz'.encode('utf-8')))
print(base64.b64decode(b'bWNkb3Y0ZXI5bGwxIXNz'))  # same as above

print(base64.b64encode(b'mcinventoryv4er9ll1!ss'))
