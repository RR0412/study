from os import fstat

class Response:
    HTTP_OK = 200
    HTTP_BAD_REQUEST = 400
    HTTP_NOT_FOUND = 404
    HTTP_INTERNAL_SERVER_ERROR = 500

    MESSAGES = {
        HTTP_OK: 'OK',
        HTTP_BAD_REQUEST: 'Bad Request',
        HTTP_NOT_FOUND: 'Not Found',
        HTTP_INTERNAL_SERVER_ERROR: 'Internal Server Error'
    }

    PROTOCOL = 'HTTP/1.1'


    def __init__(self, file):
        self.file = file
        self.status = self.HTTP_OK
        self.headers = []
        self.body = None
        self.file_body = None

    def add_header(self, name, value):
        self.headers.append({'name': name, 'value': value})

    def set_status(self, status):
        self.status = status
    
    def set_body(self,body):
        self.body = body.encode()
        self.add_header('Content-Length', len(self.body))


    def send(self):
        head = self._get_response_head()
        self.file.write(head)

        if self.body:
            self.file.write(self.body)
        elif self.file_body:
            self._write_file_body()

    def _get_status_line(self):
        message = self.MESSAGES[self.status]
        return f'{self.PROTOCOL} {self.status} {message}'
    
    def _get_response_head(self):
        status_line = self._get_status_line()

        head = [status_line]

        for header in self.headers:
            head.append(f'{header['name']}: {header['value']}')
        
        head_str = '\r\n'.join(head)
        head_str += '\r\n\r\n'

        return head_str.encode()
    
    def set_file_body(self,file) :
        self.file_body = file
        size = fstat(file.fileno()).st_size
        self.add_header('Content-Length', size)
    
    def _write_file_body(self):
        while True:
            data = self.file_body.read(1024)
            if not data:
                break
            self.file.write(data)
    










