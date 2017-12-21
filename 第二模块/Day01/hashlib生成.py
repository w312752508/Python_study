import hashlib
m = hashlib.md5()
m.update(b"hello")
print(m.hexdigest())
m.update(b"world")
print(m.hexdigest())

m2 = hashlib.md5()
m2.update("你好，世界".encode(encoding="utf-8"))
print(m2.hexdigest())
hashlib.sha512