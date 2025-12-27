def not_found(request, response):
    response.set_status(404)
    response.add_header('Content-Type', 'text/html')
    response.set_body('<h1>404 Not found</h1>')

def internal_server_error(request, response):
    response.set_status(500)
    response.add_header('Content-Type', 'text/html')
    response.set_body('<h1>Oops, something went wrong... </h1>')