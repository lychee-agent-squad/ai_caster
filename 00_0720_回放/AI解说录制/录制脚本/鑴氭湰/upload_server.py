import http.server, socketserver, os
from urllib.parse import urlparse, parse_qs
PORT=8091
OUTDIR=os.environ.get("REC_OUT","/tmp/rec")
os.makedirs(OUTDIR, exist_ok=True)
class H(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Methods','POST,OPTIONS')
        self.send_header('Access-Control-Allow-Headers','*')
    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()
    def do_POST(self):
        q=parse_qs(urlparse(self.path).query)
        name=os.path.basename(q.get('name',['rec.webm'])[0])
        reset=q.get('reset',['0'])[0]=='1'
        n=int(self.headers.get('Content-Length',0))
        data=self.rfile.read(n)
        path=os.path.join(OUTDIR,name)
        with open(path,'wb' if reset else 'ab') as f: f.write(data)
        self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(b'ok')
    def log_message(self,*a): pass
socketserver.ThreadingTCPServer.allow_reuse_address=True
print(f"upload server on :{PORT} -> {OUTDIR}", flush=True)
socketserver.ThreadingTCPServer(("127.0.0.1",PORT),H).serve_forever()
