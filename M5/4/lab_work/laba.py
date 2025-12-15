import random
import socketserver
from request import Request

ADDRESS = ('localhost',3333)
SECRET_NUMBERS = [6, 1, 9, 7]
socketserver.TCPServer.allow_reuse_address = True


class Handler(socketserver.StreamRequestHandler):
    def get(self):
        return(
            '<p>Guess 4 numbers.Enter the separated with spaces:</p>'
            '<form method="POST" action="/">' 
            '<input type="text" name="numbers"/>'
            '<input type="submit" value="Send"/>'
            '</form>'
        )
    

    def convers_numbers(self, numbers: list[str]) -> list[int]:
        split_numbers = numbers[0].split()
        return [int(num) for num in split_numbers]


    def post(self, request):
        numbers = request.body['numbers']
        numbers = self.convers_numbers(numbers)
        error = self.check_len(numbers)
        if error:
            return error
        error = self.check_value(numbers)
        if error:
            return error
        
        bulls = self.bulls(numbers)
        matches = self.matches(numbers)
        cows = self.cows(matches,bulls)
        return self.win(bulls,cows)


    def check_len(self,numbers):
        if len(numbers) != 4 :
            return(
            '<p>Guess 4 numbers.Enter the separated with spaces:</p>'
            '<form method="POST" action="/">' 
            '<input type="text" name="numbers"/>'
            '<input type="submit" value="Send"/>'
            '</form>'
            f'<p>Cows: 0, Bulls: 0</p>'
            '<p>Wrong amount of numbers entered. Should be 4!'
        )

    def check_value(self,numbers):
        for number in numbers:
            if number > 9 or number < 1:
                return(
                '<p>Guess 4 numbers.Enter the separated with spaces:</p>'
                '<form method="POST" action="/">' 
                '<input type="text" name="numbers"/>'
                '<input type="submit" value="Send"/>'
                '</form>'
                f'<p>Cows: 0, Bulls: 0</p>'
                '<p>Wrong value of number. Number must be between 1 and 9.'
            )

    def bulls(self,numbers):
        bulls = 0
        for i in range(len(SECRET_NUMBERS)):
            if SECRET_NUMBERS[i] == numbers[i]:
                bulls += 1
        return bulls

    def matches(self,numbers):
        matches = 0
        for numberS in SECRET_NUMBERS:
            for numberN in numbers:
                if numberS == numberN:
                    matches += 1
        return matches 
    
    def cows(self,matches,bulls):
        return matches - bulls




    def win(self,bulls,cows):
        if bulls == 4:
            return(
            '<p>Guess 4 numbers.Enter the separated with spaces:</p>'
            '<form method="POST" action="/">' 
            '<input type="text" name="numbers"/>'
            '<input type="submit" value="Send"/>'
            '</form>'
            f'<p>Cows: {cows}, Bulls: {bulls}</p>'
            '<p>Congratulation, you won!'
        )
        else:
            return('<p>Guess 4 numbers.Enter the separated with spaces:</p>'
            '<form method="POST" action="/">' 
            '<input type="text" name="numbers"/>'
            '<input type="submit" value="Send"/>'
            '</form>'
            f'<p>Cows: {cows}, Bulls: {bulls}</p>'
            )

    
    def handle(self):
        request = Request(self.rfile)
        print('Method: ', request.method)
        print('Uri: ', request.uri)
        print('Protocol:', request.protocol)
        print('Headers', request.headers)
        print('Body', request.body)

        if request.method == 'GET' : 
            response_body = self.get()
        elif request.method == 'POST' :
            response_body = self.post(request)
        else:
            response_body = '<h1>Wrong method!</h1>'
        

        body_bytes = response_body.encode('utf-8')
        content_length = len(body_bytes)

        headers = [
            'HTTP/1.1 200 OK',
            'Content-Type: text/html',
            f'Content-Length:{content_length}',
            'Connection: close',
            '',
        ]

        headers_bytes = '\r\n'.join(headers).encode('utf-8') + b'\r\n'
        self.wfile.write(headers_bytes)
        self.wfile.write(body_bytes)  



    
with socketserver.ThreadingTCPServer(ADDRESS, Handler) as server:
    server.serve_forever()