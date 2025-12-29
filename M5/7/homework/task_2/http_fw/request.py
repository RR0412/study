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
        self.parse_body()

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

            header_name,header_value = header.split(': ', 1)
            self.headers[header_name.lower()] = header_value

    def read_line(self):
        return self.file.readline().decode().strip()
    
    def parse_body(self):
        if 'content-length' in self.headers:
            content_length = int(self.headers['content-length'])
            self.body = self.file.read(content_length).decode()
            self._parse_specific_body()

    def _parse_specific_body(self):
        if 'content-type' in self.headers:
            if self.headers['content-type'].lower() == 'application/x-www-form-urlencoded':
                self.body = parse_qs(self.body)

