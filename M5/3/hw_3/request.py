class Request:
    def __init__(self,file):
        self.file = file

        self.method = ''
        self.uri = ''
        self.protocol = ''
        self.headers = {}

        self.parse_request_line()
        self.parse_headers()
        self.parse_body()

    def parse_request_line(self):
        request_line = self.read_line()
        self.method, self.uri, self.protocol = request_line.split(' ')

        if self.protocol != 'HTTP/1.1':
            raise ValueError('Wrong protocol')
        
    def parse_headers(self):
        while True:
            header = self.read_line()

            if header == '':
                break

            header_name,header_value = header.split(': ')
            self.headers[header_name] = header_value

    def read_line(self):
        return self.file.readline().decode().strip()
    
    def parse_body(self):
        if 'Content-Length' in self.headers:
            content_length = int(self.headers['Content-Length'])
            self.body = self.file.read(content_length)


