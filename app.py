import sqlite3
from datetime import datetime, timezone
from flask import Flask, jsonify, request, render_template
app=Flask(__name__); DB="threat_intel.db"
def db():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def init():
 c=db(); c.execute("""CREATE TABLE IF NOT EXISTS iocs(id INTEGER PRIMARY KEY, type TEXT NOT NULL, value TEXT NOT NULL UNIQUE, source TEXT, confidence INTEGER DEFAULT 50, created_at TEXT NOT NULL)"""); c.commit(); c.close()
@app.get("/")
def home(): return render_template("index.html")
@app.get("/api/iocs")
def list_iocs():
 c=db(); rows=c.execute("SELECT * FROM iocs ORDER BY id DESC").fetchall(); c.close(); return jsonify([dict(r) for r in rows])
@app.post("/api/iocs")
def add_ioc():
 d=request.get_json(silent=True) or {}; typ=str(d.get("type","")).strip().lower(); val=str(d.get("value","")).strip()
 if typ not in {"ip","domain","url","hash","email"} or not val: return jsonify(error="type and value are required"),400
 try:
  c=db(); c.execute("INSERT INTO iocs(type,value,source,confidence,created_at) VALUES(?,?,?,?,?)",(typ,val,str(d.get("source","manual"))[:100],max(0,min(100,int(d.get("confidence",50)))),datetime.now(timezone.utc).isoformat())); c.commit(); c.close(); return jsonify(success=True),201
 except sqlite3.IntegrityError: return jsonify(error="IOC already exists"),409
if __name__=="__main__": init(); app.run(debug=True)