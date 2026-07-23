import sys, json, base64, time
import websocket, urllib.request

def targets():
    d = json.load(urllib.request.urlopen("http://127.0.0.1:9222/json"))
    return d

def page_ws(match=None):
    for t in targets():
        if t.get("type")=="page" and t.get("webSocketDebuggerUrl"):
            if match is None or (match in (t.get("url") or "")):
                return t["webSocketDebuggerUrl"], t["url"]
    # fallback: first page
    for t in targets():
        if t.get("type")=="page" and t.get("webSocketDebuggerUrl"):
            return t["webSocketDebuggerUrl"], t["url"]
    raise RuntimeError("no page target")

class CDP:
    def __init__(self, ws_url):
        self.ws = websocket.create_connection(ws_url, max_size=None, timeout=120)
        self.id = 0
    def cmd(self, method, params=None):
        self.id += 1; mid=self.id
        self.ws.send(json.dumps({"id":mid,"method":method,"params":params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id")==mid:
                if "error" in msg: raise RuntimeError(method+": "+json.dumps(msg["error"]))
                return msg.get("result",{})
    def eval(self, expr, awaitp=False):
        r = self.cmd("Runtime.evaluate", {"expression":expr,"returnByValue":True,"awaitPromise":awaitp})
        if "exceptionDetails" in r:
            return {"__exc__": json.dumps(r["exceptionDetails"])[:300]}
        return r.get("result",{}).get("value")
    def screenshot(self, path):
        r = self.cmd("Page.captureScreenshot", {"format":"png"})
        data = base64.b64decode(r["data"])
        open(path,"wb").write(data)
        return len(data)
    def key(self, name):
        M={"Escape":(27,"Escape"),"Space":(32,"Space"),"Enter":(13,"Enter")}
        vk,code=M[name]; txt=" " if name=="Space" else ""
        for t in ("keyDown","keyUp"):
            p={"type":t,"windowsVirtualKeyCode":vk,"nativeVirtualKeyCode":vk,"key":(" " if name=="Space" else name),"code":code}
            if t=="keyDown" and txt: p["text"]=txt
            self.cmd("Input.dispatchKeyEvent",p); time.sleep(0.03)
    def click(self, x, y):
        for t in ("mouseMoved","mousePressed","mouseReleased"):
            p={"type":t,"x":x,"y":y,"button":"left","buttons":1,"clickCount":1}
            self.cmd("Input.dispatchMouseEvent", p)
            time.sleep(0.03)

def main():
    a = sys.argv[1:]
    match = None
    # optional --match <substr>
    if a and a[0]=="--match":
        match=a[1]; a=a[2:]
    ws_url,url = page_ws(match)
    c = CDP(ws_url)
    c.cmd("Page.enable"); c.cmd("Runtime.enable")
    op = a[0] if a else "info"
    if op=="info":
        print(json.dumps({"url":url}))
    elif op=="eval":
        print(json.dumps(c.eval(a[1], awaitp=("--await" in a))))
    elif op=="screenshot":
        n=c.screenshot(a[1]); vp=c.eval("JSON.stringify({iw:innerWidth,ih:innerHeight,dpr:devicePixelRatio})")
        print(json.dumps({"bytes":n,"viewport":vp}))
    elif op=="key":
        c.key(a[1]); print("key",a[1])
    elif op=="click":
        c.click(float(a[1]), float(a[2])); print("clicked",a[1],a[2])
    elif op=="navigate":
        c.cmd("Page.navigate",{"url":a[1]}); print("navigated",a[1])
    else:
        print("unknown op", op)

if __name__=="__main__":
    main()
