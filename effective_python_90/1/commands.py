#bytes to str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value #instance of str

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

#always returns bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of bytes
print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))

