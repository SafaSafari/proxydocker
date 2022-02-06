import requests, re
from type import *

class Proxydocker:
    def type(self, type):
        if '2' in type:
            return 'HTTPS'
        if '1' in type:
            return 'HTTP'
        if '4' in type:
            return 'SOCKS5'
        if '3' in type:
            return 'SOCKS4'
        if '5' in type:
            return 'CN25'
        if '6' in type:
            return 'CN80'
        return 'UNKNOWN'
    
    def anonymity(self, anonymity):
        if '1' in anonymity:
            return 'TRANSPARENT'
        if '2' in anonymity:
            return 'ANONYMOUS'
        if '3' in anonymity:
            return 'ELITE'
        return 'UNKNOWN'

    def __init__(self, config: config = config):
        self.config = config
    
    def run(self):
        with requests.session() as session:
            r = session.get('https://www.proxydocker.com/')
            token = re.search(r'<meta name="_token" content= "(.*)"', r.text).group(1)
            data = {'token': token, 'type': self.config.type, 'country': self.config.country, 'city': self.config.city, 'state': self.config.state, 'port': self.config.port, 'anonymity': self.config.anonymity, 'need': self.config.need, 'page': self.config.page}
            r = session.post('https://www.proxydocker.com/en/api/proxylist/', data)
            response = r.json()
            result = []
            for proxy in response['proxies']:
                result.append({'proxy': proxy['ip'] + ':' + str(proxy['port']), 'type': self.type(proxy['type']), 'isGoogle': proxy['isGoogle'], 'country': proxy['country'], 'country_code': proxy['code'], 'city': proxy['city'], 'timeout': proxy['timeout'], 'anonymity': self.anonymity(proxy['anonymity'])})
            return result

if __name__ == '__main__':
    print(Proxydocker().run())
