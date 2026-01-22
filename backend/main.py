from fastapi import FastAPI
app = FastAPI(title="SmartHome Dashboard API")

@app.get("/health")
def health():
    return {"status": "ok"}
