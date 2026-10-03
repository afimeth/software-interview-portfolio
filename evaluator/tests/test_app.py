import json, threading, unittest, urllib.request, urllib.error
from logic import create, complete, normalize
from server import make_server

class Domain(unittest.TestCase):
    def test_trim(self): self.assertEqual(normalize(' hello '), 'hello')
    def test_blank(self):
        with self.assertRaises(ValueError): normalize('   ')
    def test_type(self):
        with self.assertRaises(ValueError): normalize(7)
    def test_length(self):
        with self.assertRaises(ValueError): normalize('x'*121)
    def test_create(self): self.assertEqual(create([], 'a'), {'id':1,'title':'a','done':False})
    def test_complete(self):
        tasks=[];create(tasks,'a');self.assertTrue(complete(tasks,1)['done'])
    def test_unknown(self):
        with self.assertRaises(KeyError): complete([],1)

class HTTP(unittest.TestCase):
    def setUp(self):
        self.server=make_server();self.thread=threading.Thread(target=self.server.serve_forever,daemon=True);self.thread.start()
        self.url='http://127.0.0.1:'+str(self.server.server_port)
    def tearDown(self): self.server.shutdown();self.server.server_close();self.thread.join()
    def request(self,path,body=None):
        request=urllib.request.Request(self.url+path,data=None if body is None else body.encode(),headers={'Content-Type':'application/json'})
        try:
            with urllib.request.urlopen(request,timeout=2) as r: return r.status,r.read()
        except urllib.error.HTTPError as e: return e.code,e.read()
    def test_roundtrip(self):
        status,body=self.request('/tasks','{"title":"work"}');self.assertEqual(status,201)
        self.assertEqual(json.loads(body)['id'],1)
        self.assertEqual(self.request('/tasks/1/complete','{}')[0],200)
        self.assertTrue(json.loads(self.request('/tasks')[1])[0]['done'])
    def test_blank_rejected(self): self.assertEqual(self.request('/tasks','{"title":" "}')[0],400)
    def test_malformed(self): self.assertEqual(self.request('/tasks','{')[0],400)
    def test_unknown(self): self.assertEqual(self.request('/tasks/9/complete','{}')[0],404)
    def test_page(self):
        status,body=self.request('/');self.assertEqual(status,200);self.assertIn(b'li.textContent=task.title',body)

if __name__=='__main__': unittest.main()
