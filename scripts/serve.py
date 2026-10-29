"""Servidor somente local para catálogo e exemplos; não publica o projeto."""
import argparse,http.server,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import unquote,urlparse
        parts=pathlib.PurePosixPath(unquote(urlparse(self.path).path)).parts
        if any(p.startswith(".")for p in parts if p not in ["/",""]):self.send_error(404);return
        return super().do_GET()
    def log_message(self,*args):pass
def main():
    import functools
    p=argparse.ArgumentParser();p.add_argument("--port",type=int,default=8769);a=p.parse_args()
    with http.server.ThreadingHTTPServer(("127.0.0.1",a.port),functools.partial(Handler,directory=str(ROOT)))as server:
        print("Catálogo: http://127.0.0.1:"+str(a.port)+"/catalogo/",flush=True);server.serve_forever()
if __name__=="__main__":main()
