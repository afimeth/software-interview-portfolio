import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from logic import create, complete

def make_server(port=0):
    tasks, lock = [], Lock()
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args): pass
        def send(self, status, value, kind='application/json'):
            body = value if isinstance(value, bytes) else json.dumps(value).encode()
            self.send_response(status)
            self.send_header('Content-Type', kind)
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        def do_GET(self):
            if self.path == '/':
                return self.send(200, Path(__file__).with_name('index.html').read_bytes(), 'text/html; charset=utf-8')
            if self.path == '/tasks':
                with lock: self.send(200, tasks)
            else: self.send(404, {'error': 'not found'})
        def do_POST(self):
            try:
                size = int(self.headers.get('Content-Length', '0'))
                if not 0 < size <= 4096: raise ValueError('body size')
                payload = json.loads(self.rfile.read(size))
                if not isinstance(payload, dict): raise ValueError('object required')
                with lock:
                    if self.path == '/tasks':
                        result, status = create(tasks, payload.get('title')), 201
                    elif self.path.startswith('/tasks/') and self.path.endswith('/complete'):
                        result, status = complete(tasks, int(self.path.split('/')[2])), 200
                    else: return self.send(404, {'error': 'not found'})
                    self.send(status, result)
            except KeyError: self.send(404, {'error': 'unknown task'})
            except (ValueError, TypeError): self.send(400, {'error': 'invalid input'})
    return ThreadingHTTPServer(('127.0.0.1', port), Handler)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(); parser.add_argument('--port', type=int, default=8080)
    make_server(parser.parse_args().port).serve_forever()
