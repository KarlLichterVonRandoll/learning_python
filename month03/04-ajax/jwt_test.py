import base64
import json
import time
import copy
import hmac


class Jwt:
    def __init__(self):
        pass

    @staticmethod
    def b64encode(content):
        return base64.urlsafe_b64encode(content).replace(b"=", b"")

    @staticmethod
    def b64decode(content):
        sem = len(content) % 4
        if sem > 0:
            content += b'=' * (4 - sem)

        return base64.urlsafe_b64decode(content)  # ??????

    @staticmethod
    def encode(payload, key, exp=300):
        # init header
        header = {'typ': 'JWT', 'alg': 'HS256'}
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        header_bs = Jwt.b64encode(header_json.encode())

        # init payload
        payload_self = copy.deepcopy(payload)

        if not isinstance(exp, int) and not isinstance(exp, str):
            raise TypeError('exp must be int or str!')
        payload_self['exp'] = time.time() + int(exp)
        payload_js = json.dumps(payload_self, separators=(',', ':'), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_js.encode())

        # init sign
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')

        sign_bs = Jwt.b64encode(hm.digest())

        return header_bs + b'.' + payload_bs + b'.' + sign_bs

    @staticmethod
    def decode(token, key):
        header_bs, payload_bs, sign_bs = token.split(b'.')

        if isinstance(key, str):
            key = key.encode()

        hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')

        if sign_bs != Jwt.b64encode(hm.digest()):
            raise ValueError('不匹配')

        payload_js = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_js)

        if 'exp' in payload:
            now = time.time()
            if now > payload['exp']:
                raise TimeoutError("过期啦")
        return payload


if __name__ == "__main__":
    token = Jwt.encode({'username': 'guoxiaonao'}, '12345', 300)
    print(token)

    payload = Jwt.decode(token, '12345')
    print(payload)
