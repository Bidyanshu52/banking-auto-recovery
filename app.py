from flask import Flask, jsonify
from datetime import datetime, timezone
import os, time

app = Flask(__name__)
STARTED_AT = time.time()
VERSION = os.getenv("APP_VERSION", "1.0")

def utc_now():
    return datetime.now(timezone.utc).isoformat()

@app.get("/")
def home():
    return jsonify({
        "project": "Banking Service Availability Demo",
        "status": "UP",
        "version": VERSION,
        "uptime_seconds": round(time.time() - STARTED_AT, 1),
        "timestamp_utc": utc_now()
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy", "timestamp_utc": utc_now()}), 200

@app.post("/crash")
def crash():
    # Demo-only endpoint: intentionally terminates this process to test recovery.
    print(f"SIMULATED_CRASH timestamp_utc={utc_now()}", flush=True)
    os._exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
