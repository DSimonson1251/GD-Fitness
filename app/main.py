
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="GD-Fitness", version="0.1")

# Serve static files (CSS, images, etc.)
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    html = """
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>GD-Fitness</title>
            <meta name="viewport" content="width=device-width,initial-scale=1" />
            <style>
      body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:0;padding:0;background:#f7fafc;color:#0f172a}
      .navbar{background:#fff;padding:16px 40px;box-shadow:0 2px 8px rgba(2,6,23,0.06);display:flex;align-items:center}
      .logo{height:50px;margin-right:20px}
      .content{margin:40px;max-width:720px}
      .card{background:#fff;padding:24px;border-radius:8px;box-shadow:0 4px 20px rgba(2,6,23,0.08)}
      a{color:#0369a1}
    </style>
  </head>
  <body>
    <div class="navbar">
      <img src="/static/logo.png" alt="GD-Fitness" class="logo" />
    </div>
    <div class="content">
      <div class="card">
        <h1>GD-Fitness API</h1>
        <p>Welcome — the API is running.</p>
        <ul>
          <li><a href="/docs">Interactive docs (/docs)</a></li>
          <li><a href="/health">Health check (/health)</a></li>
          <li><a href="/hello">Example endpoint (/hello)</a></li>
        </ul>
      </div>
    </div>
  </body>
</html>
    """
    return HTMLResponse(content=html)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/hello")
async def hello():
    return {"message": "Welcome to GD-Fitness API"}
