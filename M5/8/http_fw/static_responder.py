from glob import glob
import os
import mimetypes

class StaticResponder:
    def __init__(self, request,response, static_dir):
        self.request = request
        self.response = response
        self.static_dir = static_dir
        self.file = None
        self._check_file()

    def _check_file(self):
        file_uri = self.request.uri.lstrip('/').replace('..', '')
        if not file_uri.startswith('static/'):
            return
        relative_path = file_uri[len('static/'):]
        path = os.path.join(self.static_dir, relative_path)

        if os.path.isfile(path):
            self.file = path

    def prepare_response(self):
        if self.file:
            f = open(self.file, 'rb')
            self.response.set_file_body(f)

            content_type, _ = mimetypes.guess_type(self.file)
            self.response.add_header('Content-Type', content_type or 'application/octet-stream')
            self.response.add_header('Connection', 'close')
            self.response.set_status(200)

