import hashlib

SALT = 'linkfqy'


def md5(data):
    m = hashlib.md5()
    b = data.encode(encoding='utf-8')
    m.update(b)
    return m.hexdigest()


def saltify(password):
    return md5(password+SALT)
