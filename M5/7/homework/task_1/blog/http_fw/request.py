from urllib.parse import urlparse,parse_qs

class Request:
    def __init__(self,file):
        self.file = file
        self.method = ''
        self.uri = ''
        self.protocol = ''
        self.headers = {}
        self.body = {}
        self.query = {}
        self.parse_request_line()
        self.parse_headers()

    def parse_request_line(self):
        request_line = self.read_line()
        self.method, self.uri, self.protocol = request_line.split(' ')

        if self.protocol != 'HTTP/1.1':
            raise ValueError('Wrong protocol')
        
        parsed = urlparse(self.uri)
        self.uri = parsed.path
        self.query = parse_qs(parsed.query)
        
    def parse_headers(self):
        while True:
            header = self.read_line()

            if header == '':
                break

            if ': ' in header:
                key,value = header.split(': ', 1)
                self.headers[key.lower()] = value

    def read_line(self):
        return self.file.readline().decode().strip()
    
    def parse_body(self):
        print("Headers:", self.headers)
        if 'content-length' in self.headers:
            content_length = int(self.headers['content-length'])
            raw = self.file.read(content_length)
            self.body = raw.decode()
            self._parse_specific_body()

    def _parse_specific_body(self):
        if 'content-type' in self.headers:
            if self.headers['content-type'] == 'application/x-www-form-urlencoded':
                self.body = parse_qs(self.body)

