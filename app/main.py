
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="GD-Fitness", version="0.1")


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
                    body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:40px;background:#f7fafc;color:#0f172a}
                    .card{background:#fff;padding:24px;border-radius:8px;box-shadow:0 4px 20px rgba(2,6,23,0.08);max-width:720px}
                    a{color:#0369a1}
                </style>
            </head>
            <body>
                <div class="card">
                    <h1>GD-Fitness API</h1>
                    <p>Welcome — the API is running.</p>
                    <ul>
                        <li><a href="/docs">Interactive docs (/docs)</a></li>
                        <li><a href="/health">Health check (/health)</a></li>
                        <li><a href="/hello">Example endpoint (/hello)</a></li>
                    </ul>
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
