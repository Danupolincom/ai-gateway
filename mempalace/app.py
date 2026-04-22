from fastapi import FastAPI
from pydantic import BaseModel
import os, json
from datetime import datetime

app = FastAPI(title="MemPalace")
DATA = "/data"
os.makedirs(DATA, exist_ok=True)

class AddReq(BaseModel):
    collection: str
    content: str

class SearchReq(BaseModel):
    collection: str
    query: str
    limit: int = 3

@app.post("/add")
def add(r: AddReq):
    p = f"{DATA}/{r.collection}.jsonl"
    with open(p, "a", encoding="utf-8") as f:
        f.write(json.dumps({"content": r.content, "ts": datetime.now().isoformat()}, ensure_ascii=False) + "\n")
    return {"ok": True}

@app.post("/search")
def search(r: SearchReq):
    p = f"{DATA}/{r.collection}.jsonl"
    if not os.path.exists(p):
        return {"results": []}
    q = r.query.lower()
    res = []
    with open(p, encoding="utf-8") as f:
        for line in reversed(list(f)):
            o = json.loads(line)
            if q in o["content"].lower():
                res.append(o)
            if len(res) >= r.limit:
                break
    return {"results": res}
